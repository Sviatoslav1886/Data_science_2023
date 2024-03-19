FROM python:3.9

WORKDIR /app  # Set working directory

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY api_yolo.py api_yolo.py
EXPOSE 8000

CMD ["uvicorn", "api_yolo:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]