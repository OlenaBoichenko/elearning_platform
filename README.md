# E-learning Platform

## **Project Description**

The "E-learning Platform" is a modern educational web application that enables teachers and students to interact seamlessly within an educational ecosystem. The platform allows teachers to create and manage courses, upload lessons, and track student participation. Students, in turn, can browse available courses, enroll, complete lessons, and generate detailed progress reports.
This platform offers a user-friendly interface, responsive design, and dynamic functionality that ensures an engaging experience for all users. 

## **Distinctiveness and Complexity**

### **Distinctiveness**
This project is clearly distinct from others in the course due to the following:
1. **New Context**
   - The platform simulates a real-world, dynamic e-learning website by integrating features such as progress tracking and course completion. This level of realism sets it apart from projects like basic e-commerce or social network system. This platform focuses on educational workflows, including lesson progression, student tracking, and dual role functionality. Unlike a simple e-commerce site, it implements a structured e-learning system with role based workflows and educational content production and consumption platform. It’s based on hierarchical workflows—courses, lessons, and progress tracking which require more intricate backend and frontend logic, than any other project in the course. 
2. **Unique User Role Management**
   - Custom logic for role-based access ensures that the application provides distinct, flexible permissions for teachers and students. Unlike previous projects in this course, the application’s role management system is tailored for real-world educational workflows.
3. **Role Based System Views**
   - Teachers and students see the system and interact with it absolutely differently and have totally different workflows. This makes another major distinctive feature. Teachers can create courses, upload lessons, and monitor student participation, while students focus on enrolling in courses, completing them, and generating reports. This combination of user roles adds significant depth to the application. None of the previous projects in this course had a separation of user roles.
4. **Course creation framework**
   -  Each teacher has access to easy to use front-end interface where they can upload, structure and manage educational content they offer to students. The course content can be dynamicaly updated, and is permanently stored in the backend database. 

### **Complexity**
This project involves multiple layers of technical complexity:
1. **Dynamic Role-Based Access**
   - Django's built-in capabilities are used to create a robust role management system that supports teachers and students with distinct dashboards and features. This includes a clear separation of user access rights.
2. **Course and Lesson Management**
   - Django based backend powered by SQLite database allows Teachers to create detailed courses and upload lessons with associated metadata such as descriptions, videos and images. It allows to manage the dependencies between courses and lessons and adds another layer of complexity to my project.
3. **Student Progress Tracking**
   - JavaScript logic the platform dynamically tracks each student’s course progress.
4. **Image Processing with Pillow**
   - Teachers can upload images for courses and lessons, which are processed and optimized using the Pillow library. This ensures that uploaded media is appropriately formatted and resized for various devices.
5. **Mobile Responsiveness**
   - Designed to be fully responsive, the platform ensures optimal functionality and usability on desktops, tablets, and mobile devices. Bootstrap and custom CSS media queries were used extensively to achieve this goal.

## **Libraries and packages**
The project uses the following packages, which are listed in `requirements.txt`:
- `Django>=3.2,<4.0`
- `Pillow>=10.2.0,<11.2`

## **File structure**
- **`/project_root/`** — Main project directory
  - **`manage.py`** — Main script for working with Django
  - **`requirements.txt`** — List of dependencies
  - **`/elearning_platform/`** — Application directory with platform logic
    - **`models.py`** — contains a description of all courses application models that represent the main entities and their relationships. Each model corresponds to a table in the database.
    - **`views.py`** — contains a request processing logic for the courses application. It is responsible for the interaction between an user interface and a server.
    - **`urls.py`** — defines routes for the courses application. It associates URLs with corresponding views, allowing user requests to be processed.
    - **`wsgi.py`** - used to deploy the project on the server. It is responsible for setting up WSGI, which allows the web server to communicate with the Django application.
    - **`apps.py`** - allows to create user groups (Teachers and Students) automatically after applying migrations.
    - **`forms.py`** - contains forms for creating Courses and Lessons.
    - **`templates/`** — a folder for HTML-templates
        - **`available_courses.html`** — HTML-template to reflect available Courses for Students.
        - **`course_detail.html`** - HTML-template displays details of each Course such as Course Title, Course Description, Course Lessons.
        - **`course_list.html`** - HTML-template contains different interfaces for Teacher and Student.
        - **`course_report.html`** - HTML-template displays details of each completed Course Report, including Course Name, Username, Student Rating.
        - **`course_reports.html`** - HTML-template includes Reports on all completed Courses.
        - **`create_course.html`** - HTML-template is required for the Teacher to create a Course and includes a form for creating a Course, a form for creating Lessons, uploading images and videos, and adding a description.
        - **`edit_course.html`** - HTML-template is required for editing the Course by the Teacher.
        - **`home.html`** - HTML-template is the main page that displays a welcome message and an invitation to register or log in.
        - **`layout.html`** - Main HTML-template for all html pages.
        - **`lesson_detail.html`** - HTML-template reflects Lesson details such as Title, Description, Video, Progress Bar.
        - **`login.html`** - HTML-template allows the user to log in.
        - **`manage_courses`** - HTML-template allows to view all courses created by the Teacher and edit them.
        - **`my_courses.html`** - HTML-template permits the Student to view all Courses to which they are subscribed.
        - **`register.html`** - HTML-template allows the user to register.
        - **`student_dashboard`** - HTML-template gives the Student access to view available courses and enrolled courses. And also an opportunity to join any available course.
        - **`view_enrollements`** - HTML-template allows the Teacher to view subscriptions to their courses.
    - **`templatetags/`** — a folder that contains a file custom_filters.py.
        - **`custom_filters.py`** - This is a special filter and is necessary in order to be able to use a custom filter Django "add_class" that allows to add CSS classes to HTML form elements.
    - **`static/`** — Static files
        - **`lesson.js`** - Handler for going to a lesson when a link is clicked
        - **`lesson_detail.js`** - Logic for completing lessons and a progress bar.
        - **`styles.css`** - custom styles
        - **`default_course_image`** - The default image to load if a Teacher did not upload an image when creating a course.

## **How to run the application**
1. Clone the repository:
   ```bach
   git clone https://github.com/me50/OlenaBoichenko.git
   cd elearning_platform
2. Install all dependencies:
   ```bach
   pip install -r requirements.txt
3. Perform database migrations:
   ```bach
   python manage.py migrate
4. Start the development server:
   ```bach
   python manage.py runserver
5. Go to the address in your browser:
   ```bach
   http://127.0.0.1:8000/

## **Acknowledgments**
- I thank the course teachers for providing high-quality training material.
