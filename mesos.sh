wget http://apache.mesi.com.ar/mesos/0.21.2/mesos-0.21.2.tar.gz
sudo apt-get update
sudo apt-get install -y tar wget git
sudo apt-get install -y openjdk-7-jdk
sudo apt-get install -y autoconf libtool
sudo apt-get -y install build-essential python-dev python-boto libcurl4-nss-dev libsasl2-dev libsasl2-modules maven libapr1-dev libsvn-dev

gunzip mesos-0.21.2.tar.gz
tar -xvf mesos-0.21.2.tar

cd mesos-0.21.2
./bootstrap
mkdir build
cd build
../configure
make

