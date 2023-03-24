from pydantic import BaseModel


class Profile(BaseModel):
    caughtGolds: int
    deaths: int
    earnedCrystals: int
    gearScore: int
    hasPremium: bool
    kills: int
    name: str
    rank: int
    score: int
    scoreBase: int
    scoreNext: int


class Mode(BaseModel):
    name: str
    scoreEarned: int
    timePlayed: int
    type: int


class Present(BaseModel):
    count: int
    imageUrl: str
    name: str
    prototypeId: int
