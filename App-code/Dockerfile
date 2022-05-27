FROM python:3

WORKDIR /code
COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt

CMD [ "uvicorn", "app:app", "--port", "5000", "--host", "0.0.0.0"]



