FROM python:3.10.11
RUN pip install --upgrade pip
COPY requirements.txt /code/requirements.txt
#ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code
#CMD python manage.py runserver 0.0.0.0:18001
CMD python app.py