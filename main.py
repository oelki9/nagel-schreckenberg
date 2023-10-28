#!/usr/bin/env python3
"""The Nagel–Schreckenberg model is a theoretical model for the simulation of freeway traffic.
https://en.wikipedia.org/wiki/Nagel%E2%80%93Schreckenberg_model
A good exercise to learn some python ..."""

__author__ = "Uwe Ressler"
__copyright__ = "Copyright 2023"
__credits__ = ["Kai Nagel", "Michael Schreckenberg"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = ""
__email__ = ""
__status__ = "Development"  # Development, Production
import random
import time
from parameters import get_parameters, fg

# LEN_OF_CELL = 7.5  # 7.5 m per cell => 1 cell per second ==> 27 km/h
MT_CELL = -1  # empty cell


def setup(num_of_cells, num_of_cars):
    """road setup and place cars randomly"""
    cells = [MT_CELL for _ in range(num_of_cells)]
    cars_placed = 0
    while cars_placed < num_of_cars:
        r = random.randint(0, num_of_cells - 1)
        if cells[r] == MT_CELL:
            cells[r] = 0
            cars_placed += 1
    return cells


def accelerate(cells, v_max):
    """accelerate if actual speed is below v_max"""
    for n in range(len(cells)):
        if MT_CELL < cells[n] < v_max:
            cells[n] += 1
    return cells


def slow_down(cells):
    """slow down if cars are in front"""
    for n in range(len(cells)):
        if cells[n] != MT_CELL:
            for c in range(1, cells[n] + 1):  # actual speed is stored in cells[n]
                if cells[(n + c) % len(cells)] != MT_CELL:
                    cells[n] = c - 1
                    break
    return cells


def randomize(cells, probability):
    """With a probability reduce the speed of a car by 1, if the speed is not already 0."""
    for n in range(len(cells)):
        if cells[n] > 0 and random.random() < probability:
            cells[n] -= 1
    return cells


def move_cars(cells):
    cells_new = [MT_CELL for _ in range(len(cells))]
    for n in range(len(cells)):
        if cells[n] != MT_CELL:
            cells_new[(n + cells[n]) % len(cells)] = cells[n]
    return cells_new


def print_cells(cells):
    """print all cells"""
    print(f"{fg['lightgrey']}>>>", end="")
    for cell in cells:
        # if cell == MT_CELL:
        #     print(" ", end="")
        match cell:
            case -1:  # MT_CELL
                print(" ", end="")
            case 0:
                print(f"{fg['red']}{cell}", end="")
            case 1:
                print(f"{fg['pink']}{cell}", end="")
            case 2:
                print(f"{fg['yellow']}{cell}", end="")
            case 3:
                print(f"{fg['purple']}{cell}", end="")
            case 4:
                print(f"{fg['blue']}{cell}", end="")
            case 5:
                print(f"{fg['lightgreen']}{cell}", end="")
        # else:
        #     print(cell, end="")
    print(f"{fg['lightgrey']}>>>")


def main():
    para = get_parameters()  # ok
    cells = setup(para["num_of_cells"], para["num_of_cars"])  # ok
    while True:
        cells = accelerate(cells, para["v_max"])  # ok
        cells = slow_down(cells)  # ok
        cells = randomize(cells, para["probability"])  # ok
        cells = move_cars(cells)  # ok
        print_cells(cells)  # ok
        time.sleep(para["delay"])


if __name__ == '__main__':
    print(fg["green"])
    main()
