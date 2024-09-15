from sqlalchemy import Column, String, Numeric, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid

Base = declarative_base()

class InvoiceModelSqlAlchemy(Base):
    __tablename__ = 'invoices'

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    invoice_id = Column(String(50), nullable=False)
    customer_id = Column(PG_UUID(as_uuid=True), nullable=True)
    payment_id = Column(PG_UUID(as_uuid=True), nullable=True)
    amount = Column(Numeric(10, 2), nullable=False)
    tax = Column(Numeric(10, 2), nullable=False)
    total_amount = Column(Numeric(10, 2), nullable=False)
    subscription = Column(String(100), nullable=False)
    subscription_id = Column(PG_UUID(as_uuid=True), nullable=False)
    status = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    generation_date = Column(DateTime(timezone=True), nullable=False)
    period = Column(DateTime(timezone=True), nullable=False)