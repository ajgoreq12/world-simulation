import math
import random

x_arrows = 10
y_arrows = 10

grid_multiply = 1

arrows = [[0 for i in range(x_arrows)] for j in range(y_arrows)]
grid = [[0 for i in range(len(arrows[0])*grid_multiply)] for j in range(len(arrows)*grid_multiply)]

for y in range(len(arrows)):
    for x in range(len(arrows[y])):
        arrows[y][x] = random.randint(0,360)


new_list = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        y1 = y
        x1 = x

        multiplyed_x = 0
        multiplyed_y = 0

        x_true, y_true = True, True

        while x_true and y_true:
            if(y1 % grid_multiply == 0):
                multiplyed_y = y1/grid_multiply
                y_true = False
                if(x1% grid_multiply == 0):
                    multiplyed_x = x1/grid_multiply
                    x_true = False
                else:
                    x1 -= 1
            else:
                y1-=1

        multiplyed_x = int(multiplyed_x)
        multiplyed_y = int(multiplyed_y)

        if multiplyed_x < (len(arrows[0])-1) and multiplyed_y < (len(arrows)-1):

            

            first_angle = (-(x / (grid_multiply * 10))) * math.cos(arrows[multiplyed_y][multiplyed_x]) + (-(y / (grid_multiply * 10))) * math.sin(arrows[multiplyed_y][multiplyed_x])
            second_angle = (-(x / (grid_multiply * 10))) * math.cos(arrows[multiplyed_y][multiplyed_x+1]) + (-(y / (grid_multiply * 10))) * math.sin(arrows[multiplyed_y][multiplyed_x+1])
            third_angle = (-(x / (grid_multiply * 10))) * math.cos(arrows[multiplyed_y+1][multiplyed_x]) + (-(y / (grid_multiply * 10))) * math.sin(arrows[multiplyed_y+1][multiplyed_x])
            forth_angle = (-(x / (grid_multiply * 10))) * math.cos(arrows[multiplyed_y+1][multiplyed_x+1]) + (-(y / (grid_multiply * 10))) * math.sin(arrows[multiplyed_y+1][multiplyed_x+1])

            linear_1 = (1-(multiplyed_x - (x / (grid_multiply * 10)))) * first_angle + (1-(multiplyed_x - (x / (grid_multiply * 10)))) * second_angle
            linear_2 = (1-(multiplyed_x - (x / (grid_multiply * 10)))) * third_angle + (1-(multiplyed_x - (x / (grid_multiply * 10)))) * forth_angle

            value = (1-(multiplyed_y - (x / (grid_multiply * 10)))) * linear_1 + (1-(multiplyed_y - (x / (grid_multiply * 10)))) * linear_2

            new_list.append(value)
            print(x)

        

        

print(new_list)
