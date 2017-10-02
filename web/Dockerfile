FROM python:3.6
ADD . /code
WORKDIR /code
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade -r web/requirements.txt
EXPOSE 5000
ENV WEB_SETTINGS="settings.cfg"
CMD ["python", "-u", "web/server.py"]