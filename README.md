ArtGallery: Django Framework with PostgreSQL Backend for Full Stack Development
This project focuses on showcasing artists artworks through a website built using the Django framework with PostgreSQL as the backend, employing full-stack development in Python. The platform provides artists with the ability to sell their artworks, and it includes three interfaces:

1.User Interface
2.Artist Interface
3.Admin Interface

Here are the steps to create the project:

1.Ensure that you have PyCharm IDE and PostgreSQL (PgAdmin) installed on your computer.

2.To create a Django project in PyCharm:
  - Open the terminal and execute the command "pip install django" to download the Django 
    package.
  - Use the command "django-admin startproject projectname" to initiate a Django project.
  - Navigate to the project directory using the "cd projectname" command.
  - Create apps within the Django project using the command "django-admin startapp yourappname."
  - 
3.After setting up the project and apps, go to the settings.py file inside your project. In the 'INSTALLED_APPS' section, include the apps of your project.

4.Include the app URLs in the project-level urls.py file (inside your project name directory).

5.Connect the PostgreSQL database to the project. A code snippet for the 'DATABASES' setting is provided in settings.py. Ensure you enter your respective database details.

6.The project includes functionality for sending emails for forgotten passwords. At the bottom of settings.py, ensure you provide your email address along with the password.

7.Template creation:
  - Create a directory at the project level named 'templates.'
  - Inside the templates directory, create subdirectories with the names of your respective apps.
  - Within the app directories, create HTML files corresponding to each app.

8.Static directory:
  - This directory is for storing styles and images.
  - Similar to the templates directory, create a static directory at the project level.
  - Create subdirectories named - css, js, images.
  - Store styles.css, script.js, and images as needed.
  - Create urls.py inside apps as there will be no urls.py in the apps by default.
  - Optionally, include forms.py if necessary.

9.Create superuser:
  - Enter the command "python manage.py createsuperuser" in the terminal.
  - Then give your user details like username,email(optional) and password.
  - To access the administration page - ' /admin ' in the url in browser. Then login with the credentials that you have given in the terminal.

10.Makemigration and migrate:
  - After creating the models for the table creation, you have to run the commands 'python manage.py makemigrations' and 'python manage.py migrate' in the terminal.
    

These steps are designed for beginners to create the project. Upon reviewing the repository, you will definitely understand the structure to be followed.





