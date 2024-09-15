from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List, Optional
from uuid import UUID
from ...domain.models import Invoice
from ...domain.interfaces import InvoiceRepository
from ...infrastructure.databases.invoice_model_sqlalchemy import Base, InvoiceModelSqlAlchemy

class InvoicePostgresqlRepository(InvoiceRepository):
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
        self._create_tables()

    def _create_tables(self):
        Base.metadata.create_all(self.engine)
    
    def list_by_consumer_id(self, customer_id) -> List[Invoice]:
        session = self.Session()
        try:
            invoice_models = session.query(InvoiceModelSqlAlchemy).filter_by(customer_id=customer_id).all()
            return [self._from_model(invoice_model) for invoice_model in invoice_models]
        finally:
            session.close()

    def list(self) -> List[Invoice]:
        session = self.Session()
        try:
            invoice_models = session.query(InvoiceModelSqlAlchemy).all()
            return [self._from_model(invoice_model) for invoice_model in invoice_models]
        finally:
            session.close()

    def _to_model(self, invoice: Invoice) -> InvoiceModelSqlAlchemy:
        return InvoiceModelSqlAlchemy(
            id=invoice.id,
            customer_id=invoice.customer_id,
            invoice_id=invoice.invoice_id,
            payment_id=invoice.payment_id,
            amount=invoice.amount,
            tax=invoice.tax,
            total_amount=invoice.total_amount,
            subscription=invoice.subscription,
            subscription_id=invoice.subscription_id,
            status=invoice.status,
            created_at=invoice.created_at,
            updated_at=invoice.updated_at,
            generation_date=invoice.generation_date,
            period=invoice.period
        )

    def _from_model(self, model: InvoiceModelSqlAlchemy) -> Invoice:
        return Invoice(
            id=model.id,
            customer_id=model.customer_id,
            invoice_id=model.invoice_id,
            payment_id=model.payment_id,
            amount=model.amount,
            tax=model.tax,
            total_amount=model.total_amount,
            subscription=model.subscription,
            subscription_id=model.subscription_id,
            status=model.status,
            created_at=model.created_at,
            updated_at=model.updated_at,
            generation_date=model.generation_date,
            period=model.period
        )