FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN  python3 -m  pip  install --upgrade pip

RUN  python3 -m  pip  install  --no-cache-dir -r requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

COPY app app

EXPOSE 5000

CMD [ "python3", "app/routes.py"]
