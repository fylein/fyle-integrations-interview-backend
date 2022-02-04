## Application 
### There are 4 resources:
- Users
- Students
- Teachers
- Assignments

4 Users (2 students and 2 teachers) have already been created for you in the db fixture

## User Actions:
- A student can create and edit a draft assignment
- A student can list all his created assignments
- A teacher can list all assignments submitted to him
- A teacher can grade an assignment submitted to him

## Available APIs
### Auth
- header: "X-Principal"
- value: {"user_id":4, "student_id":2}

For APIs to work you need a principal header to establish identity and context

### GET /student/assignments/
#### List all assignments created by a student
```
headers:
X-Principal: {"user_id":4, "student_id":2}

response:
[
  {
    "id": 1,
    "content": "This is assignment 1",
    "grade": null,
    "state": "DRAFT",
    "created_at": "2022-01-31T14:09:18Z",
    "updated_at": "2022-01-31T14:09:18Z",
    "student": 2,
    "teacher": 1
  },
  {
    "id": 4,
    "content": "This is assignment 4",
    "grade": null,
    "state": "SUBMITTED",
    "created_at": "2022-01-31T14:09:18Z",
    "updated_at": "2022-01-31T14:09:18Z",
    "student": 2,
    "teacher": 1
  },
  {
    "id": 5,
    "content": "This is assignment 5",
    "grade": "A",
    "state": "GRADED",
    "created_at": "2022-01-31T14:09:18Z",
    "updated_at": "2022-01-31T14:09:18Z",
    "student": 2,
    "teacher": 1
  },
  {
    "id": 8,
    "content": "This is assignment 8",
    "grade": "D",
    "state": "GRADED",
    "created_at": "2022-01-31T14:09:18Z",
    "updated_at": "2022-01-31T14:09:18Z",
    "student": 2,
    "teacher": 2
  }
]
```

### POST /student/assignments/
#### Create an assignment
```
headers:
X-Principal: {"user_id":4, "student_id":2}

payload:
{
    "content": "This is a new assignment"
}

response:
{
  "id": 12,
  "content": "This is a new assignment",
  "grade": null,
  "state": "DRAFT",
  "created_at": "2022-02-01T08:23:03.303983Z",
  "updated_at": "2022-02-01T08:23:03.304028Z",
  "student": 2,
  "teacher": null
}
```

### PATCH /student/assignments/
#### Edit an assignment
```
headers:
X-Principal: {"user_id":4, "student_id":2}

payload:
{
    "id": 12,
    "content": "Updated content of the new assignment"
}

response:
{
  "id": 12,
  "content": "Updated content of the new assignment",
  "grade": null,
  "state": "DRAFT",
  "created_at": "2022-02-01T08:23:03.303983Z",
  "updated_at": "2022-02-01T08:24:00.415712Z",
  "student": 2,
  "teacher": null
}
```

### PATCH /student/assignments/
#### Submit an assignment
```
headers:
X-Principal: {"user_id":4, "student_id":2}

payload:
{
    "id": 12,
    "state": "SUBMITTED",
    "teacher": 2
}

response:
{
  "id": 12,
  "content": "Updated content of the new assignment",
  "grade": null,
  "state": "SUBMITTED",
  "created_at": "2022-02-01T08:23:03.303983Z",
  "updated_at": "2022-02-01T08:25:55.782979Z",
  "student": 2,
  "teacher": 2
}
```

## Missing APIs
### Auth
- header: "X-Principal"
- value: {"user_id":1, "teacher_id":1}

For APIs to work you need a principal header to establish identity and context

### GET /teacher/assignments/
#### List all assignments submitted to this teacher
```
headers:
X-Principal: {"user_id":1, "teacher_id":1}

response:
[
  {
    "id": 1,
    "content": "This is assignment 1",
    "grade": null,
    "state": "DRAFT",
    "created_at": "2022-01-31T14:09:18Z",
    "updated_at": "2022-01-31T14:09:18Z",
    "student": 2,
    "teacher": 1
  },
  {
    "id": 4,
    "content": "This is assignment 4",
    "grade": null,
    "state": "SUBMITTED",
    "created_at": "2022-01-31T14:09:18Z",
    "updated_at": "2022-01-31T14:09:18Z",
    "student": 2,
    "teacher": 1
  },
  {
    "id": 5,
    "content": "This is assignment 5",
    "grade": "A",
    "state": "GRADED",
    "created_at": "2022-01-31T14:09:18Z",
    "updated_at": "2022-01-31T14:09:18Z",
    "student": 2,
    "teacher": 1
  }
]
```

### PATCH /teacher/assignments/
#### Grade an assignment
```
headers:
X-Principal: {"user_id":2, "teacher_id":2}

payload:
{
    "id":  3,
    "grade": "A"
}

response:
{
    "id": 3,
    "content": "This is assignment 3",
    "grade": "A",
    "state": "GRADED",
    "created_at": "2022-01-31T14:09:18Z",
    "updated_at": "2022-01-31T14:09:18Z",
    "student": 1,
    "teacher": 2
}
```