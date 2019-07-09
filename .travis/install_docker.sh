#!/bin/bash
if [[ "$TRAVIS_OS_NAME" == 'linux' ]]; then 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - 
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 
sudo apt-get update 
sudo apt-get -y -o Dpkg::Options::="--force-confnew" install docker-ce docker-ce-cli containerd.io 
fi

if [[ "$TRAVIS_OS_NAME" == 'osx' ]]; then 
brew install docker docker-compose docker-machine xhyve docker-machine-driver-xhyve 
sudo chown root:wheel $(brew --prefix)/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve
sudo chmod u+s $(brew --prefix)/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve
docker-machine create default --driver xhyve --xhyve-experimental-nfs-share
eval $(docker-machine env default)
docker-machine start default
fi