from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
import requests
 
app = FastAPI()
 
@app.get("/")
def root():
    return FileResponse("public/index.html")
 
 
@app.post("/postdata")
def postdata(username = Form(), userphone=Form()):
    requests.post('https://order.drcash.sh/v1/order', 
                  data={'title':{
                                'Content-Type': 'application/json',
                                'Authorization': 'Bearer RLPUUOQAMIKSAB2PSGUECA'
                                },
                        'body':{
                                'stream_code': 'vv4uf',
                                'client': {
                                            'phone': userphone,
                                            'name': username,
                                        }
                            }
                    }
                )
