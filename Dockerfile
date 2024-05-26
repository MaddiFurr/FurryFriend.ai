FROM python:3.12

LABEL maintainer='her@maddi.wtf'

WORKDIR /app

# Optional: Copy a requirements.txt file if you have external dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your application code
COPY . .

# Specify the command to run your application
CMD [ "python", "__main__.py" ]  # Replace with your actual script name