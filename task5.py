import random
def calculate_pi():
    points= 100000
    inside= 0
    count= 0
    while count <points:
        x= random.uniform(-1.0,1.0)
        y= random.uniform(-1.0, 1.0)
        if (x* x) +(y* y)<= 1.0:
            inside= inside +1
        count= count + 1
    pi = 4* (inside/ points)
    return pi