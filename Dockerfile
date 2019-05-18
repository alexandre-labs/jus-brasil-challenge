FROM python:3.7.3
ADD . /project
WORKDIR /project
RUN make install
