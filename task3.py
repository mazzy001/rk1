import threading

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()
next_id = 1
lock = threading.Lock()


class Item(BaseModel):
    name: str
    price: float = Field(gt=0)
    tags: list[str] = Field(default_factory=list)


class ItemWithId(Item):
    id: int


@app.post("/items", response_model=ItemWithId)
def create_item(item: Item) -> ItemWithId:
    global next_id
    with lock:
        result = ItemWithId(id=next_id, **item.model_dump())
        next_id += 1
    return result
