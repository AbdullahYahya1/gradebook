function getToken(name){
    const value = `; ${document.cookie}`  
    const parts = value.split(`; ${name}=`)
    if(parts.length == 2)
        return parts.pop().split(';').shift();
}

  





function page1(){
    document.querySelector('.page1').style.display="block"
    document.querySelector('.page2').style.display="none"
    document.querySelector('.page3').style.display="none"

}
function page2(){
    document.querySelector('.page1').style.display="none"
    document.querySelector('.page2').style.display="block"
    document.querySelector('.page3').style.display="none"
}
function page3(){
    document.querySelector('.page1').style.display="none"
    document.querySelector('.page2').style.display="none"
    document.querySelector('.page3').style.display="block"
}


function editStudent(student_id, target) {
    if (target === 'exit') {
        document.querySelector(`#score${student_id}`).innerHTML=document.querySelector(`#scoreValue${student_id}`).dataset.originalScore
        document.querySelector(`#name${student_id}`).innerHTML=document.querySelector(`#nameValue${student_id}`).dataset.originalScore
        document.querySelector(`#student_id_container${student_id}`).innerHTML= document.querySelector(`#oldstdid${student_id}`).dataset.originalScore;

        document.querySelector(`#button${student_id}`).innerHTML=`<a class="nav-link" onclick="editStudent(${student_id})" href="#">edit</a>`
        return;
    }
    if (target === 'save' || target === 'delete') {
        if(target === 'delete'){
            const scoreElement = document.querySelector(`#scoreValue${student_id}`);
            const nameElement = document.querySelector(`#nameValue${student_id}`);
            const idElement = document.querySelector(`#oldstdid${student_id}`);
            delete_student_score = scoreElement.dataset.originalScore
            delete_student_name =nameElement.dataset.originalScore
            delete_student_id = idElement.dataset.originalScore;
            classroom = document.querySelector('#classroom_id').value;


            if (scoreElement) {
                scoreElement.parentElement.parentElement.parentElement.removeChild(scoreElement.parentElement.parentElement)
            }
            const csrfToken = getToken('csrftoken');

            // ##################################
            fetch(`/deleteStudent/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({
                    student_score: delete_student_score,
                    student_name: delete_student_name,
                    student_id: delete_student_id,
                    room_id: classroom,
                }),
            }).then(response => response.json())
            .then(data => {
              console.log(data); // Handle the response data as needed
            })
            .catch(error => {
              console.error('Error:', error); // Handle the error
            });
            // ##################################
            return 
        }else if(target=='save'){

            newstudentID = document.querySelector(`#oldstdid${student_id}`).value;
            newscore= document.querySelector(`#scoreValue${student_id}`).value 
            newname=  document.querySelector(`#nameValue${student_id}`).value
            
            document.querySelector(`#score${student_id}`).innerHTML=newscore
            document.querySelector(`#name${student_id}`).innerHTML=newname
            document.querySelector(`#student_id_container${student_id}`).innerHTML = newstudentID
            document.querySelector(`#button${student_id}`).innerHTML=`<a class="nav-link" onclick="editStudent(${student_id})" href="#">edit</a>`
            classroom = document.querySelector('#classroom_id').value;
            // ##################################
            fetch(`/editStudent/${student_id}`, {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',
                  'X-CSRFToken': getToken('csrftoken')
                },
                body: JSON.stringify({
                  student_name: newname , 
                  student_score: newscore ,
                  new_student_id: newstudentID,
                  room_id: classroom,
                })
              })
              .then(response => response.json())
              .then(data => {
                console.log(data); // Handle the response data as needed
              })
              .catch(error => {
                console.error('Error:', error); // Handle the error
              });
            // ##################################
            return
        }
    }

    score = document.querySelector(`#score${student_id}`);
    student_name = document.querySelector(`#name${student_id}`);
    student_id_container = document.querySelector(`#student_id_container${student_id}`);

    if (score && student_name && student_id_container) {
        score.innerHTML = `<input class='s_score' id="scoreValue${student_id}" data-original-score='${(score.innerHTML)}' type="number" name="score" placeholder="score" value='${(score.innerHTML)}'> `;
        student_name.innerHTML = `<input class='s_name' id="nameValue${student_id}" type="text" name="name" value='${student_name.innerHTML}' data-original-score='${(student_name.innerHTML)}'>`;
        student_id_container.innerHTML = `<input class='s_id' id="oldstdid${student_id}" type="text" name="name" value='${student_id_container.innerHTML}' data-original-score='${(student_id_container.innerHTML)}'>`;
    }

    button_container = document.querySelector(`#button${student_id}`);

    button_container.innerHTML = `
        <a class="nav-link green" onclick='editStudent(${student_id},"save")' href='#'>save</a>
        <a class="nav-link black" onclick='editStudent(${student_id}, "exit")' href='#'>exit</a>
        <a class="nav-link red" onclick='editStudent(${student_id}, "delete")' href='#'>delete</a>
        `;
}

document.addEventListener("DOMContentLoaded", function() {
    var myDiv = document.getElementById("myDiv");
    
    if (myDiv) {
        document.querySelector('.page1').style.display="block"
        document.querySelector('.page2').style.display="none"
        document.querySelector('.page3').style.display="none"
    }
});



