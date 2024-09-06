#FROM ubuntu/python
#FROM ubuntu/python:3.10-22.04_stable
#FROM python
#FROM ubuntu:latest

#FROM linuxserver/chromium:latest
FROM joyzoursky/python-chromedriver:3.8


RUN apt-get update && apt-get install -y python3
RUN apt-get install -y python3-pip
#RUN apt-get install -y chromium-chromedriver
#RUN apt-get install snapd
#RUN apt-get install  chromium
#RUN apt-get install -y chromium-browser
#RUN chromedriver --version   
#RUN apt-get install chromium
#docker run -it ubuntu
#FROM ubuntu
RUN mkdir /data
#VOLUME /data
COPY requirements.txt /code/requirements.txt
#RUN pip3 install -r /code/requirements.txt
RUN pip3 install  -r /code/requirements.txt
#RUN pip3 install  --break-system-packages -r /code/requirements.txt
COPY mftickets_technolab_com_ru.py /code/mftickets_technolab_com_ru.py
#RUN python3 -m pip install -r /code/requirements.txt
##CMD ["python", "/code/mftickets_technolab_com_ru.py"]
#CMD ["bash"]
