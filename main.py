import turtle
import floor

from common import *

testTab=list(list())
grid=floor.world()
testTab=grid.getRoomState(grid)
for i in range(mansionSize):
    for j in range(mansionSize):
        print(testTab[i][j], " ")
    print("\n")
