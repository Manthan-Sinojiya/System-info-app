# Stage 1: build / install dependencies
FROM python:3.11-slim AS build

WORKDIR /app

# Install pip-tools / build-time deps if you need them (none here)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: runtime
FROM python:3.11-slim

WORKDIR /app

# Copy only what's needed
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .

ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

CMD ["python", "app.py"]
