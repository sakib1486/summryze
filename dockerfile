# using an offical Python runtime
FROM python:3.12.5-slim

# setting the working directory in the container
WORKDIR /app

# copying current directory contents into the container at /app
COPY . /app

# intall any required packages
RUN pip install --no-cache-dir -r requirements.txt

# expose the port 5000 of the container
EXPOSE 5000

# define env variable for Flask
ENV FLASK_APP=app.py

# run flask app when container launches
CMD ["flask", "run", "--host=0.0.0.0"]