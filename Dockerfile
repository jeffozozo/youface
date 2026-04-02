FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir flask tinydb timeago
EXPOSE 5005
CMD ["python", "youface.py"]
