# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5001 to the outside world
EXPOSE 5001

# Define environment variable to avoid Python buffering
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "app.py"]
