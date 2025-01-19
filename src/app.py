from fastapi import FastAPI
from api.v1.routers.user_controller import router as user_router

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))


app = FastAPI()
app.include_router(user_router)