'''
Project Name: Random Walk
Author: Robbie Platt
Due Date: 2021-12-04
Course: CS1400-zzz




I learned how to use the turtle.stamp. Using turtle.stamp I will display the endpoints
of the 3 different people (Pa, Mi-Ma (shown as ma via dictionaries), and Reg.
'''
import subprocess
import tempfile
import turtle #Doing both turtle imports as you did both, don't want to miss something, 
import random
import turtle
import statistics
import sys
from functools import reduce
def main():
    """
    Defines the main function. All of the code is contained within.
    """


    
    screen = turtle.getscreen()
    screen.setup(width = 300, height = 400)
    turtle.shapesize(0.5, 0.5)
    current = [0,0]
    n = [0,1]
    s = [0,-1]
    e = [1,0]
    w = [-1,0]
    """
    lengths = list(map(int(sys.argv[1].split(','))))
    trials = int(sys,argv[2])
    walker = sys.argv[3]
    """
    lengths = [100, 1000]
    trials = 50
    walker = 'all'




    """
    a = end_point[0]
    print(a)
    """
    """
    c = 
    distance = (end_point[0])**2
    
    max_distance = max(distances)
    min_distance = min(distances)
    average_distance = statistics.mean(distances)
    std_dev = statistics.stdev(distances)
    cv = std_dev / average
    """
    simulate([100, 1000], 50, "all")
    plot()
    save_to_image(dest='random_walk.png')
    #help(statistics.mean)
def simulate(walk_lengths, trials, person):
    """
    Defines the simulate function that calculates the data and prints it to the screen.
    """

    try:
        condition = (sys.argv[1]).lower()
        if condition == "100":
            steps = 100
        elif condition == "1000":
            steps = 1000
        elif condition == "10":
            steps = 10
    except IndexError:
        print("Usage index 1: 100 for 100 steps, 1000 for 1000 steps.")
        steps = 100
    trials = 50


    pa = {"name":"Pa", "start":(0,0), "cur":[0,0], "end_point":[], "distance":[], "rules":([0,1],[0,-1],[1,0],[-1,0]), "shape":'circle', "color":'black'}
    ma = {"name":"Ma", "start":(0,0), "cur":[0,0], "end_point":[], "distance":[], "rules":([0,1],[1,0],[0,-1],[0,-1],[-1,0]), "shape":'square', "color":'green'}
    reg = {"name":"Reg", "start":(0,0), "cur":[0,0], "end_point":[], "distance":[], "rules":([1,0],[-1,0]), "shape":'triangle', "color":'red'}
    people = [pa, ma, reg]
    run_trials(people, trials, steps)
    for person in people:
        for _i in range(trials):
            person['cur'] = list(person['start'])
            for _j in range(steps):
                choice = random.choice(person['rules'])
                person['cur'] = step(person['cur'], choice)
                person["end_point"].append(person["cur"])
                #end of j in steps
                
                
                
                
                
                
                
                lengths_x = []
                lengths_y = []
                list_dist = []
                average_list = []

                for point in person['end_point']:
                    x_end_point = point[0] * 5
                    y_end_point = point[1] * 5
                    lengths_x.append((x_end_point)**2)
                    lengths_y.append((y_end_point)**2)
        sum_xy = lengths_x + lengths_y
    def average_distance():
        
        summ = reduce(lambda x, y: x + y, sum_xy)
        dist = summ**0.5
        list_dist.append(dist)
        length = len(sum_xy)
        average = dist/(len(sum_xy))
        
        print(lengths_y)
        print(lengths_x)
        print(sum_xy)
        print(summ)
        print(dist)   
        print(list_dist)
        print(length)
    
        print(average)
        print(f"{person['name']} random walk of 100 steps")
        print(f"{person['name']} Mean {average:.1f}")
        
    average_distance()
    def standard_deviation():
        pass
        

    
    

    
    
    #print(f"Pa Mean: {average[0]}")

            

def plot():
    """
    Function that draws the endpoints of the calculations for the 50 trials of 100 steps. 
    """
    turtle.tracer(n = 99, delay = 50)
    steps = 100
    trials = 50


    pa = {"name":"Pa", "start":(0,0), "cur":[0,0], "end_point":[], "distance":[], "rules":([0,1],[0,-1],[1,0],[-1,0]), "shape":'circle', "color":'black'}
    ma = {"name":"Mi-Ma", "start":(0,0), "cur":[0,0], "end_point":[], "distance":[], "rules":([0,1],[0,-1],[1,0],[-1,0],[0,-1]), "shape":'square', "color":'green'}
    reg = {"name":"Reg", "start":(0,0), "cur":[0,0], "end_point":[], "distance":[], "rules":([1,0],[-1,0]), "shape":'triangle', "color":'red'}
    people = [pa, ma, reg]

    for person in people:
        for _i in range(trials):
            person['cur'] = list(person['start'])
            for _j in range(steps):
                choice = random.choice(person['rules'])
                person['cur'] = step(person['cur'], choice)
                person["end_point"].append(person["cur"])
                #end of j in steps
                
                color = person['color']
                shape = person['shape']
                
                turtle.up()
                turtle.color(color)
                turtle.shape(shape)
                for point in person['end_point']:
                    x_end_point = point[0] * 5
                    y_end_point = point[1] * 5
                    
            
            turtle.goto(x_end_point, y_end_point)
            turtle.stamp()



def run_trials(people, trials, steps):
    """
    defines function that runs the individual trials and prints to the screen.
    """
    for person in people:
        for _i in range(trials):
            person['cur'] = list(person['start'])
            for _j in range(steps):
                choice = random.choice(person['rules'])
                person['cur'] = step(person['cur'], choice)
                #end of j in steps
            print(f"{person['name']}: End of trial number {_i} location: {person['cur']}")
    
def step(current, direction):
    """
    defines how to move each step.
    """
    current[0] = current[0] + direction[0]
    current[1] = current[1] + direction[1]
    return current

def save_to_image(dest='random_walk.png'):
    '''Saves the turtle canvas to dest. Do not modify this function.'''
    with tempfile.NamedTemporaryFile(prefix='random_walk',
                                     suffix='.eps') as tmp:
        turtle.getcanvas().postscript(file=tmp.name)
        subprocess.run(['gs',
                        '-dSAFER',
                        '-o',
                        dest,
                        '-r200',
                        '-dEPSCrop',
                        '-sDEVICE=png16m',
                        tmp.name],
                       stdout=subprocess.DEVNULL)
    
if __name__== "__main__":
    """
    Program starts here.
    """
    main()


