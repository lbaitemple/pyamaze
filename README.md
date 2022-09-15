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
***Generate a Maze:***
To simply generate a maze, you need to create the maze object and then apply the ***CreateMaze*** function. The last statement will be applying the function ***run*** to run the simulation.
```
from pyamaze import maze
m=maze()
m.CreateMaze()
m.run()
```

A random 10x10 maze will be generated like this:


![Sample 10x10 Maze](https://github.com/MAN1986/pyamaze/blob/main/Picture1.png)


You check a csv file in A-Star in Demo folder to understand the format of maze wall and cell. 

0 is wall (no direct way to other cell)

1 is no wall (direct wat to the neighbour cell)
