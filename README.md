🧑‍💻 Django Portfolio Management System

A personal Portfolio Management System built with Django, where users can register, log in, and manage their professional information including profile details, education, work experience, and projects. The system automatically generates a professional resume view, which can be printed as a PDF-friendly format.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🚀 Features

✅ User registration and authentication (custom userModel)
✅ Profile management with image upload
✅ Add and manage education, work experience, and projects
✅ Beautiful resume view (auto-generated from user data)
✅ Responsive and print-friendly resume template
✅ Secure with Django’s authentication system


```
project_root/
│
├── protfolio/
│   ├── models.py         
│   ├── views.py           
│   ├── forms.py          
│   ├── templates/
│   │   ├── base.html      
│   │   ├── auth/          
│   │   ├── profile/      
│   │   └── project/       
│   └── static/            
│
├── manage.py
└── requirements.txt
```



🧠 Models Overview
userModel

Custom user model inheriting from AbstractUser.

profileModel

Stores user details like full name, phone, address, and profile picture.

EduModel

Contains education information such as degree, institution, grade, and passing year.

workExModel

Stores work experience including company name, designation, and duration.

projectModel

Holds project details including project name, description, and completion date.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


⚙️ How It Works

1.User registers an account and logs in.

2.Profile page allows updating full name, phone, address, and profile image.

3.Add Details page allows adding education, work experience, and project info.

4.The Home/Resume page displays all the data in a clean, professional layout.

5.Users can print their resume directly from the browser.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


🖼️ Templates Included

1.base.html → Resume layout

2.profile/profile.html → Profile edit form

3.project/projectAdd.html → Add projects, work, and education

4.auth/login.html and auth/register.html → Authentication pages

5.All templates are styled with custom CSS (no external frontend framework required).

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧰 Technologies Used

Python 3.10+

Django 5.x

SQLite (default)

HTML, CSS 

Pillow (for image upload)



🔧 Setup Instructions
1. Create a Virtual Environment

```
python -m venv venv
source venv/bin/activate  # on macOS/Linux
venv\Scripts\activate     # on Windows
```
2.Install Dependencies

```
pip install -r requirements.txt
```

3. Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```
5. Run the Development Server
```
python manage.py runserver
```
7. Open in Browser



Go to → http://127.0.0.1:8000/
🧾 Example Pages

1./register – Create an account

2./login – Login to your account

3./home – Resume view

4./profile – Edit your personal profile

5./add-details – Add work, education, and projects

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📸 Screenshots

This is my resume in the website
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<img width="530" height="541" alt="resume" src="https://github.com/user-attachments/assets/cf10da7f-d0e3-48b9-b639-45c4c7f3ed76" />

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<img width="368" height="537" alt="profile" src="https://github.com/user-attachments/assets/e7f20fbb-c997-4e4b-a21b-3379ed7b0815" />

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<img width="377" height="541" alt="add profile" src="https://github.com/user-attachments/assets/d4c02860-7911-497f-b2f7-80671dcd39c8" />

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

MD ZIHAD HOSSAIN

Diploma in Computer Science | Django Developer

📧 mdzihad01793561142@gmail.com

