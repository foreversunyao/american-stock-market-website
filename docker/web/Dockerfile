FROM ubuntu:16.04

RUN apt-get update -y

RUN apt-get install -y python python-pip python-dev build-essential libmysqlclient-dev


# Add requirements.txt
ADD requirements.txt .
 
# Install app requirements
RUN pip install -r requirements.txt
 
# Create app directory
COPY webapp /webapp
COPY crawler /crawler 
 
# Set the default directory for our environment
ENV HOME /webapp
WORKDIR /webapp
 
# Expose port 8000 for uwsgi
EXPOSE 8888
 
ENTRYPOINT ["python"]
CMD ["controller.py"]
