from typing import List, Optional
from uuid import UUID
from ..models.customer import Customer

class CustomerRepository:
    def list(self) -> List[Customer]:
        raise NotImplementedError