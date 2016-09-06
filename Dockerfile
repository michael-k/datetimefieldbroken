FROM python:3.5

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 0
ENV DJANGO_SETTINGS_MODULE datetimefieldbroken.settings

EXPOSE 8023

WORKDIR /opt/code

COPY requirements.txt /opt/code/requirements.txt
RUN pip3 install -Ur requirements.txt
COPY . /opt/code

WORKDIR /opt/code/datetimefieldbroken

ENTRYPOINT ["./manage.py"]
CMD ["runserver 0.0.0.0:8023"]
