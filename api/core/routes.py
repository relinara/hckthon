from fastapi import APIRouter
from api.core.models import BaseResponse, ErrorResponse
import requests, json
from api.core.config import cnf

default_responses = {
    200: {"model": BaseResponse, "description": "Хүсэлт амжилттай"},
    404: {"model": ErrorResponse, "description": "aldaa"},
    500: {"model": ErrorResponse, "description": "Серверт алдаа гарлаа"}
}

default_route = APIRouter(prefix="/api/v1/accountStatement", tags = ["AccountStatement"])

@default_route.get("/test", response_model = BaseResponse, responses = default_responses, tags = ["AccountStatement"], summary = "Get Root")
def getRoot(userId: int):
    # accountbalance = requests.get(cnf.KB_URL, data = {"user_id": userId})
    # resp = accountbalance.json
    _file = open(cnf.EP_FILE)
    data = json.load(_file)
    retData = ""
    isFound = False
    for item in data:
        if int(item['userId']) == int(userId):
            retData = item
            isFound = True
    if isFound:
        return BaseResponse(success = True, msg = str(retData)) 
    else:
        return BaseResponse(success = False, msg = "Өгөгдөл олдсонгүй")