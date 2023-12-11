FROM nvidia/cuda:12.0.0-base-ubuntu22.04
SHELL ["/bin/bash", "-c"]

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN apt update &&\
    apt -y install software-properties-common &&\
    add-apt-repository ppa:deadsnakes/ppa &&\
    apt update &&\
    apt -y install python3.11 python3.11-dev python3-pip ffmpeg cmake clang g++-12

RUN python3.11 -m pip install poetry

ARG USERNAME=docker
ARG GROUPNAME=user
ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME
USER $USERNAME

WORKDIR /home/$USERNAME/vall_e_x_api


EXPOSE 8000


