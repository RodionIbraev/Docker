import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory(_quantity=10)
    responce = client.get('/api/v1/courses/', {id: course[0].id})
    data = responce.json()
    assert data[0]['id'] == course[0].id
    assert responce.status_code == 200
