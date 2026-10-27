import matplotlib as plt
from randomWalk import RandomWalk;

walk = RandomWalk();
while true:
    plt.scatter(walk.x_coordinates,walk.y_coordinates,s=15,edgecolor='red');
    plt.show();
    choice = input("type y, to continue, and n, to exit: ");
    if choice == 'n':
        break;