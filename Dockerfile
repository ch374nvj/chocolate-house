FROM python:3.10

# Create app directory
WORKDIR /app

# Install app dependencies
COPY src/requirements.txt ./

RUN pip install -r requirements.txt

COPY src /app

CMD ["python", "app.py"]
