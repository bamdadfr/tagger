FROM python:3.7-slim-stretch

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir typing_extensions

COPY src ./src

RUN pip install --no-cache-dir -e src

CMD ["tag"]
