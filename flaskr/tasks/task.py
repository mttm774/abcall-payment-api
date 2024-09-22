from celery import Celery
from celery.schedules import crontab
import os
from  config import Config
from ..application.invoice_service import InvoiceService
from ..infrastructure.databases.customer_postresql_repository import CustomerPostgresqlRepository
from ..infrastructure.databases.invoice_postgresql_repository import InvoicePostgresqlRepository


config=Config()

celery = Celery('tasks', broker=f'{config.SCHEDULE_BROKER}{config.TOPIC_SCHEDULE}')


@celery.task
def scheduled_generate_invoice_task():
    print("generating invoices!")
    repository = CustomerPostgresqlRepository(config.DATABASE_URI)
    repository_invoice = InvoicePostgresqlRepository(config.DATABASE_URI)
    invoice_service=InvoiceService(repository_invoice,repository)
    invoice_service.generate_invoices()


celery.conf.beat_schedule = {
    'run-generate-invoice-schedule': {
        'task': 'flaskr.tasks.task.scheduled_generate_invoice_task',
        'schedule': crontab(minute=f'*/{config.MINUTES_TO_EXECUTE_INVOICES}'),  
    },
}