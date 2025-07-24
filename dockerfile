FROM  httpd:latest
RUN apt-get update 
RUN apt-get install -y iputils-ping
# RUN apt-get install inetutils-tracer-route
#RUN apt-get install -y ip route2
#RUN apt-get install -y curl telnet dnsutils


WORKDIR /var/www/html/onsite3
