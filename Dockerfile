FROM python:3

WORKDIR /home/vakr/Project/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .env ./.env
COPY . .

CMD [ "python", "./main.py" ]
