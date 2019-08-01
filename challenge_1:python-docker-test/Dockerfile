FROM alpine:3.10.1

RUN apk add --no-cache libressl-dev musl-dev libffi-dev gcc g++ make libpcap-dev bash git
RUN apk add --no-cache python3

COPY requirements.txt /app/hello_world/requirements.txt
RUN pip3 install -r /app/hello_world/requirements.txt

WORKDIR /app/hello_world

COPY hello_world.py /app/hello_world
CMD ["python3","-u","./hello_world.py"]
