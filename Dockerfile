FROM python:3.12

# Set the working directory to /app
WORKDIR /apps

# Copy the current directory contents into the container at /app
COPY . .

# Update apt (while building the image, not when running the container)
RUN apt update -y
RUN apt upgrade -y

# Upgrade pip (while building the image, not when running the container)
RUN pip install --no-cache-dir --upgrade pip

# Install the dependencies (while building the image, not when running the container)
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

CMD ["python", "-u", "main.py"]