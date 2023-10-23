import sys
from fastapi import FastAPI, status
import redis
import uvicorn
from dotenv import dotenv_values

def print_python_version():
    print(sys.version)

config = dotenv_values(".env")
#conn = redis.Redis(host = config["host"], port = config["port"], decode_responses = True)
conn = redis.from_url(f'redis://{config["host"]}:{config["port"]}')

app = FastAPI()


@app.get('/show/{id}')
def show(id):
    return {conn.get(id)}


@app.get('/visit/{id}')
def visit(id):
    conn.incr(id)
    return status.HTTP_200_OK


if __name__ == "__main__":
    uvicorn.run(app,host = config["host"], port = config['site_port'], log_level = config['log_level'])
