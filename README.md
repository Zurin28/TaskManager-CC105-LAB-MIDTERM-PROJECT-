
# Task Manager

This is a Django-based CRUD application for managing tasks with specific business logic.

## Project Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x or later
- MySQL server
- Git

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/task_manager.git
   cd task_manager
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the MySQL database:**

   - Ensure MySQL server is running.
   - Create a database named `taskManager`.

   ```sql
   CREATE DATABASE taskManager;
   ```

5. **Configure the database settings:**

   Ensure the `DATABASES` setting in `myProject/settings.py` is configured as follows:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'taskManager',
           'USER': 'root',
           'PASSWORD': '',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

6. **Apply migrations:**

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

8. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/` to access the Task Manager application.

