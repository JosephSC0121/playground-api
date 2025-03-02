FROM python:3.10.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/app

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "80", "--reload"]
