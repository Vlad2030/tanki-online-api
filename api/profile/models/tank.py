from pydantic import BaseModel


class Hulls(BaseModel):
    grade: int
    id: int
    imageUrl: str
    name: str
    properties: None
    scoreEarned: int
    timePlayed: int


class Turrets(BaseModel):
    grade: int
    id: int
    imageUrl: str
    name: str
    properties: None
    scoreEarned: int
    timePlayed: int


class Drone(BaseModel):
    grade: int
    id: int
    imageUrl: str
    name: str
    properties: None
    scoreEarned: int
    timePlayed: int


class Paint(BaseModel):
    grade: int
    id: int
    imageUrl: str
    name: str
    properties: list
    scoreEarned: int
    timePlayed: int


class Resistance(BaseModel):
    grade: int
    id: int
    imageUrl: str
    name: str
    properties: list
    scoreEarned: int
    timePlayed: int


class Supplies(BaseModel):
    id: int
    imageUrl: str
    name: str
    usages: int
