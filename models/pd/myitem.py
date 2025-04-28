from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict



class MyItemBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    name: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    meta: dict


class MyItemList(MyItemBase):
    id: int
