import os
import json

import pytest
from rest_framework.test import APIClient

import sqlite3
from sqlite3 import Error

from django.conf import settings
from fyle_classroom.settings import BASE_DIR


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect('test_db.sqlite3')
        print('Created test DB', sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def django_db_setup():
    create_connection()
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'test_db.sqlite3',
    }
    os.system('python manage.py migrate')


@pytest.fixture
def student_1():
    return json.dumps({
        'student_id': 1,
        'user_id': 3
    })


@pytest.fixture
def student_2():
    return json.dumps({
        'student_id': 2,
        'user_id': 4
    })


@pytest.fixture
def teacher_1():
    return json.dumps({
        'teacher_id': 1,
        'user_id': 1
    })


@pytest.fixture
def teacher_2():
    return json.dumps({
        'teacher_id': 2,
        'user_id': 2
    })
