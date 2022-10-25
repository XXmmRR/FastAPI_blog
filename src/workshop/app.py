from fastapi import FastAPI
from workshop.api.Article_api import router
from workshop.api.auth import router as auth_router

app = FastAPI()
app.include_router(router)
app.include_router(auth_router)


@app.get('/')
def root():
    return {'message': 'hello'}
