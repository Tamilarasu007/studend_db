from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int
    course: str
