FROM centos:7

RUN \
        cd /etc/yum.repos.d/ && \
        sed -i  -e 's!#baseurl=http://mirror.centos.org/!baseurl=http://mirror.fsmg.org.nz/!g' *
RUN \
        yum -y --disableplugin=fastestmirror install rpm-build rpm*
RUN \
        rpmdev-setuptree
