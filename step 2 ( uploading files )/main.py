from fastapi import FastAPI
from dotenv import load_dotenv
import os
from routes import base , data

load_dotenv("miniRAG.env")
app=FastAPI()

app.include_router(base.base_router)
app.include_router(data.data_router)

#this part because i use google colab not local machine
import uvicorn
import threading


def run_app():
    uvicorn.run(app, host="0.0.0.0", port=8000)

thread = threading.Thread(target=run_app, daemon=True)
thread.start()

# 4. Expose with ngrok
from pyngrok import ngrok

public_url = ngrok.connect(8000)
print("Public URL:", public_url)