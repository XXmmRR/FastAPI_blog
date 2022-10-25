from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = 'sqlite:///./database.sqlite'

    jwt_secret: str = 'vqza8mHH1T035seDS4W6MzTEeR93iVGv-BdK-5wUEzA'
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600


settings = Settings()

