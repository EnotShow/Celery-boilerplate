# Use an official Python runtime as a base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the Django project into the container
COPY . /app/

# Run the Django development server (adjust CMD as needed for production)
CMD python manage.py runserver 0.0.0.0:8000
