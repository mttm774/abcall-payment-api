from uuid import UUID
from typing import Optional
from datetime import datetime

class InvoiceDetail:
    def __init__(self, id: UUID, detail: str, invoice_id: UUID, issue_id: Optional[UUID], amount: float, tax: float,
                 total_amount: float, chanel_plan_id: UUID):
        self.id = id
        self.detail=detail
        self.amount=amount
        self.tax=tax
        self.total_amount=total_amount
        self.issue_id=issue_id
        self.chanel_plan_id=chanel_plan_id
        self.invoice_id=invoice_id