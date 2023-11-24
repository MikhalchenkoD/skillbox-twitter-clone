FROM python:3.11

WORKDIR /api

COPY . .

RUN pip install --no-cache-dir -r api/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api.routes:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
