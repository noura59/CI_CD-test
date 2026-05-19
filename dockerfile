FROM python:3.11-slim

WORKDIR /CI_CD

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "etl.py"]