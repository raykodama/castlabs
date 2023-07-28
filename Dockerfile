# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files to the container's working directory
COPY jwt_utility.py .
COPY secret.txt .

# Install required dependencies
RUN pip install pyjwt

# Command to run the JWT utility script
CMD ["python", "jwt_utility.py"]

