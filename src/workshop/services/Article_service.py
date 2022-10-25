import fastapi
from fastapi.responses import Response
from fastapi import status
import workshop.tables as tables
from workshop.database import get_session
from workshop.models.Article_models import CreateArticle, UpdateArticle, Article
from fastapi import Depends
from sqlalchemy.orm import Session

from typing import (List,
                    Optional)


class ArticleService:
    def __init__(self, session: Session = Depends(get_session),
                 ):
        self.session = session

    def _get(self, article_id: int) -> tables.Article:
        article = (
            self.session
            .query(tables.Article)
            .filter_by(id=article_id)
            .first()
        )
        if not article:
            raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND)
        return article

    def get_list(self) -> List[tables.Article]:
        query = self.session.query(tables.Article)
        articles = query.all()
        if not articles:
            raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND)
        return articles

    def create(self, article_data: CreateArticle) -> tables.Article:
        article = tables.Article(**article_data.dict())
        self.session.add(article)
        self.session.commit()
        return article

    def delete(self, article_id: int):
        article = self._get(article_id=article_id)
        self.session.delete(article)
        self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    def update(self, article_id: int, article_data: UpdateArticle):
        article = self._get(article_id=article_id)
        for field, value in article_data:
            setattr(article, field, value)
        self.session.commit()
        return article
