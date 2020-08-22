FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN apt remove --purge imagemagick

ENV LISTEN_PORT=5000
EXPOSE 5000
ENV UWSGI_INI uwsgi.ini

WORKDIR /webapp

COPY . /webapp

COPY requirements.txt / 
RUN pip install --upgrade pip
RUN mv ./webapp/nltk_data /usr/local/share/nltk_data
RUN pip3 install --no-cache-dir -r /requirements.txt