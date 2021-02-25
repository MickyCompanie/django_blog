# How To Use

## Requirements

- Python 3
- pip
- virtualenv 

## Setting up the environement

First, clone the repo on your machine and then navigate in it with your terminal

```bash
$ virtual env venv
```

then, to activate this environement:

- On linux:
    ```bash
    $ . venv/bin/activate
    ```

- on windows:
    ```bash
    $ venv\Scripts\activate.bat
    ```
if you whant to stop this virtual environement, simply type

```bash
$ deactivate
```

## Installing the tools we need

all we need to install is

```bash
$ pip install django django-crispy-forms pillow
```

## Creating a super user

Once it's done, move to the django_blog directory where `manage.py` exists:

```bash
$ cd django_blog/
```

```bash
$ python manage.py createsuperuser
```
Now Django will prompt you to enter the details, enter your desired details and hit enter.

## Migrate

first

```bash
$ python manage.py makemigrations
```

then

```bash
$ python manage.py migrate
```

## Using it

- start de developpement server:

    ```bash
    $ python manage.py runserver
    ```

- go to localhost:8000 in your web browser to see the project.

- connect with your super user id and password.

now you can: 
- create posts, update them in their page 
- change your profile informations 
- create other user either by login off and then signin up or going to localhost:8000/admin

> tips: you'll see pagination on the home page if you create more than 6 posts !
