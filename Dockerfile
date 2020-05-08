FROM python:3
RUN pip install flask

WORKDIR /app

COPY code/main.py /app/

CMD ["python", "main.py"]
