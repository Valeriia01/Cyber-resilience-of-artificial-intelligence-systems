"""FAST-API application for counting and displaying website visits"""
import logging
import os 
from fastapi import FastAPI, status
import redis
import uvicorn
from dotenv import dotenv_values

logger = logging.getLogger('informing')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('site_informing.log')
fh.setLevel(logging.INFO)
FORMATSTR = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(FORMATSTR)
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.info('RESTARTED')

config = {
    **dotenv_values(".env"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}
conn = redis.from_url(f'redis://{config["host_redis"]}:{config["port_redis"]}')

app = FastAPI()


@app.get('/show/{web_host}')
def show(web_host):
    """function to display the number of visits""" 
    logger.info('Displaying info about %s', web_host) 
    return {conn.get(web_host)}


@app.get('/visit/{web_host}')
def visit(web_host):
    """increment function hkjsfadhjsdhjsdhj"""
    conn.incr(web_host)
    logger.info('Visiting %s', web_host)
    return status.HTTP_200_OK


if __name__ == "__main__":
    uvicorn.run(app,host = config["host_app"], port = int(config['site_port']),
                log_level = config['log_level'])
