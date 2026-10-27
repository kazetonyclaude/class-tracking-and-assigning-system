import matplotlib.pyplot as plt;
from randomWalk import RandomWalk;

while True:
    walk = RandomWalk(5000);
    walk.randomWalk();
    plt.scatter(walk.x_coordinates,walk.y_coordinates,s=15,edgecolor='none');
    plt.scatter(walk.x_coordinates[-1],walk.y_coordinates[-1],s=15,edgecolor='none');
    plt.scatter(0,0,s=15,edgecolor='none',c='red')
    plt.show();
    choice = input("type y, to continue, and n, to exit: ");
    if choice == 'n':
        break;