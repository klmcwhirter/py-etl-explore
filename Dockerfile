FROM python:3

USER 1001

WORKDIR /opt/app-root/src

COPY README.md requirements.txt setup.py ./
COPY src src

RUN /bin/bash -c "python3 -m venv venv && source venv/bin/activate \
    && pip install --no-cache-dir --upgrade pip wheel \
    && pip install --no-cache-dir -r requirements.txt \
    && python3 setup.py bdist_wheel"

COPY data data

CMD [ "uwsgi", "app.ini"]