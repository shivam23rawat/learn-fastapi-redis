# Use the official Python image from the Docker Hub
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY src/ /app/src

# Expose the port that the app runs on
EXPOSE 8000

# Set the maintainer label
LABEL maintainer="shivam23rawat <shivamrawat2000@gmail.com>"

# Command to run the application
CMD ["fastapi", "run", "src/app.py", "--host", "0.0.0.0", "--port", "8000"]