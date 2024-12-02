# E-learning Platform

## **Project Description**

Project "E-learning platform" is an educational platform that allows teachers and students to interact within the educational process. In this project, teachers can create and edit courses, add lessons, and track which courses students have signed up for. Students can view available courses, sign up for courses, complete courses, and view completed course reports. The platform is developed using modern technologies, which allows us to provide a convenient and functional user interface.

## **Distinctiveness and Complexity**

### **Distinctiveness**
The project stands out from other projects in this course in that it includes both features for teachers (create and manage courses, track subscriptions) and students (view courses, subscribe, complete courses, view reports). This combination of roles and functionality makes the project more comprehensive and closer to the real educational system. I also used my own logic to manage user roles, which allows for more flexibility in working with access rights and functionality for different types of users.

### **Complexity**
The project includes several complex technical aspects:
- Manage user roles with different access rights (teachers and students).
- Creation and management of courses, lessons, student subscriptions.
- Completed course reports.
- Implementation of the interface using HTML, CSS and JavaScript to improve user experience.
- Interaction between frontend and backend using Django.

## **Technologies**
- **Django**: to implement server logic and interact with the database.
- **JavaScript, HTML, CSS, Bootstrap**: for user interface development.
- **Pillow**: for images processing.

## **Libraries and packages**
The project uses the following packages, which are listed in `requirements.txt`:
- `Django>=3.2,<4.0`
- `Pillow>=10.2.0,<11.2`

## **File structure**
- **`/project_root/`** — Main project directory
  - **`manage.py`** — Main script for working with Django
  - **`requirements.txt`** — List of dependencies
  - **`/elearning_platform/`** — Application directory with platform logic
    - **`models.py`** — Database models
    - **`views.py`** — Views and query processing
    - **`urls.py`** — Routes and routing
    - **`templates/`** — HTML-templates
    - **`static/`** — Static files (CSS, JavaScript, images)

## **How to launch the application**
1. Clone the repository:
   ```bach
   git clone <repository_url>
   cd <project_name>
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

## **Project idea**
The idea for the project arose from the desire to create a functional educational platform that would cover a wide range of tasks for both teachers and students. This platform provides flexible options for creating courses and managing student subscriptions, making the learning process more convenient and efficient.

## **Acknowledgments**
- I thank the course teachers for providing high-quality training material.

