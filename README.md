# Outline

- What are prerequisites?
- How to setup development environment?
- How to run backend server?
- How to test? 
- Thoguths on deployment
- Lincese

## Prerequisites
    - Ubuntu 16.04.1 LTS
	- git 2.7.4
	- python 3.5.2
	- pip 19.0.3
	- virtualenv 15.1.0

**N.B.**: Backend developed in given environment. If you run on problem please create bug issue in current project. 
	
## How to setup development environment?

- Download backend code by running following code:
```bash
git clone https://github.com/elibrarium/backend.git
```

- Createt virtual environment and activate it:
```bash
cd backend/
virtualenv --python=python3.5 --prompt="[v]" .env
source .env/bin/activate
```

- Install python requirements in virtual environment:
```bash
pip install -i requirements/development.txt
```

- Run migrations
```bash
python manage.py migrate
```

- Create default default user:
```bash
cat create_superuser.py | python manage shell
```

**N.B.:** Feel free change username and password directly or by providing environment variable.


## How to run backend server?

- In order to run server in your development environment do following
```bash
cd backend/
virtualenv --python=python3.5 --prompt="[v]" .env
source .env/bin/activate
python manage.py runserver
```

## How to test? 

** Will be updated later **

## Thoguths on deployment

** Will be updated later **

