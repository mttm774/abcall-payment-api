# Description
This is the microservice artifact make with python 🐍 with flask 🌶️. This artifact represents the payment 🛒💳 bundle context to management the payment and invoice 🧾 process

# Made with
[![Python](https://img.shields.io/badge/python-2b5b84?style=for-the-badge&logo=python&logoColor=white&labelColor=000000)]()
[![Flask](https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white&labelColor=000000)]()
[![PostgreSQL](https://img.shields.io/badge/postgresql-699eca?style=for-the-badge&logo=postgresql&logoColor=white&labelColor=000000)]()

https://github.com/abcall-project/abcall-payment-api/actions/workflows/action.yaml/badge.svg

# Instructions to execute schedule

In local environment, if you need execute the schedule ⏰ to generate invoice then execute the follow command:

First to execute worker
```
celery -A flaskr.tasks.task.celery worker --loglevel=info
```

Next to execute beat:
```
celery -A flaskr.tasks.task.celery beat --loglevel=info
```