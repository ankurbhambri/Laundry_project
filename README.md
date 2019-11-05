# Laundry_project

Quick Setup:
1.Create a vitual environment.
virtualenv -p python3.6 venv
2.Activate your virtual environment by
source venv/bin/activate
3.Install required python libraries by using pip.
pip install -r requirements.txt
4.Migrate database queries.
python manage.py migrate
5.Finally, run your django runserver.
python manage.py runserver
