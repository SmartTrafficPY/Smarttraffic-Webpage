FROM python:3.8-slim

# RUN addgroup -S app && \
#     adduser -S -G app app && \
#     mkdir -p /var/log/app && \
#     chown app: /var/log/app
RUN groupadd app && \
    useradd -ms /bin/bash -g app app && \
    mkdir -p /var/log/app && \
    chown app: /var/log/app

ADD poetry.lock pyproject.toml /home/app/

# RUN apk -U add bash build-base libffi-dev openssl-dev \
#     uwsgi-python3 && \
#     pip install poetry==1.0.5 && \
#     poetry config virtualenvs.create false && \
#     cd /home/app/ && \
#     # https://github.com/python-poetry/poetry/issues/2102
#     poetry install --no-ansi --no-interaction && \
#     apk del build-base
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq && \
    apt-get install -qq -y build-essential mime-support gettext iproute2 && \
    pip install -q --no-cache-dir -U pip && \
    pip install -q --no-cache-dir uwsgi && \
    pip install -q --no-cache-dir poetry && \
    cd /home/app/ && \
    poetry config virtualenvs.create false && \
    poetry install --no-ansi --no-interaction

COPY . /home/app/code

RUN chown -R app: /home/app/
WORKDIR /home/app/code

COPY ./docker/uwsgi.ini /etc/uwsgi.ini
COPY ./docker/build-staticfiles.sh ./docker/start.sh /

RUN chmod +x /build-staticfiles.sh
RUN chmod +x /start.sh

EXPOSE 5050

ENTRYPOINT ["/start.sh"]

# CMD ["docker/run_gunicorn.sh"]
CMD ["uwsgi", "--ini", "/etc/uwsgi.ini"]
