cd $HOME
pkg install python2 -y
pip2 install requests
mv gazi/* $HOME
rm $PREFIX/etc/motd&&cat $HOME/profile > $PREFIX/etc/profile
exit
