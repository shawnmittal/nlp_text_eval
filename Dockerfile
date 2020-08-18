FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV LISTEN_PORT=5000
EXPOSE 5000

ENV UWSGI_INI uwsgi.UWSGI_INI
WORKDIR /webapp

COPY . /webapp

COPY requirements.txt / 
RUN pip install --no-cache-dir -U pip
RUN pip install --no-cache-dir -r /requirements.txt
