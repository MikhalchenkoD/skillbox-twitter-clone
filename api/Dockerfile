FROM python:3.11

WORKDIR /app

COPY api/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY api /app

VOLUME /app/uploadfile

CMD ["uvicorn", "routes:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
