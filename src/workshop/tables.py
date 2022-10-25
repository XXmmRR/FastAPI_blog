import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = 'Article'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.Text)
    description = sq.Column(sq.Text)


class User(Base):
    __tablename__ = 'users'
    id = sq.Column(sq.Integer, primary_key=True)
    email = sq.Column(sq.Text, unique=True)
    username = sq.Column(sq.Text, unique=True)
    password_hash = sq.Column(sq.Text)
