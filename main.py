import turtle
import floor

testTab=list(list())
grid=floor.world()
testTab=grid.getRoomState(grid)
for i in range(5):
    for j in range(5):
        print(testTab[i][j], " ")
    print("\n")
