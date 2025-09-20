#defining configuration for variables in project and defining thier types
# to validate them during coding

from pydantic_settings import BaseSettings ,SettingsConfigDict
# from dotenv import load_dotenv
# load_dotenv("miniRAG.env")
class Settings(BaseSettings):
  APP_NAME:str
  APP_VERSION : str 
  OPENAI_API_KEY : str 
  FILE_ALLOWED_TYPES: list
  FILE_MAX_SIZE : int
  FILE_DEFAULT_CHUNK_SIZE: int

  class config :
    env_file = "miniRAG.env"


def get_settings():
  return Settings()  