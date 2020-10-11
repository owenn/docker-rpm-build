FROM rpm-builder:latest

RUN \
        yum -y --disableplugin=fastestmirror install make curl

RUN mkdir /data
RUN chmod 777 /data
USER 1001
WORKDIR /data


CMD make
