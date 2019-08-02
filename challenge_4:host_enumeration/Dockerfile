FROM jpetazzo/dind

ENV LC_ALL=C.UTF-8 
ENV LANG=C.UTF-8


RUN mkdir /app
ENV DATADIR /app

RUN  apt-get update -qq && apt-get install -qqy \
    software-properties-common \  
    build-essential \ 
    git


RUN apt-get update -qq && \
    add-apt-repository ppa:jonathonf/python-3.6 && \
    python3.6 \
    python3-pip 

RUN cd $DATADIR
RUN git clone https://github.com/Sandarmann/dr_robot.git

RUN pip3 install pipenv simple_http_server
RUN pip3 install simple_http_server

CMD /bin/bash

RUN cd dr_robot  && \
    pipenv --python /usr/bin/python3 && \
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
