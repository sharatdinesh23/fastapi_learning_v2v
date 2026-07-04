from fastapi import APIRouter,HTTPException,status
from schemas.orders_schema import OrderRequest,OrderResponse

order_router = APIRouter(prefix ="/orders",tags = ["Orders"])

orders = [
    {
        "order_id":1,
        "order_name":"yash",
        "status":"shipped"
    },
    {
        "order_id":2,
        "order_name":"Hayat",
        "status":"out_for_delivery"
    }
]

@order_router.get("/get_all",response_model = list[OrderResponse])
def get_orders():
    return orders


@order_router.get("/get/{order_id}",response_model = OrderResponse)
def get_order_by_id(order_id:int):
    for order in orders:
        if order["order_id"] == order_id:
            return order
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Order with id {order_id} not found")

@order_router.post("/create",response_model=OrderResponse)
def create_order(order:OrderRequest):
    orders.append(
        {
                "order_id":order.order_id,
                "order_name":order.order_name,
                "status":order.status
            }
    )
    return order

    


