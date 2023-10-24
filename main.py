"""FAST-API application for counting and displaying website visits"""
from fastapi import FastAPI, status
import redis
import uvicorn
from dotenv import dotenv_values


config = dotenv_values(".env")
#conn = redis.Redis(host = config["host"], port = config["port"], decode_responses = True)
conn = redis.from_url(f'redis://{config["host"]}:{config["port"]}')

app = FastAPI()


@app.get('/show/{web_host}')
def show(web_host):
    """function to display the number of visits"""
    return {conn.get(web_host)}


@app.get('/visit/{web_host}')
def visit(web_host):
    """increment function hkjsfadhjsdhjsdhj"""
    conn.incr(web_host)
    return status.HTTP_200_OK


if __name__ == "__main__":
    uvicorn.run(app,host = config["host"], port = config['site_port'],
                log_level = config['log_level'])
