from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('internal', '0001_initial'),
        ('students', '0001_initial'),
    ]

    raw_query = """
        insert into users (email, created_at, updated_at) values 
        ('siva@fyle.in', date('now'), date('now')),
        ('gokul@fyle.in', date('now'), date('now')),
        ('rahul@fyle.in', date('now'), date('now')),
        ('chris@fyle.in', date('now'), date('now'));


        insert into teachers (user_id, created_at, updated_at) values 
        (1, date('now'), date('now')),
        (2, date('now'), date('now'));

        insert into students (user_id, created_at, updated_at) values 
        (3, date('now'), date('now')),
        (4, date('now'), date('now'));

        insert into assignments (content, state, created_at, updated_at, teacher_id, student_id) values
        ('This is assignment 1', 'DRAFT', date('now'), date('now'), 1, 2),
        ('This is assignment 2', 'DRAFT', date('now'), date('now'), 2, 1),
        ('This is assignment 3', 'SUBMITTED', date('now'), date('now'), 2, 1),
        ('This is assignment 4', 'SUBMITTED', date('now'), date('now'), 1, 2);

        insert into assignments (content, grade, state, created_at, updated_at, teacher_id, student_id) values
        ('This is assignment 5', 'A', 'GRADED', date('now'), date('now'), 1, 2),
        ('This is assignment 6', 'B', 'GRADED', date('now'), date('now'), 1, 1),
        ('This is assignment 7', 'C', 'GRADED', date('now'), date('now'), 2, 1),
        ('This is assignment 8', 'D', 'GRADED', date('now'), date('now'), 2, 2);
    """

    operations = [
        migrations.RunSQL(raw_query)
    ]