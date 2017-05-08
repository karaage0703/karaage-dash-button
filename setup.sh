#!/bin/bash -e

pip_install(){
	# for dasher
	sudo pip install bottle
}

dasher_install(){
	# for dasher
	sudo apt-get install -y libpcap-dev
	sudo apt-get install -y npm
	sudo apt-get install -y node
	wget http://node-arm.herokuapp.com/node_latest_armhf.deb 
	sudo dpkg -i node_latest_armhf.deb
	git clone https://github.com/maddox/dasher.git
	cd dasher
	sudo npm install
}

START_TIME=`date +%s`

# change directory here
cd `dirname $0`

pip_install
dasher_install

END_TIME=`date +%s`

SS=`expr ${END_TIME} - ${START_TIME}`
HH=`expr ${SS} / 3600`
SS=`expr ${SS} % 3600`
MM=`expr ${SS} / 60`
SS=`expr ${SS} % 60`

echo "Total Time: ${HH}:${MM}:${SS} (h:m:s)"

echo "Please reboot"
