from fastapi import FastAPI
from api.Article_api import router
from api.auth import router as auth_router

app = FastAPI()
app.include_router(router)
app.include_router(auth_router)


@app.get('/')
def root():
    return {'message': 'hello'}
