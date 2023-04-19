# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container and install the dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY app-counter.py app.py

# Expose port 5000 for the Flask app
EXPOSE 5000

# Start the Flask app when the container starts
CMD [ "python", "app.py" ]
