from typing import Optional
from pydantic import BaseModel

class Category(BaseModel):
    idCategory: Optional[str] = None
    strCategory: Optional[str] = None
    strCategoryDescription: Optional[str] = None
    strCategoryThumb: Optional[str] = None

