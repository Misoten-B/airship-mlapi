FROM nvidia/cuda:12.0.0-base-ubuntu22.04
SHELL ["/bin/bash", "-c"]

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN <<EOF
apt update
apt -y install software-properties-common
add-apt-repository ppa:deadsnakes/ppa
apt update
apt -y install python3.11 python3.11-dev python3-pip ffmpeg cmake clang g++-12
apt clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EOF

ENV PYSETUP_PATH="/opt/pysetup" \
    USERNAME=docker \
    GROUPNAME=user \
    UID=1000 \
    GID=1000

RUN <<EOF
groupadd -g $GID $GROUPNAME
useradd -m -s /bin/bash -u $UID -g $GID $USERNAME
EOF

WORKDIR /home/$USERNAME/vall_e_x_api
RUN python3.11 -m pip install --upgrade setuptools pip
COPY ./app/requirements.txt ./app/pyproject.toml /home/$USERNAME/

USER $USERNAME

RUN python3.11 -m pip install --no-cache-dir -r /home/${USERNAME}/requirements.txt 
ENV PATH=/hone/docker/.local/bin:$PATH

EXPOSE 8000

CMD [ "python3.11", "main.py" ]
