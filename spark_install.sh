######installing scala
#!/bin/sh
sudo apt-add-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java7-installer

wget http://www.scala-lang.org/files/archive/scala-2.10.4.tgz
sudo mkdir /usr/local/src/scala
sudo tar xvf scala-2.10.4.tgz -C /usr/local/src/scala/

echo "export SCALA_HOME=/usr/local/src/scala/scala-2.10.4" >> ~/.bashrc
echo "export PATH=\$SCALA_HOME/bin:\$PATH" >> ~/.bashrc

sudo apt-get install git

######installing spark
wget http://apache.mirrors.lucidnetworks.net/spark/spark-1.6.1/spark-1.6.1.tgz
tar xvf spark-1.6.1.tgz

cd spark-1.6.1
sbt/sbt assembly

