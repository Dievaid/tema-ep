FROM python:3.11

RUN apt update
RUN apt upgrade -y
RUN apt install systemctl mininet -y

RUN pip install requests
RUN pip install argparse
RUN pip install mininet

COPY . /ep
WORKDIR /ep

CMD ["systemctl", "start", "ovs-vswitchd.service"]