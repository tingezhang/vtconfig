sudo apt-get install libevent-dev
sudo apt-get install libncurses5-dev
wget https://github.com/tmux/tmux/releases/download/2.3/tmux-2.3.tar.gz
tar -zxf tmux-2.3.tar.gz
cd tmux-2.3/
mkdir -p ~/usr
./configure --prefix=/home/tinge/usr
make
make install
