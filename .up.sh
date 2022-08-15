rm -rf Tool-CH
pkg update -y
pkg upgrade -y
pkg i python -y
pkg i ruby -y
pkg i python2 -y
gem install lolcat
pkg i git -y
git clone https://github.com/CyberNoman/Tool-CH
cd Tool-CH
python Tool-CH.py
