FROM python:3-alpine

RUN apk add --no-cache libressl-dev 

RUN mkdir /app
ENV DATADIR /app
COPY src/index.html ${DATADIR}

ENV PORT 8080
EXPOSE ${PORT}
WORKDIR ${DATADIR}

RUN pip install simple_http_server

CMD python -m http.server ${PORT}
#CMD python3 -m SimpleHTTPServer ${PORT}
