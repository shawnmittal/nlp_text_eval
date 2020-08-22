FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN apt remove -y --purge imagemagick \
    imagemagick-6-common \
    magemagick-6.q16 \
    libmagickcore-6-arch-config \
    libmagickcore-6-headers \
    libmagickcore-6.q16-6 \
    libmagickcore-6.q16-6-extra \
    libmagickcore-6.q16-dev \
    libmagickcore-dev \
    libmagickwand-6-headers \
    libmagickwand-6.q16-6 \
    libmagickwand-6.q16-dev \
    libmagickwand-dev

RUN apt-get update && apt-get install -y \
    libperl5.28 \
    libpython3.7-minimal \
    libpython3.7-stdlib \
    linux-libc-dev \
    perl \
    perl-base \
    perl-modules-5.28 \
    python3.7 \
    python3.7-minimal \
&& rm -rf /var/lib/apt/lists/*


ENV LISTEN_PORT=5000
EXPOSE 5000

ENV UWSGI_INI uwsgi.ini

WORKDIR /webapp

COPY . /webapp

COPY requirements.txt / 
RUN pip install --upgrade pip
RUN mv ./webapp/nltk_data /usr/local/share/nltk_data
RUN pip3 install --no-cache-dir -r /requirements.txt