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
import turtle #Doing both turtle imports as you did both, don't want to miss something
import random
import statistics
import sys
import functools
def main():
    """
    Defines the main function. All of the code is contained within.
    Use command line indices for function: position 1 is for
    """

    pa_ = None
    ma_ = None
    reg = None


    if sys.argv[3] == "Pa":
        person = [pa_]
    elif sys.argv[3] == "Mi-Ma":
        person = [ma_]
    elif sys.argv[3] == "Reg":
        person = [reg]
    elif sys.argv[3] == "all":
        person = [pa_, ma_, reg]




    simulate(sys.argv[1], sys.argv[2], {sys.argv[3]})
    plot()
    save_to_image(dest='random_walk.png')

def simulate(walk_lengths, trials, person):
    """
    Defines the simulate function that calculates the data and prints it to the screen.
    """
    steps = int(str(walk_lengths).strip("[]"))
    pa_ = {"name":"Pa", "start":(0,0), "cur":[0,0], "end_point":[], "distance":[], "rules":([0,1],[0,-1],[1,0],[-1,0]), "shape":'circle', "color":'black'}
    ma_ = {"name":"Mi-Ma", "start":(0,0), "cur":[0,0], "end_point":[], "distance":[], "rules":([0,1],[1,0],[0,-1],[0,-1],[-1,0]), "shape":'square', "color":'green'}
    reg = {"name":"Reg", "start":(0,0), "cur":[0,0], "end_point":[], "distance":[], "rules":([1,0],[-1,0]), "shape":'triangle', "color":'red'}
    if person == {'Pa'}:
        person = pa_
    elif person == {'Mi-Ma'}:
        person = ma_
    elif person == {'Reg'}:
        person = reg
    elif person == {'all'}:
        people = [pa_, ma_, reg]
        for person in people:
            for _i in range(int(trials)):
                person['cur'] = list(person['start'])
                for _j in range(steps):
                    choice = random.choice(person['rules'])
                    person['cur'] = step(person['cur'], choice)
        person["end_point"].append(person["cur"])
    else:
        print(person)
    for _i in range(int(trials)):
        person['cur'] = list(person['start'])
        for _j in range(steps):
            choice = random.choice(person['rules'])
            person['cur'] = step(person['cur'], choice)
    person["end_point"].append(person["cur"])

    lengths_x = []
    lengths_y = []
    list_dist = []

    for point in person['end_point']:
        x_end_point = point[0] * 5
        y_end_point = point[1] * 5
        lengths_x.append((x_end_point)**2)
        lengths_y.append((y_end_point)**2)
        sum_xy = lengths_x + lengths_y
        summ = functools.reduce(lambda x, y: x + y, sum_xy)
        dist = summ**0.5
        list_dist.append(dist)
        average = statistics.mean(sum_xy)
        standard_deviation = statistics.stdev(sum_xy)
        coefficient = standard_deviation/average
        maximum = max(sum_xy)
        minimum = min(sum_xy)
        print(f"{person['name']} random walk of {steps} steps")
        print(f"Mean = {average:.1f} CV = {coefficient:.1f} ")
        print(f"Max = {maximum:.1f} Min = {minimum:.1f} ")

def plot():
    """
    Function that draws the endpoints of the calculations for the 50 trials of 100 steps.
    """
    screen = turtle.getscreen()
    screen.setup(width = 300, height = 400)
    turtle.shapesize(0.5, 0.5)
    turtle.tracer(n = 99, delay = 50)
    steps = 100
    trials = 50


    pa_ = {"name":"Pa", "start":(0,0), "cur":[0,0], "end_point":[], "distance":[], "rules":([0,1],[0,-1],[1,0],[-1,0]), "shape":'circle', "color":'black'}
    ma_ = {"name":"Mi-Ma", "start":(0,0), "cur":[0,0], "end_point":[], "distance":[], "rules":([0,1],[1,0],[0,-1],[0,-1],[-1,0]), "shape":'square', "color":'green'}
    reg = {"name":"Reg", "start":(0,0), "cur":[0,0], "end_point":[], "distance":[], "rules":([1,0],[-1,0]), "shape":'triangle', "color":'red'}
    people = [pa_, ma_, reg]

    for person in people:
        for _i in range(trials):
            person['cur'] = list(person['start'])
            for _j in range(steps):
                choose = random.choice(person['rules'])
                person['cur'] = step(person['cur'], choose)
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
    main()




