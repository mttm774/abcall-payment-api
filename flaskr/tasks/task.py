from celery import Celery
from celery.schedules import crontab
import os
from  config import Config
from ..application.invoice_service import InvoiceService


config=Config()

celery = Celery('tasks', broker=f'{config.SCHEDULE_BROKER}{config.TOPIC_SCHEDULE}')


@celery.task
def scheduled_generate_invoice_task():
    print("generating invoices!")
    invoice_service=InvoiceService(None)
    invoice_service.generate_invoices(None)


celery.conf.beat_schedule = {
    'run-generate-invoice-schedule': {
        'task': 'flaskr.tasks.task.scheduled_generate_invoice_task',
        'schedule': crontab(minute=f'*/{config.MINUTES_TO_EXECUTE_INVOICES}'),  
    },
}