FROM python:3.7.0-alpine3.7

RUN pip3 install requests

WORKDIR /hugo
COPY hugo.py .

ENTRYPOINT ["python3", "hugo.py"]
