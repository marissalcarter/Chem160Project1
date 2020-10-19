import random
from random import choice
npart=500 
side=31  

maxsteps=10000 
perc=0
density=random.random()
steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]
grid[side//2][side//2]=1
for ipart in range(npart):
    x,y = side//2,side//2
    perc=0
    while 1:
        perc+=1
        grid[x][y]=0
        sx,sy = choice(steps)
        x += sx
        y += sy
        if x<0 or y<0 or x==side or y==side:
             perc+=1
             break
        if (grid[(x+1)%side][y]+grid[x][(y+1)%side]+grid[(x+side-1)%side][y]+grid[x][(y+side-1)%side])>0:
            continue
        else:
            break

prob=perc/npart
print("density= ", density)
print("probability= ", prob)
