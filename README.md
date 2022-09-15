In this documentation, we address the issue in Ubuntu 18.04 because X11 is working different for tk


```
sudo apt install -y python3-tk
git clone -b ece3432 https://github.com/lbaitemple/pyamaze
cd pyamaze
sudo python3 setup.py install

```

```
export X11Forwarding=yes 
export DISPLAY=:0
```
