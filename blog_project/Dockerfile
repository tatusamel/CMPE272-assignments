# Dockerfile
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy requiremeents.txt and install dependencies
COPY requiremeents.txt /app/
RUN pip install --no-cache-dir -r requiremeents.txt

# Copy the entire project into the container
COPY . /app/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expose port 8000 for Django
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

