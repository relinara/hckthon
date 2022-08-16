from fastapi import FastAPI

tags_metadata = [{
    "name" : "Automate ticketing service",
    "description" : "Харилцагч app др хүсэлт гаргахад автоматаар тикет үүсч Гомдол бүртгэх сервис"
}]
app = FastAPI(title = "KB Hackathon", description = "For KB Hackathon", version = "0.1.0", openapi_tags = tags_metadata)
from api.core.routes import default_route
app.include_router(default_route)