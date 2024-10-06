from typing import List
from ..domain.models import Invoice
import requests
from ..domain.interfaces.invoice_repository import InvoiceRepository
from ..domain.interfaces.customer_repository import CustomerRepository
from ..infrastructure.mappers import InvoiceMapper
import uuid
from datetime import datetime
from ..utils import Logger
from  config import Config

class InvoiceService:
    def __init__(self, repository: InvoiceRepository,customer_repository: CustomerRepository=None):
        self.log = Logger()
        self.repository = repository
        self.customer_repository=customer_repository

    def list_invoices_by_customer(self, customer_id)->str:
        invoices = self.repository.list_by_consumer_id(customer_id)
        mapper = InvoiceMapper()
        json_response =  mapper.list_response(invoices)
        return json_response
    
    def generate_invoices(self)->str:
        self.log.info('generating invoices')
        customers=self.customer_repository.list()
        now = int(datetime.now().strftime("%Y%m%d%H%M"))
        for item in customers[:500]:
            now+=1
            self.log.info(f'generating invoice I{now}')
            new_invoice=Invoice(uuid.uuid4(),
                                item.id,
                                f'I{now}',
                                uuid.uuid4(),
                                item.plan_rate,
                                0,
                                item.plan_rate,
                                'Emprendedor',
                                uuid.uuid4(),
                                'G', #Generada con éxito
                                datetime.now(),
                                None,
                                datetime.now(),
                                datetime.now()
                                )
            self.repository.create_invoice(new_invoice)
            #generating invoice
            if self.__send_invoice_to_document(new_invoice)==False:
                #error creating pdf document
                new_invoice.status='E' # no fue posible generar la factura
                self.repository.update_invoice(new_invoice)


    def __send_invoice_to_document(self,invoice: Invoice):
        """
        method to send invoice to create document pdf 
        Args:
            invoice (Invoice): invoice to process
        Return:
           None
        """
        try:
            config=Config()
            data={
                "id":str(invoice.id),
                "customer_id":str(invoice.customer_id),
                "invoice_id":invoice.invoice_id,
                "payment_id":str(invoice.payment_id),
                "amount":str(invoice.amount),
                "tax":str(invoice.tax),
                "total_amount":str(invoice.total_amount),
                "subscription":invoice.subscription,
                "subscription_id":str(invoice.subscription_id),
                "status":invoice.status,
                "created_at": invoice.created_at.isoformat() if invoice.created_at else None,
                "updated_at": invoice.updated_at.isoformat() if invoice.updated_at else None,
                "generation_date": invoice.generation_date.isoformat() if invoice.generation_date else None,
                "period":invoice.period.isoformat() if invoice.generation_date else None,
            }
            self.log.info('calling endpoint to generate pdf invoice ')
            response = requests.post(f'{config.URL_REPORTS_SERVICE}/invoice',json=data)
            self.log.info('api reports called')
            if response.status_code == 200:
                self.log.info('invoice created')
                data = response.json()
                self.log.info('invoice generated successfull')
                return True
            else:
                self.log.error(f'error in service to generate pdf invoice {response.status_code}')
                return False
            
        except Exception as e:
            self.log.error(f'Comunication error with reports service: {str(e)}')
            return False