FROM python:3.11
ENV PYTHONUNBUFFERED 1
EXPOSE 5000
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]