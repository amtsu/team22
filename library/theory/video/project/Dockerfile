FROM python:3.10.11
RUN pip install --upgrade pip
COPY requirements.txt /code/requirements.txt
#ADD . /code
WORKDIR /code
RUN apt-get update
RUN apt-get install -y libgl1
RUN pip install -r requirements.txt
##RUN pip uninstall opencv-python -y
#RUN apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
#RUN apt-get install gstreamer1.0-tools
ADD . /code
#CMD python manage.py runserver 0.0.0.0:18001
CMD python app.py