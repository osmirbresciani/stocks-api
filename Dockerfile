FROM python:3-onbuild

RUN mkdir -p /opt/services/flaskapp/src
COPY requirements.txt /opt/services/flaskapp/src/
WORKDIR /opt/services/flaskapp/src
RUN pip install -r requirements.txt
COPY . /opt/services/flaskapp/src
EXPOSE 5000
EXPOSE 5432
CMD ["flask", "run", "--host", "0.0.0.0"]
CMD ["python3", "app.py"]







