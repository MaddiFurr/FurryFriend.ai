FROM python:3.12

LABEL maintainer='her@maddi.wtf'

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "./__main__.py"]
