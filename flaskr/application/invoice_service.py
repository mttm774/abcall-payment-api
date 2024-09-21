from typing import List
from ..domain.models import Invoice
from ..domain.interfaces.invoice_repository import InvoiceRepository
from ..infrastructure.mappers import InvoiceMapper

class InvoiceService:
    def __init__(self, repository: InvoiceRepository):
        self.repository = repository

    def list_invoices_by_customer(self, customer_id)->str:
        invoices = self.repository.list_by_consumer_id(customer_id)
        mapper = InvoiceMapper()
        json_response =  mapper.list_response(invoices)
        return json_response
    
    def generate_invoices(self, customer_id)->str:
        print(f'generate invoices to {customer_id}')