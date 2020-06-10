FROM python:3

USER 1001

WORKDIR /opt/src/app

COPY requirements.txt ./

RUN /bin/bash -c "python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt"

COPY data data
COPY src src

CMD [ "/bin/bash", "-c", "./src/app.sh"]