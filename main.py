import uvicorn
from api import app
from api.core.config import cnf

if "__main__" in __name__:
    print("Starting")
    uvicorn.run("api:app", host = cnf.SERVER_IP, port = cnf.SERVER_PORT, reload = True)