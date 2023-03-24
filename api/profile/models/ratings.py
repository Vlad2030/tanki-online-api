from pydantic import BaseModel


class Mount(BaseModel):
    armor: str
    coloring: str
    weapon: str


class Rating(BaseModel):
    position: int
    value: int
    efficiency: None
