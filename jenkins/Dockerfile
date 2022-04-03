# FROM jenkins/jenkins:2.332.1-jdk11
FROM jenkins/jenkins:2.341-jdk11
USER root

RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli
# COPY /home/haidi/jenkins_compose/jenkins_configuration:/var/jenkins_home
# COPY /var/run/docker.sock:/var/run/docker.sock
# COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy

USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean:1.25.3 docker-workflow:1.28" 