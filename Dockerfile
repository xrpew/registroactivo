FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt
COPY . . 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]