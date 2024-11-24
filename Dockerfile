# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8777

# Add Scores.txt file
COPY Scores.txt /Scores.txt

# Run the Flask application
CMD ["python", "app.py"]
