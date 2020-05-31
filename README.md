# Chinnawat Ong-art Challenge:

This is a challenge project from Manatal back end team to evaluate how good you are with building APIs with Django.

## Step 0 (spent 3 days)

- Learning

## Step 1 (spent 1 day)

The first step focuses on Django setup and models.

1. ✅ Create a Django app, with:
     - Postgres as a database
     - Pipenv as a Python dependency manager.
     - Environment file (for sensitive information, etc.)

2. ✅ Add models to create the following structure:
     - Students have a first name, a last name, and a student identification string (20 characters max for each)
     - Schools have a name (20 char max) and a maximum number of student (any positive integer)
     - Each student object must belong to a school object


## Step 2 (spent 1 day)

This second step focuses on Django Rest Framework (DRF).


1. ✅ Add __Django REST framework__ library to your project by using Pipenv

2. ✅ Enable and use the DRF browsable API for testing things manually.

3. ✅ Design your API according to specifications below (make sure to test and customize your solution) by creating urls, views, serializers, tests for all your models so that:
     - Endpoint `students/` will return all students (GET) and allow student creation (POST)
     - Endpoint `/schools/` will return all schools (GET) and allow school creation (POST)
     - Endpoint `/schools/:id` and `/students/:id` will return the object by :id (GET) and allow editing (PUT/PATCH) or deleting (DELETE)
     - Student creation will generate a unique identification string (like random hexadecimal or uuid4 or anything of your choice)
     - Trying to add a student in a full school (maximum number of student reached) will return a DRF error message


## Step 3 (Spent 0.5 day)

This third step focuses on __Django Nested Routers__.

1. ✅ Add Django Nested Routers library to your project by using Pipenv

2. ✅ Design your API according to specifications below:
     - Endpoint /schools/:id/students will return students who belong to school :id (GET)
     - Endpoint /schools/:id/students will allow student creation in the school :id (POST)
     - Your nested endpoint will allow GET/PUT/PATCH/DELETE methods on /schools/:id/students/:id
     - Your nested endpoint will respect the same two last rules of Step 2 too


## Bonus

- ✅ You can host your solution in Heroku (or other).
- ✅ You can add fields of your choice to students and schools such as location, nationality, age, etc. You can use Python Faker library to generate random data (names, etc) to populate fields.
- ✅ You can add search filters to your endpoints such as /students/?search=jeremy and you can add ordering filters as well, for example by age, by nationality, etc.
- ✅ You can add pagination or anything else that you wanna show us, feel free to add interesting stuff to this project!


## Heroku
- https://nameless-journey-20986.herokuapp.com/

## Pagination example

```
http://127.0.0.1:8000/schools/?page=1
```

# Searching example
## School
```
http://127.0.0.1:8000/schools/?name=Oxford  //name.contains('Oxford')
http://127.0.0.1:8000/schools/?min_capacity=5 //max_student >= 5
http://127.0.0.1:8000/schools/?max_capacity=5 //max_student <= 20
http://127.0.0.1:8000/schools/?min_capacity=5&max_capacity=8 //5 <= max_student <= 8

```
## Student
```
http://127.0.0.1:8000/students/?first_name=Chin //first_name.contains('Chin')
http://127.0.0.1:8000/students/?last_name=Chin //last_name.contains('Chin')
http://127.0.0.1:8000/students/?min_age=5 //age >= 5
http://127.0.0.1:8000/students/?max_age=5 //age <= 20
http://127.0.0.1:8000/students/?min_age=5&max_age=8 //5 <= age <= 8
http://127.0.0.1:8000/students/?address=Bangkok //address.contains('Bangkok')

```

# Ordering example
## School
```
http://127.0.0.1:8000/schools/?order_by_max_student=asc // order by max_student with ascending order
```
## Student
```
http://127.0.0.1:8000/students/?order_by_age=asc // order by age with ascending order
```

# Generate Fake data to database
## School
```
http://127.0.0.1:8000/gen_fake_school/
```
## Student
```
http://127.0.0.1:8000/gen_fake_students/
```