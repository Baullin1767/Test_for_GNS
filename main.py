from fastapi import FastAPI, Form, status
from fastapi.responses import FileResponse, JSONResponse
import requests
 
app = FastAPI()
 
@app.get("/")
def root():
    return FileResponse("public/index.html")

users={}
 
# метод post для клиента
@app.post("/postdata")
def postdata(username = Form(), userphone=Form()):
    # Проверяем, есть ли пользователь в списке
    if not user_exist(username):
        users.update({username: userphone})  # Если нет добавляем пользователя в список
        # И отправляем post запрос на сервис
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
        return {username: userphone}
    else:
        # Если пользователь найден отправляем статус код и сообщение
        return JSONResponse(
                status_code=status.HTTP_208_ALREADY_REPORTED, 
                content="Пользователь уже существует"
        )

# Проверяет существует ли пользователь
def user_exist(username):
    if username in users:
        return True
    else:
        return False
