sudo ufw allow 22
sudo ufw allow 12021
sudo ufw allow  80
sudo ufw allow 8080
sudo ufw show added


mkdir ~/usr
mkdir ~/work
mkdir ~/.ssh
touch ~/.ssh/authorized_keys

sudo apt-get update
sudo apt-get install libncurses5-dev libgnome2-dev libgnomeui-dev libgtk2.0-dev libatk1.0-dev libbonoboui2-dev libcairo2-dev libx11-dev libxpm-dev libxt-dev python-dev  python3-dev ruby-dev lua5.1 lua5.1-dev libperl-dev git
sudo apt-get install htop cscope ctags ipython3
