from fastapi import FastAPI
from dotenv import load_dotenv
import os
from routes import base , data
# from helpers.config import get_settings , Settings

# from google.colab import userdata
# from pyngrok import ngrok
from pyngrok import ngrok
load_dotenv("miniRAG.env")
# NGROK_AUTH_TOKEN = userdata.get("NGROK_AUTH_TOKEN")
ngrok_key=os.getenv("ngrok_key")
ngrok.set_auth_token(ngrok_key)
app=FastAPI()

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