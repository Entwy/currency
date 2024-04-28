from requests import get, post
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('ENDPOINT')

result = get(key)

print(result.json())
headers = {"Content-Type": "application/json"}

message = input("Введите сообщение ")
res_post = post(key, json={"test": {"time": "18:32", "message": f'{message}'}},headers=headers)
print(res_post.json())