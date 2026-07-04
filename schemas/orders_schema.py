from pydantic import BaseModel
from datetime import datetime
from schemas.product_schema import ProductRequest,ProductResponse
from typing import List
from enum import Enum


class OrderStatus(str,Enum):
    CREATED = "created"
    SHIPPED = "shipped"
    OUT_FOR_DELIVERY = "out_for_delivery"
    DELIVERED = "delivered"
    RETURNED = "returned"


class OrderRequest(BaseModel):
    order_id:int
    order_name:str
    status: OrderStatus

class OrderResponse(BaseModel):
    order_id:int
    status:OrderStatus
