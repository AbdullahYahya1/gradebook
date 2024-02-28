# Grade Book

Welcome to the Grade Book project! Our platform is designed to streamline grade management for educators, making it easier to track student progress, generate valuable statistics, and export necessary reports. This project has been tailor-made to cater to the needs of less privileged countries that may not have access to advanced web systems.

## Features and Benefits

- **Grade Management**: An intuitive interface for recording and organizing student grades.
- **CSV File Upload**: Teachers can upload a CSV file containing student information for quick and seamless student addition.
- **Individual Student Addition**: The option to add students one by one manually.
- **Multiple Classrooms**: Users can create and manage multiple classrooms with unique student sets.
- **Customizable Grade Formats**: Teachers can customize the grading format according to their preference.
- **Comprehensive Statistics**: The platform generates comprehensive statistics based on the entered grades.
- **Student Mark IDs**: Each student is assigned a unique mark ID, ensuring secure access to their grades.
- **Editable Student Information**: Teachers can edit or delete student information directly from the website.
- **Interactive Graphs**: The platform offers interactive graphs to visually represent class performance.
- **Downloadable CSV Grade Reports**: Teachers can download grade reports in CSV format for further analysis or sharing with stakeholders.

## Getting Started

- **Login**: Access the Grade Book platform with your unique credentials.
- **Add Classrooms**: Create multiple classrooms based on your teaching assignments.
- **Add Students**: Upload a CSV file for bulk addition or manually enter individual student details.
- **Generate Reports**: Generate insightful reports and view statistics to gauge the overall class performance.
- **Customize Formats**: Customize the report format as per your needs at the end of the semester.

## Distinctiveness and Complexity

This project stands out from anything we have created before. It's neither a social media app nor an e-commerce platform. It differs from other previous year's projects as well. The Grade Book fulfills the distinctiveness and complexity requirements by providing a unique solution for grade management, specifically targeted at educators in less privileged countries. The platform leverages Django for the back-end, JavaScript for the front-end, and is designed to be mobile-responsive. Its features, such as CSV file upload, customizable grade formats, comprehensive statistics, and downloadable CSV grade reports, make it more complex and robust compared to other projects in this course.

## File Structure

The project consists of the following components:

- **views.py**: Contains all the backend code. The main functions include:
    - `index`: Displays the appropriate page based on whether the user is registered or not.
    - `createClassroom`: Shows a form page to add a classroom.
    - `deleteRoom`: An API to delete a classroom.
    - `room`: The classroom page with tables, stats, and links to download CSV and add students.
    - `addStudent`: A form page to add one student.
    - `editStudent`: An API to edit student information.
    - `deleteStudent`: An API to delete student information.
    - `Login`, `logout`, and `register` functions copied from project 4.
    - `error`: Displays an error page in case a user attempts to manipulate the system.
    - `home`: The home page displaying relevant information.

- **models.py**: Contains the different models, including:
    - A `users` model.
    - A model for `Classroom`.
    - A model for `Student`.

- **app.js**: Handles page display and disabling, makes API calls for the views, and manages edit and delete functions.

- **index.js**: Handles page display and disabling, makes API calls for the views, and creates the download link for the image.

- **Templates**: Contains all the different HTML pages, including a layout file.

- **CSS files** Two CSS files with styling : 
    - A `room.css`:  for rooms styling  
    - A `styles.css`: for the rest of the page that is common
      
- **urls.py**: This file contains all the URL routing for our application. It maps URLs to their respective views.

- **admin.py**: We have registered our models here to utilize Django's built-in admin interface.

- **settings.py**: Contains all the settings for our Django application. We have added our application in the INSTALLED_APPS setting here.

## Running the Application

To run the Grade Book web application, follow these steps:

1. Install the required Python packages by running: `pip install -r requirements.txt`
2. Create and apply the necessary database migrations: 
    - `python manage.py makemigrations finalapp`
    - `python manage.py migrate`
3. Start the development server: `python manage.py runserver`

## Python Packages

Ensure that all the Python packages listed in the `requirements.txt` file are installed to run this web application successfully.
The following Python packages are necessary for our application:
    - `Django`
    - `matplotlib`
    
## Additional Information

During the development process, we faced numerous challenges, especially when it came to implementing CSV file uploads and generating interactive graphs. However, we were able to overcome these issues by leveraging Django's robust file-handling capabilities and making matplotlib for the graphs.

We made a conscious decision to design our application with a focus on user experience. This is why we implemented features like CSV file upload and bulk grade entry, which we believe will save educators significant time and effort.

## In Conclusion

The Grade Book project aims to enhance your teaching experience by providing a convenient and efficient platform for grade management. We appreciate your choice of Grade Book and look forward to assisting you in your noble educational endeavors.
