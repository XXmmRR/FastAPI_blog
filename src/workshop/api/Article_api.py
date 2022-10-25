from fastapi import APIRouter
from typing import List, Optional
from fastapi import Depends
from fastapi import Response
from fastapi import status

from models.Article_models import Article, CreateArticle, UpdateArticle
from services.Article_service import ArticleService

router = APIRouter(
    prefix='/article',
)


@router.get('/', response_model=List[Article])
def get_articles(service: ArticleService = Depends()):
    return service.get_list()


@router.post('/', response_model=CreateArticle)
def create_article(
    article_data: CreateArticle,
    service: ArticleService = Depends(),
):
    return service.create(article_data)


@router.put('/{article_id}')
def update_operation(
        article_id: int,
        article_data: UpdateArticle,
        service: ArticleService = Depends()):
    service.update(
        article_id=article_id,
        article_data=article_data,
    )
    return Response(status_code=status.HTTP_200_OK)


@router.delete('/delete/{id}')
def delete_article(id: int, service: ArticleService = Depends(),):
    return service.delete(id)
