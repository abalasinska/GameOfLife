from pydantic import BaseSettings

class Settings(BaseSettings):
    height: int = 10
    width: int = 10

    class Config:
        env_file = ".env"
        env_file_coding = "utf-8"
        
