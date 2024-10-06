from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List, Optional
from uuid import UUID
from ...domain.models import Customer
from ...domain.interfaces import CustomerRepository
from ...infrastructure.databases.customer_model_sqlalchemy import Base, CustomerModelSqlAlchemy

class CustomerPostgresqlRepository(CustomerRepository):
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
        self._create_tables()

    def _create_tables(self):
        Base.metadata.create_all(self.engine)
    
    def list(self) -> List[Customer]:
        session = self.Session()
        try:
            customer_models = session.query(CustomerModelSqlAlchemy).all()
            return [self._from_model(invoice_model) for invoice_model in customer_models]
        finally:
            session.close()


    def _from_model(self, model: CustomerModelSqlAlchemy) -> Customer:
        return Customer(
            id=model.id,
            name=model.name,
            plan_rate=model.plan_rate,
            bill_date=model.bill_date
        )