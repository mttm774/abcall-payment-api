from typing import List
from ..domain.models import Invoice
from ..domain.interfaces.invoice_repository import InvoiceRepository
from ..domain.interfaces.customer_repository import CustomerRepository
from ..infrastructure.mappers import InvoiceMapper
import uuid
from datetime import datetime

class InvoiceService:
    def __init__(self, repository: InvoiceRepository,customer_repository: CustomerRepository):
        self.repository = repository
        self.customer_repository=customer_repository

    def list_invoices_by_customer(self, customer_id)->str:
        invoices = self.repository.list_by_consumer_id(customer_id)
        mapper = InvoiceMapper()
        json_response =  mapper.list_response(invoices)
        return json_response
    
    def generate_invoices(self)->str:
        print('generate invoices')
        customers=self.customer_repository.list()
        now = int(datetime.now().strftime("%Y%m%d%H%M"))
        for item in customers:
            now+=1
            print(item.id)
            new_invoice=Invoice(uuid.uuid4(),
                                item.id,
                                f'I{now}',
                                uuid.uuid4(),
                                item.plan_rate,
                                0,
                                item.plan_rate,
                                'Emprendedor',
                                uuid.uuid4(),
                                'G',
                                datetime.now(),
                                None,
                                datetime.now(),
                                datetime.now()
                                )
            self.repository.create_invoice(new_invoice)
            #todo enviar la factura al reports