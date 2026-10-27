from random import choice

class RandomWalk():
    def __init__(self):
        points = 2
        self.x_coordinates = [0]
        self.y_coordinates = [0]
        
    def randomWalk(self):
        while len(self.x_coordinates) < 2:
            x_direction = choice([-1,1]);
            x_distance = choice([0,1,2,3,4]);
            x_step = x_direction * x_distance;
            
            y_direction = choice([-1,1]);
            y_distance = choice([0,1,2,3,4]);
            y_step = y_direction * y_distance;
            
            if x_step == 0 and y_step == 0:
                continue;
                
            next_xstep = self.x_coordinates[-1] + x_step;
            next_ystep = self.y_coordinates[-1] + y_step;
            self.x_coordinates.append(next_xstep)
            self.y_coordinates.append(next_ystep)
            