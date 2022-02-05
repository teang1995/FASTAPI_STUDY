from typing import Optional

from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must gt zero")
    tax: Optional[float] = None
    image: Optional[Image] = None

    class Config:
        # 우리가 설정한 예시로 docs의 기본 예시에 덮힌다.
        schema_extra = {
            "example": {
                "name": "kani",
                "description": "fuck",
                "price": 12,
                "tax": 10.3,
                "image": {
                    "url": "fasdfa",
                    "name": "afdsda"
                }
            }
        }


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int,
                      item: Item = Body(..., embed=True)):
    # TODO: Body Class의 의미?
    results = {"item_id": item_id, "item": item}
    return results


@app.get("/items/{item_id}")
async def read_items(item_id: int = Path(default=1, ge=3)):
    # ... : 값이 무조건 있어야 한다는
    # TODO: default value 넣는 법?
    results = item_id
    return results