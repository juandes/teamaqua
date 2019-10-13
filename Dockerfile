
FROM golang:1.12

WORKDIR /go/src/github.com/juandes/teamaqua
COPY . .

RUN echo $GOPATH
RUN make test
RUN make go-build

RUN apt-get update
RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-recommends python3.6  python3-pip python3-setuptools screen

RUN pip3 install -r water_retriever/requirements.txt

CMD [ "./run.sh"]
