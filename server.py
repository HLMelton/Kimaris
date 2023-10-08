from fastapi import FastAPI, Request, HTTPException, Response

import logging
import time
import uvicorn

from modules.args import get_args
from modules.constants import HttpResponse, http_code_to_enum
import modules.sqlite_helpers as sqlite_helpers

kimaris = FastAPI()
args = get_args()

DATABASE_FILE = args.database.file_path
sqlite_helpers.maybe_create_table(DATABASE_FILE)

@kimaris.post("/createCard/UID") #This Method will only be accessible on web client
async def addCard(UID: str):
    # Add user creation logic here
    return {"message":"Card has been added"}

@kimaris.post("/verifyCard/{UID}") #Primary request type used in the hardware. 
async def verifyCard(UID: str):
    # Add user verification logic here
    return {"message": "User is authorized"}

@kimaris.post("/removeCard/{UID}") #This Method will only be available on the web client
async def removeCard(UID: str):
    # Add user remove logic here
    return {"message": "User removed"}




if __name__ == "__main__":
    logging.info(f"running on {args.host}, listening on port {args.port}")
    uvicorn.run("server:app", host=args.host, port=args.port, reload=True)