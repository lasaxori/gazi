cd $HOME
pkg install python2 -y&&pkg install git -y&&pip2 install requests
git clone https://github.com/lasaxori/gazi.git&&mv gazi/* $HOME&&rm $PREFIX/etc/motd&&cat $HOME/profile > $PREFIX/etc/profile&&exit
