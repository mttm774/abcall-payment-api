from sqlalchemy import create_engine,extract, func
from sqlalchemy.orm import sessionmaker
from typing import List, Optional
from uuid import UUID
from ...domain.models import InvoiceDetail
from ...domain.interfaces import InvoiceDetailRepository
from ...infrastructure.databases.model_sqlalchemy import Base, InvoiceDetailModelSqlAlchemy

class InvoiceDetailPostgresqlRepository(InvoiceDetailRepository):
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
        self._create_tables()

    def _create_tables(self):
        Base.metadata.create_all(self.engine)

    def create_invoice_detail(self,invoice_detail: InvoiceDetail):
        session = self.Session()
        session.add(self._to_model(invoice_detail))
        session.commit()

    def _to_model(self, invoice_detail: InvoiceDetail) -> InvoiceDetailModelSqlAlchemy:
        return InvoiceDetailModelSqlAlchemy(
            id=invoice_detail.id,
            detail=invoice_detail.detail,
            amount=invoice_detail.amount,
            tax=invoice_detail.tax,
            total_amount=invoice_detail.total_amount,
            issue_id=invoice_detail.issue_id,
            chanel_plan_id=invoice_detail.chanel_plan_id,
            invoice_id=invoice_detail.invoice_id
        )

    def _from_model(self, model: InvoiceDetailModelSqlAlchemy) -> InvoiceDetail:
        return InvoiceDetail(
            id=model.id,
            detail=model.detail,
            amount=model.amount,
            tax=model.tax,
            total_amount=model.total_amount,
            issue_id=model.issue_id,
            chanel_plan_id=model.chanel_plan_id,
            invoice_id=model.invoice_id
            
        )
    