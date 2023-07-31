FROM python:3.11
#WORKDIR /tmp
#RUN pip freeze > requirements.txt
#COPY requirements.txt /tmp/requirements.txt
#RUN python3 -m pip install -r /tmp/requirements.txt

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app