# health-info-system

# Description

This is a health information system for managing clients and health programs/services.It allows a doctor (system user) to
Create a health program – e.g., TB, Malaria, HIV, etc,register a new client in the system,enroll a client in one or more programs,search for a client from a list of registered clients,view a client's profile, including the programs they are enrolled in and expose the client profile via an API, so that other systems can retrieve this information.

# Set-up and Installation

git clone https://github.com/AdlightAkinyi/health-info-system.git

CD health-info-system

python -m venv virtual

source virtual/bin/activate

pip install -r requirements

python manage.py makemigrations neighbourhood

python manage.py migrate

# Running the app

python3 manage.py runserver

Open the application on your browser 127.0.0.1:8000.

# Technologies used
Python(Django)

HTML

 Bootstrap CSS

Javascript

SQLite



