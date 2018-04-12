#### Requirements
[pip-tools](https://github.com/jazzband/pip-tools) is for managing requirements. There are
two sets of requirements - `requirements.in` and `requirements-test.in`, compiled to
`requirements.txt` and `requirements-test.txt` respectively.

#### Setup (using virtualenv)
**Prerequisites**:
- Python 3 (implemented with 3.6)
- [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

**Steps**:

1. Clone the repository.

2. `virtualenv -p python3 venv && source .venv/bin/activate`

3. `python manage.py migrate` to init db and run migrations

4. `python manage.py runserver`

   will start the application at `http://127.0.0.1:8000/` on your host -
   using Django's test server.
