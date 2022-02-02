import json

from django.urls import reverse
import pytest


@pytest.mark.django_db()
def test_get_assignments_student_1(api_client, student_1):
    response = api_client.get(
        reverse('students-assignments'),
        HTTP_X_Principal=student_1
    )

    assert response.status_code == 200

    assignments = response.json()
    assert type(assignments) == list

    for assignment in assignments:
        assert assignment['student'] == 1


@pytest.mark.django_db()
def test_get_assignments_student_2(api_client, student_2):
    response = api_client.get(
        reverse('students-assignments'),
        HTTP_X_Principal=student_2
    )

    assert response.status_code == 200

    assignments = response.json()
    assert type(assignments) == list

    for assignment in assignments:
        assert assignment['student'] == 2


@pytest.mark.django_db()
def test_post_assignment_student_1(api_client, student_1):
    content = 'ABCD TESTPOST'

    response = api_client.post(
        reverse('students-assignments'),
        data=json.dumps({
            'content': content
        }),
        HTTP_X_Principal=student_1,
        content_type='application/json'
    )

    assert response.status_code == 201

    assignment = response.json()
    assert assignment['content'] == content
    assert assignment['state'] == 'DRAFT'
    assert assignment['student'] == 1
    assert assignment['teacher'] is None
    assert assignment['grade'] is None
    assert assignment['id'] is not None


@pytest.mark.django_db()
def test_submit_assignment_without_teacher_student_1(api_client, student_1):
    response = api_client.patch(
        reverse('students-assignments'),
        data=json.dumps({
            'id': 2,
            'state': 'SUBMITTED'
        }),
        HTTP_X_Principal=student_1,
        content_type='application/json'
    )

    assert response.status_code == 400
    error = response.json()

    assert error['non_field_errors'] == ['Teacher ID has to be sent to set state to SUBMITTED']


@pytest.mark.django_db()
def test_submit_assignment_student_1(api_client, student_1):
    response = api_client.patch(
        reverse('students-assignments'),
        data=json.dumps({
            'id': 2,
            'state': 'SUBMITTED',
            'teacher_id': 1
        }),
        HTTP_X_Principal=student_1,
        content_type='application/json'
    )

    assert response.status_code == 200

    assignment = response.json()

    assert assignment['content'] is not None
    assert assignment['state'] == 'SUBMITTED'
    assert assignment['student'] == 1
    assert assignment['teacher'] == 1
    assert assignment['grade'] is None
    assert assignment['id'] is not None
