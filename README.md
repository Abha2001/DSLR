# A role based access control system

## For non admin users:

- User can signup and login as a non admin.
- Only their own profile will be visible to non admins.

## For admins
- The first admin user can only be created by the superuser
- An admin can create other admin and non admin users
- An admin can view all users 
- An admin user can delete non admin users

## Setup project

`git clone https://github.com/Abha2001/DSLR.git`
`cd DSLR`

create virtual environment

`pip install -r requirements.txt`

create superuser

`python manage.py runserver`

Navigate to localhost:8000!



