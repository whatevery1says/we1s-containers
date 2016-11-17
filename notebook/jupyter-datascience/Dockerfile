FROM jupyter/scipy-notebook
# https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook/Dockerfile
# jupyter/scipy-notebook is copyright (c) Jupyter Development Team, and distributed under the terms of the Modified BSD License.

MAINTAINER Jeremy Douglass <jeremydouglass@gmail.com>

# R pre-requisites: https://github.com/jupyter/docker-stacks/blob/master/r-notebook/Dockerfile
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    gfortran \
    zip \
    gcc && apt-get clean && \
    rm -rf /var/lib/apt/lists/*	

# R packages: : https://github.com/jupyter/docker-stacks/blob/master/r-notebook/Dockerfile
USER $NB_USER
RUN conda config --add channels r && \
    conda install --quiet --yes \
    'r-base=3.2*' \
    'r-irkernel=0.5*' \
    'r-plyr=1.8*' \
    'r-devtools=1.9*' \
    'r-dplyr=0.4*' \
    'r-ggplot2=1.0*' \
    'r-tidyr=0.3*' \
    'r-shiny=0.12*' \
    'r-rmarkdown=0.8*' \
    'r-forecast=5.8*' \
    'r-stringr=0.6*' \
    'r-rsqlite=1.0*' \
    'r-reshape2=1.4*' \
    'r-nycflights13=0.1*' \
    'r-caret=6.0*' \
    'r-rcurl=1.95*' \
    'r-randomforest=4.6*' && conda clean -tipsy

# Warning:
# Removing r-dichromat-2.0_0-r3.2.2_2a.tar.bz2
# conda-build is not installed; could not clean source cache

# Java JDK and rJava (conda)
USER $NB_USER
RUN conda install --quiet --yes \
    -c bioconda 'java-jdk'
RUN conda install --quiet --yes \
    -c edurand 'r-rjava'

# Mallet
USER root
RUN wget http://mallet.cs.umass.edu/dist/mallet-2.0.8RC3.zip && \
    unzip mallet-2.0.8RC3.zip && \
    cp mallet-2.0.8RC3/bin/* /usr/bin/ && \
    rm mallet-2.0.8RC3.zip && \
    rm -r mallet-2.0.8RC3

# dfrtopics dependencies
USER $NB_USER
RUN conda install --quiet --yes \
    'r-lubridate' \
RUN conda install --quiet --yes \
    -c bioconda 'r-readr'

# R dfrtopics (and R mallet wrapper)
USER $NB_USER
RUN Rscript -e 'install.packages("mallet", repos="http://cran.rstudio.com/")' && \
    Rscript -e 'devtools::install_github("agoldst/dfrtopics", quiet = TRUE)'

## ERROR: installing package DESCRIPTION failed for package ‘Matrix’
## * removing ‘/opt/conda/lib/R/library/Matrix’
## * restoring previous ‘/opt/conda/lib/R/library/Matrix’


# RUN conda install conda-build && \ conda skeleton cran mallet && \
#    conda build r-mallet/ && \
#    conda install r-mallet --use-local

# RUN Rscript -e 'install.packages("bigtabulate", repos="http://cran.rstudio.com/")' && \

## dfrtopics Dependencies:
## -  jdk
##    -  mallet
##    -  rJava
##       -   mallet (r wrapper)
## -  r-devtools, r-dplyr, r-ggplot2, r-lubridate, r-stringr, r-readr
##    -   dfrtopics

# Set default python to python2
## 1.
# ENV PATH /opt/conda/envs/python2/bin:$PATH
## $ source activate python2
##    prepending /opt/conda/envs/python2/bin to PATH
##    (python2) jovyan@4443cb5c4743:~/work$ echo $PATH
##    /opt/conda/envs/python2/bin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr
##
## ... this did not work as expected -- e.g. python2 was the default in the Jupyter notebooks, but the R and Python3 entries disappeared!
## 2.
# CMD ["source activate python2 && start-notebook.sh"]
## .. this also did not work as expected, it gets passed to tini and tini fails -- can't parse two commands
##    [FATAL tini (5)] Executing child process 'source activate python2 && start-notebook.sh' failed: 'No such file or directory'
## 3.
# RUN source activate python2
## Fails during build:
##    /bin/sh: 1: source: not found
##    The command '/bin/sh -c source activate python2' returned a non-zero code: 127

# USER root
# RUN sed '2a\ source activate python2' /usr/local/bin/start-notebook.sh > /usr/local/bin/start-notebook.sh
# USER $NB_USER
## also fail inserting a line into start-notebook.sh container quits immediately

# #!/bin/sh
# source activate python2
