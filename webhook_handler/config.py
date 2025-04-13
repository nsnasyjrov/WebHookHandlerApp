from flask.cli import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Setting(BaseSettings):
    SECRET_KEY: str
    USER: str
    PASSWORD: str
    HOST_NAME: str
    PORT: int
    DB_NAME: str

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"
        case_sensitive = True

    @property
    def database_uri(self):
        return f"postgresql+psycopg2://{self.USER}:{self.PASSWORD}@{self.HOST_NAME}:{self.PORT}/{self.DB_NAME}"

settings = Setting()