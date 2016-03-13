FROM ubuntu:14.04
MAINTAINER Avi Yashchin  <avi.yashchin@gmail.com>

RUN mkdir /srv/m3 && \
	cd /srv/m3

RUN git clone https://github.com/aviyashchin/liquidity.ai.git
