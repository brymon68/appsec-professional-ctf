FROM python:3-alpine

ENV http_proxy="http://wwwproxy.sandia.gov:80/" \
    https_proxy="http://wwwproxy.sandia.gov:80/" \
    no_proxy="localhost,localnets,sandia.gov,127.0.0.1" \
    HTTP_PROXY="http://wwwproxy.sandia.gov:80/" \
    HTTPS_PROXY="http://wwwproxy.sandia.gov:80/" \
    NO_PROXY="localhost,localnets,sandia.gov,127.0.0.1"

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
