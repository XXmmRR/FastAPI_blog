from pydantic import BaseModel


class Article(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True


class CreateArticle(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class UpdateArticle(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True
