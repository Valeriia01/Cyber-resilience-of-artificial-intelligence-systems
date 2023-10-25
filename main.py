"""FAST-API application for counting and displaying website visits"""
from fastapi import FastAPI, status
import redis
import uvicorn
from dotenv import dotenv_values


config = {
    **dotenv_values(".env"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}
#conn = redis.Redis(host = config["host_redis"], port = config["port_redis"], decode_responses = True)
conn = redis.from_url(f'redis://{config["host_redis"]}:{config["port_redis"]}')

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
    uvicorn.run(app,host = config["host_app"], port = config['site_port'],
                log_level = config['log_level'])
