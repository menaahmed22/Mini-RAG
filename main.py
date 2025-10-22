from fastapi import FastAPI
from dotenv import load_dotenv
import os
from routes import base , data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
# from helpers.config import get_settings , Settings

# from google.colab import userdata
# from pyngrok import ngrok
from pyngrok import ngrok
load_dotenv("miniRAG.env")
# NGROK_AUTH_TOKEN = userdata.get("NGROK_AUTH_TOKEN")
ngrok_key=os.getenv("ngrok_key")
ngrok.set_auth_token(ngrok_key)
# MONGO_URI = "mongodb://localhost:27017"
# MONGODB_DATABASE="minirag"
app=FastAPI()
@app.on_event("startup")
async def startup_db_client():
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_conn.close()
app.include_router(base.base_router)
app.include_router(data.data_router)

#this part because i use google colab not local machine
# import uvicorn
# import threading


# def run_app():
#     uvicorn.run(app, host="0.0.0.0", port=8000)

# thread = threading.Thread(target=run_app, daemon=True)
# thread.start()

# 4. Expose with ngrok

public_url = ngrok.connect(5000)
print("Public URL:", public_url)

#uvicorn main:app --host 0.0.0.0 --port 5000
