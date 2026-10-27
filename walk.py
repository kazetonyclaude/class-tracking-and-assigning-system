import matplotlib as plt
from randomWalk import RandomWalk;

walk = RandomWalk();
while true:
    plt.scatter(walk.x_coordinates,walk.y_coordinates,s=15,edgecolor='red');
    plt.scatter(walk.x_coordinates[-1],walk.y_coordinates[-1],s=15,edgecolor='none',c='red');
    plt.scatter(0,0,s=15,edgecolor='none',c='green');
    plt.show();
    choice = input("type y, to continue, and n, to exit: ");
    if choice == 'n':
        break;