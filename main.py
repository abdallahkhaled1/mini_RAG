from fastapi import FastAPI
from routes import base
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(base.base_router)




  