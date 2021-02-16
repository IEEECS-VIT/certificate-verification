How to run on localhost?

STEP- 1 : SET up virtual environment 
          1. open terminal
          2. py -m venv project-name (create env)
          3. project-name\Scripts\activate.bat (activate env)

STEP-2 : run on terminal : pip install -r requirements.txt 
STEP-3 : goto certificate_verify/settings.py 
        DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'certificate_verification',
              'USER': 'postgres',
              'PASSWORD': 'postgres',
              'HOST': 'localhost'
            }
          }
          
         => find above code in settings.py and replace NAME, USER, PASSWORD with your postgres database password
STEP-4 : run on terminal : python manage.py makemigrations
STEP-5 : run on terminal : python manage.py migrate
STEP-6 : python manage.py runserver
STEP-7 : Done
