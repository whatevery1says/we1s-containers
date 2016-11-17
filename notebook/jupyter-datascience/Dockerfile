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
RUN conda install --quiet --yes 'r-lubridate' && \
    conda install --quiet --yes -c bioconda 'r-readr'

# R dfrtopics (and R mallet wrapper)
USER $NB_USER
RUN Rscript -e 'install.packages("mallet", repos="http://cran.rstudio.com/")'
RUN Rscript -e 'devtools::install_github("agoldst/dfrtopics", quiet = TRUE)'


