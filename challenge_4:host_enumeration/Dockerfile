FROM jpetazzo/dind


RUN mkdir /app
ENV DATADIR /app

RUN apt-get update -qq && apt-get install -qqy \
    git \ 
    python3 \
    python3-pip

RUN cd $DATADIR
RUN git clone git@github.com:Sandarmann/dr_robot.git

RUN pip install pipenv simple_http_server
RUN pip install simple_http_server

RUN cd dr_robot && \
    pipenv sync && \
    pipenv shell && \
    pipenv run python drrobot.py gather overstock.com -sub
#

# RUN mkdir /app
# ENV DATADIR /app
# COPY src/index.html ${DATADIR}

# ENV PORT 8080
# EXPOSE ${PORT}
# WORKDIR ${DATADIR}



# CMD python -m http.server ${PORT}
