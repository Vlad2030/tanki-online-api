from pydantic import BaseModel


class Response(BaseModel):
    responseType: str
