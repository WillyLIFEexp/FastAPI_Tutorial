from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    name: str = Field(..., description="The name of the item")
    description: Optional[str]=None
    price: float = Field(..., gt=0, description="The price of the item; must be greater than zero")

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str]=None
    description: Optional[str]=None
    price: Optional[float]=None

class ProductResponse(ProductBase):
    # using Field(...) means that when creating an instance of the model, a value for id must be provided.
    id: str = Field(..., alias="id")
    created_at: datetime


    model_config = ConfigDict(from_attributes=True)

