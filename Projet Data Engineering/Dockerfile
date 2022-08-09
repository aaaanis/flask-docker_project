# Import base image with python and pip installed
FROM python:3.7-slim-buster

# Set working directory
WORKDIR /usr/data

# Copy code from host machine
COPY . .

# Install project dependencies
RUN pip install -r requirements.txt

# Expose our application port
EXPOSE 3000

# Precise command to launch when the image will be ran
RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]