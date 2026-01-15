FROM python:3.10-slim-buster

#Define working directory name
WORKDIR /app

#copy your requirmensst.txt having list of dependecies
COPY requirements.txt requirements.txt

#run the requirements.txt
RUN pip install -r requirements.txt

#copy all contents from source to destination
COPY . .

#change qwork directory to blueprintapp (for alldb pkg runs - optional)
#WORKDIR /py-flask-app/blueprintapp
#RUN flask db init
#RUN flask db migrate
#RUN flask db upgrade

WORKDIR /app

# the the final startup file app.py with python
CMD ["python" , "app.py"]

# INSTALL DOCKER  DESKTOP
# RUN 2 COMMANDS     IN TERMINAL

# create image first
#docker build -t flask-app-img .
#deploy the image as container
#docker run -p 5000:5000 flask-app-img


