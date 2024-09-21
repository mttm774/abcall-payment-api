from typing import List
from ..domain.models import Invoice
from ..domain.interfaces.invoice_repository import InvoiceRepository
from ..domain.interfaces.customer_repository import CustomerRepository
from ..infrastructure.mappers import InvoiceMapper

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
        print(f'generate invoices')
        customers=self.customer_repository.list()
        for item in customers:
            print(item.id)
            #todo crear la factura
            #todo enviar la factura al reports