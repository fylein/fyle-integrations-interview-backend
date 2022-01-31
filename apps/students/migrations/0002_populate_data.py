from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('internal', '0001_initial'),
        ('students', '0001_initial'),
    ]

    raw_query = """
        insert into users (email, created_at, updated_at) values 
        ('siva@fyle.in', datetime('now'), datetime('now')),
        ('gokul@fyle.in', datetime('now'), datetime('now')),
        ('rahul@fyle.in', datetime('now'), datetime('now')),
        ('chris@fyle.in', datetime('now'), datetime('now'));


        insert into teachers (user_id, created_at, updated_at) values 
        (1, datetime('now'), datetime('now')),
        (2, datetime('now'), datetime('now'));

        insert into students (user_id, created_at, updated_at) values 
        (3, datetime('now'), datetime('now')),
        (4, datetime('now'), datetime('now'));

        insert into assignments (content, state, created_at, updated_at, teacher_id, student_id) values
        ('This is assignment 1', 'DRAFT', datetime('now'), datetime('now'), 1, 2),
        ('This is assignment 2', 'DRAFT', datetime('now'), datetime('now'), 2, 1),
        ('This is assignment 3', 'SUBMITTED', datetime('now'), datetime('now'), 2, 1),
        ('This is assignment 4', 'SUBMITTED', datetime('now'), datetime('now'), 1, 2);

        insert into assignments (content, grade, state, created_at, updated_at, teacher_id, student_id) values
        ('This is assignment 5', 'A', 'GRADED', datetime('now'), datetime('now'), 1, 2),
        ('This is assignment 6', 'B', 'GRADED', datetime('now'), datetime('now'), 1, 1),
        ('This is assignment 7', 'C', 'GRADED', datetime('now'), datetime('now'), 2, 1),
        ('This is assignment 8', 'D', 'GRADED', datetime('now'), datetime('now'), 2, 2);
    """

    operations = [
        migrations.RunSQL(raw_query)
    ]