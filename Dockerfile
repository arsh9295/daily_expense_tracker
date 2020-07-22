FROM centos
ADD . /
RUN yum install -y python3 \
    && yum install -y python3-pip \
    && pip3 install django \
    && yum install -y mysql-devel \
    && yum install -y epel-release \
    && yum install -y python3-devel \
    && yum install -y gcc \
    && pip3 install mysqlclient \
    && pip3 install pyttsx3 \
    && pip3 install sqlparser
CMD python3 manage.py runserver
EXPOSE 8000

