from typing import List, Optional
from uuid import UUID
from ..models.invoice import Invoice

class InvoiceRepository:
    def list(self) -> List[Invoice]:
        raise NotImplementedError
    
    def list_invoices_by_customer(self, customer_id) -> List[Invoice]:
        raise NotImplementedError
    
    def create_invoice(self,invoice: Invoice):
        raise NotImplementedError
    
    def update_invoice(self,invoice: Invoice):
        raise NotImplementedError