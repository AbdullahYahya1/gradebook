import csv
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render , redirect
from django.urls import reverse 
import matplotlib
import matplotlib.pyplot as plt
import io
from io import StringIO
import base64
from .models import User , Classroom , Student
import json
from .forms import CSVUploadForm

def index(request):
    if request.user.is_authenticated:
        rooms =  Classroom.objects.filter(doctor=request.user).order_by('-date')
        return render(request, "finalapp/doctor.html" , {"rooms": rooms})
    
    if not request.user.is_authenticated and request.method =='POST':
        try:
            student = Student.objects.get(student_id =  request.POST['id'] , name=request.POST['name'] , pk = request.POST['markid'])
            return render(request, "finalapp/index.html" , {'student':student})
        except:
            return render(request, "finalapp/index.html" , {'massage':'no student with this info'})
        
    return render(request, "finalapp/index.html")

    




def addStudent(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '')
            student_id =  int(request.POST.get('student_id', ''))
            print('here')
            classroom_id = request.POST.get('classroom_id', '')
            score = int(request.POST.get('score'))
            student = Student(name=name , student_id=student_id , classroom_id=classroom_id , score=score )
            student.save()
            return redirect(reverse('room' , args=[classroom_id]))
        except :
            return redirect(reverse('error'))
    
    
def createClassroom(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if request.user.is_authenticated and request.method =="GET":
        return render(request, "finalapp/createClassroom.html")

    if request.user.is_authenticated and request.method == 'POST':
        field_value = request.POST.get('classRoom')
        field_value2 = request.POST.get('subject')
        myyclassroom = Classroom(name = field_value , doctor = request.user , subject = field_value2)
        myyclassroom.save()
        return redirect(reverse('index'))
    return redirect(reverse('index'))
def deleteRoom(request , room_id):
    print(room_id)
    try: 
        myclass = Classroom.objects.get(id=room_id , doctor=request.user)
        myclass.delete()
        return JsonResponse({'status': 'good'})
    except:
        return JsonResponse({'status': 'bad'})
def room(request, room_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.user.is_authenticated and Classroom.objects.get(pk = room_id,doctor=request.user):
        classroomv =  Classroom.objects.get(pk = room_id,doctor=request.user)
        Students = classroomv.students.all()
        
        try:
            query_param = request.GET.get('query')
            if query_param =='max':
                Students = Students.order_by('-score')
            if query_param =='min':
                Students = Students.order_by('score')  
            if 'CSV' in query_param:
                if('m' in query_param ):
                    Students = Students.order_by('name' , '-score')
                elif('n' in query_param):
                    Students = Students.order_by('score')
                elif('x' in query_param):
                    Students = Students.order_by('-score')
                csv_buffer = StringIO()
                csv_writer = csv.writer(csv_buffer)
                csv_writer.writerow(['Name', 'ID', 'Score'])
                for student in Students:
                    if('CSVS' in query_param):
                        csv_writer.writerow([student.name, student.student_id, student.transScore()])
                    else:
                        csv_writer.writerow([student.name, student.student_id, student.score])        
                response = HttpResponse(csv_buffer.getvalue(), content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="{classroomv.name}_students.csv"'
                return response
            if 'markID' == query_param:
                csv_buffer = StringIO()
                csv_writer = csv.writer(csv_buffer)
                csv_writer.writerow(['studentID', 'markID'])
                for student in Students:
                    csv_writer.writerow([student.student_id, student.id])
                response = HttpResponse(csv_buffer.getvalue(), content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="{classroomv.name}_students_Mark_id.csv"'
                return response                
        except :
            pass 
        
        form = CSVUploadForm()

        if(Students):
            score_array =list( classroomv.students.values_list('score', flat=True))
            matplotlib.use('Agg')
            grades = {student.id: student.transScore() for student in Students}
            grade_counts = {}
            for grade in grades.values():
                grade_counts[grade] = grade_counts.get(grade, 0) + 1     
            plt.figure(figsize=(8, 8))
            plt.pie(grade_counts.values(), labels=grade_counts.keys(), autopct='%1.1f%%', startangle=140)
            plt.xlabel('Grades')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            plt.clf()  
            plt.close()
            buffer.seek(0)
            image_base64 = base64.b64encode(buffer.getvalue()).decode()
            img = f'<img src="data:image/png;base64,{image_base64}" alt="Grade Distribution">'             
            return render(request, "finalapp/room.html", {
                'room': classroomv,
                'Students':Students,
                'imglink':f'image/png;base64,{image_base64}',
                'img': img,
                'avg':sum(score_array)/len(score_array),
                'min_score': min(score_array), 
                'max_score': max(score_array),
                'form': form,
                })
        return render(request, "finalapp/room.html", {
                'room': classroomv,
                'Students':Students,
                'form': form,
                })
    
    
    
def editStudent(request, Student_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == 'POST':
        data = json.loads(request.body)    
        try:
            myclass = Classroom.objects.get(doctor=request.user , id = data['room_id'])
            student = Student.objects.get(id=Student_id)
        except:
            return JsonResponse({
                'status': 'failed'
            })
        if(data and (student in myclass.students.all())):
            try:
                student.name=(data['student_name'])
                student.student_id =int(data['new_student_id'])
                student.score=int((data['student_score']))
                student.save()
                return JsonResponse({
                    'status': 'success'
                })
            except :      
                return JsonResponse({
                    'status': 'failed'
                })
        else:
            return JsonResponse({
                'status': 'failed'
            })

def deleteStudent(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == 'POST':
        data = json.loads(request.body)
        try:         
            student = Student.objects.get(
                                    student_id=int(data['student_id']),
                                    name=data['student_name'],
                                    classroom=Classroom.objects.get(doctor=request.user , id = data['room_id']),
                                    score=int(data['student_score']))
        except:
            return JsonResponse({'status': 'still not deleted'})
        student.delete()
        return JsonResponse({'status': 'Student deleted successfully.'})
    else:
        return JsonResponse({'status': 'Student deleted successfully.'})
        

        
def upload_csv(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            
            if not csv_file.name.endswith('.csv'):
                return redirect(reverse('error'))

            csv_file_text_mode = csv_file.read().decode('utf-8-sig')
            csv_reader = csv.reader(csv_file_text_mode.splitlines())

            header_row = next(csv_reader)
            column_names = [column.strip() for column in header_row]
            column_names = list(map(lambda x: str(x).upper(), column_names))
            
            required_columns = { 'NAME', 'SCORE','ID'}
            if not required_columns.issubset(column_names):
                return redirect(reverse('error'))
                

            classroom_id = request.POST.get('classroom_id', '')
            myclass = Classroom.objects.get(doctor=request.user, id=classroom_id)
            try:
                for row in csv_reader:
                    student_data = dict(zip(column_names, row))
                    new_student = Student(
                        name=student_data['NAME'],
                        student_id=int(student_data['ID']),
                        classroom=myclass,
                        score=int(student_data['SCORE'])
                    )
                    new_student.save()
            except:
                return redirect(reverse('error'))
                        
                
            return HttpResponseRedirect(reverse("room" , args={classroom_id}))

                

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "finalapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "finalapp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "finalapp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "finalapp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "finalapp/register.html")


def error(request):
    return render(request, "finalapp/error.html" , {'error1': '##error##'})


def home(request):
    return render(request, "finalapp/home.html")