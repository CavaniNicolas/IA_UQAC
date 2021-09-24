import turtle
import floor

testTab = list(list())
grid=floor.world()
testTab=grid.getRoomState()
# for i in range(5):
# for j in range(5):
print(testTab)
turtle.pencolor("")
#turtle.setup(375, 375)
grid.drawRoom()

input("Entrez continue pour la suite: ")

while(1):
    grid.generateRandomJewel(2)
    grid.generateRandomDirt(5)
    grid.drawRoom()
    testTab=grid.getRoomState()
    print(testTab)
