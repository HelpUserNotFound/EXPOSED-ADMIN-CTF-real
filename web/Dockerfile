FROM python:3.11

WORKDIR /app

COPY app.py .

COPY static ./static

RUN pip install flask

CMD ["python", "app.py"]