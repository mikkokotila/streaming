sudo apt-get update -y
sudo apt install python -y 
sudo apt install python-pip -y
sudo apt install unzip -y
sudo pip install tweepy

wget https://github.com/mikkokotila/streaming/archive/master.zip
unzip master.zip

mv ~/streaming-master/setup.sh .
mv ~/streaming-master/twitter2stream.py .

chmod +x setup.sh twitter2stream.py

sudo mv ~/streaming-master/twitter2stream.conf /etc/init/sosi.conf
sudo service sosi start
