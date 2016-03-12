#!/bin/sh
#ubunto 14.04 on ec2 mesos and spark install script

wget http://archive.apache.org/dist/mesos/0.21.0/mesos-0.21.0.tar.gz
tar -zxf mesos-0.21.0.tar.gz

sudo apt-get update
sudo apt-get install -y tar wget git

# Update the packages.
sudo apt-get update

# Install a few utility tools.
sudo apt-get install -y tar wget git

# Install the latest OpenJDK.
sudo apt-get install -y openjdk-7-jdk

# Install autotools (Only necessary if building from git repository).
sudo apt-get install -y autoconf libtool

# Install other Mesos dependencies.
sudo apt-get -y install build-essential python-dev python-boto libcurl4-nss-dev libsasl2-dev libsasl2-modules maven libapr1-dev libsvn-dev

#####installing mesos

 # Change working directory.
cd mesos-0.21.0

# Bootstrap (***Skip this if you are not building from git repo***).
./bootstrap

# Configure and build.
mkdir build
cd build
../configure
make

# Run test suite.
make check

# Install (***Optional***).
 make install
