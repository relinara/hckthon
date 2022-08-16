from typing import Optional
from pydantic import BaseSettings, Field

class GlobalConfig(BaseSettings):
    SERVER_IP: str = "127.0.0.1"
    SERVER_PORT: int = 8080
    # KB_URL: str = "https://kb.local"
    ACCSTATEMENT_URL: str = "/accState"
    ENV_STATE: Optional[str] = Field(None, env = "ENV_STATE")
    EP_FILE: str = "datas.json"

    class Config:
        env_file: str = ".env"
        env_file_encoding = "utf-8"

class DevConfig(GlobalConfig):
    class Config:
        env_prefix: str = "DEV_"
        env_file_encoding: str = "utf-8"

class ProdConfig(GlobalConfig):
    class Config:
        env_prefix: str = "PROD_"
        env_file_encoding: str = "utf-8"

class MainConfig:
    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return DevConfig()
        elif self.env_state == "prod":
            return ProdConfig()
        
cnf = MainConfig(GlobalConfig().ENV_STATE)()
print(cnf.__repr__())