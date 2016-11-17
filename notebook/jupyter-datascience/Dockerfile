FROM jupyter/datascience-notebook
# https://github.com/jupyter/docker-stacks/blob/master/datascience-notebook/Dockerfile

MAINTAINER Jeremy Douglass <jeremydouglass@gmail.com>

# zip -- for dfr-browser export
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    zip && \
    rm -rf /var/lib/apt/lists/*	

# Java JDK and rJava (conda) -- for mallet
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
	mkdir -p /usr/class/ && \
    cp -R mallet-2.0.8RC3/class/cc /usr/class/cc && \
    chown -R $NB_USER:users /usr/class/cc/ && \
    mkdir -p /usr/lib && \
    cp mallet-2.0.8RC3/lib/mallet-deps.jar /usr/lib/mallet-deps.jar && \
    chown -R $NB_USER:users /usr/lib/mallet-deps.jar
    # rm mallet-2.0.8RC3.zip && \
    # rm -r mallet-2.0.8RC3

# dfrtopics R dependencies
USER $NB_USER
RUN conda install --quiet --yes 'r-lubridate' && \
    conda install --quiet --yes -c bioconda 'r-readr'
RUN Rscript -e 'install.packages("mallet", repos="http://cran.rstudio.com/")'
RUN Rscript -e 'devtools::install_github("agoldst/dfrtopics", quiet = TRUE)'
