#!/bin/bash -e
file=node_latest_armhf.deb
dir=dasher

pip_install(){
	# for dasher
	sudo pip install bottle
	# for twitter
	sudo pip install twython
	sudo pip install requests_oauthlib
	# for slack
	sudo pip install slackweb
}

dasher_install(){
	# for dasher
	sudo apt-get install -y libpcap-dev
	sudo apt-get install -y npm
	sudo apt-get install -y node
	if [ -e $file ]; then
		echo "$file found."
	else
		wget http://node-arm.herokuapp.com/node_latest_armhf.deb 
		sudo dpkg -i node_latest_armhf.deb
	fi

	if [ -e $dir ]; then
		echo "$dir found."
	else
		git clone https://github.com/maddox/dasher.git
	fi
	cd dasher
	sudo npm install
}

START_TIME=`date +%s`

# change directory here
cd `dirname $0`

sudo apt-get update
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
