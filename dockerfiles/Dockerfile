FROM osgeo/gdal:ubuntu-full-3.4.0

RUN apt-get update -y                                         \
    && apt-get upgrade -y                                         \
    && apt-get install -y build-essential python3-pip htop screen git wget

# install aws cli
# RUN pip3 --no-cache-dir install --upgrade awscli

# Download Miniconda
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

# install in batch (silent) mode, does not edit PATH or .bashrc or .bash_profile
# -p path
# -f force
RUN bash Miniconda3-latest-Linux-x86_64.sh -b

ENV PATH=/root/miniconda3/bin:${PATH}

#RUN source /root/.bashrc
#RUN source /root/.bash_profile

RUN conda update conda \
    && conda clean --all --yes

# Cleanup
RUN rm Miniconda3-latest-Linux-x86_64.sh

# -----------------------------------------------------------------------------

WORKDIR /media/validere

# Copy conda env
COPY env_validere.yml .

# Create environment
RUN conda env create --file env_validere.yml