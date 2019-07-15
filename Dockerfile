FROM python:3.6-jessie

LABEL maintainer="conda"

WORKDIR /app
COPY . /app
# Add user ubuntu with no password, add to sudo group
RUN adduser --disabled-password --gecos '' ubuntu
RUN adduser ubuntu sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ubuntu
RUN chmod a+rwx /home/ubuntu/

USER root
RUN cd /app && wget https://repo.continuum.io/archive/Anaconda3-2019.03-Linux-x86_64.sh

USER ubuntu
RUN bash /app/Anaconda3-2019.03-Linux-x86_64.sh -b
ENV PATH /home/ubuntu/anaconda3/bin:$PATH

#RUN conda update conda
#RUN conda update anaconda
#RUN conda update --all


USER root
RUN chmod 7777 /app
RUN rm /app/Anaconda3-2019.03-Linux-x86_64.sh
