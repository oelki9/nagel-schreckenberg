import os
# Constants
LOGO = """
                   ________________________
                  |   traffic         || -.\\
__                |      simulation   || |_\\\\             ______     ___
 L\\___  __~p\\___  |___________________|| -  |  __~p\\___  /[]  []\\  _/[]L\\__
.__,._)(_,.__,._) B_,-._,-.____________|,-._) (_,.__,._) \\__,.__|-(_,.__,._)
'--`'----`'--`'-----`-'-`-'-------------`-'-----`'--`'------`'------`'--`'--
"""

WIKI = """The Nagel–Schreckenberg model is a theoretical model for the simulation of freeway traffic. The model was 
developed in the early 1990s by the German physicists Kai Nagel and Michael Schreckenberg. It is essentially a 
simple cellular automaton model for road traffic flow that can reproduce traffic jams, i.e., show a slow down in 
average car speed when the road is crowded (high density of cars). The model shows how traffic jams can be thought of 
as an emergent or collective phenomenon due to interactions between cars on the road, when the density of cars is high 
and so cars are close to each other on average."""

# initial settings
INIT_NUM_OF_CELLS = 150
INIT_NUM_OF_CARS = 25
INIT_V_MAX = 5
INIT_PROBABILITY = 0.2
INIT_DELAY = 1

fg = {  # fg colors
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'orange': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'lightgrey': '\033[37m',
    'darkgrey': '\033[90m',
    'lightred': '\033[91m',
    'lightgreen': '\033[92m',
    'yellow': '\033[93m',
    'lightblue': '\033[94m',
    'pink': '\033[95m',
    'lightcyan': '\033[96m',
}

bg = {  # fg colors
    'black': '\033[40m',
    'red': '\033[41m',
    'green': '\033[42m',
    'orange': '\033[43m',
    'blue': '\033[44m',
    'purple': '\033[45m',
    'cyan': '\033[46m',
    'lightgrey': '\033[47m',
}


def clear():
    if os.name == "posix":
        os.system("clear")
        return
    os.system("cls")


def print_logo():
    clear()
    print(LOGO)


def print_help():
    """print some help"""
    print_logo()
    print("HELP")
    print("====\n")
    print(f"{WIKI}\n")
    print(f"The original model was designed with a cell length of 7.5 m, "
          f"7,5 m/s and a delay between steps of 1 s ==> 27 km/h (v = 1)"
          f"v_max = 5h ==> 135 km/h")
    input("\n  ==> ")
    get_parameters()


def get_parameters():
    # globals
    variable_dict = {"num_of_cells": INIT_NUM_OF_CELLS,
                     "num_of_cars": INIT_NUM_OF_CARS,
                     "v_max": INIT_V_MAX,
                     "probability": INIT_PROBABILITY,
                     "delay": INIT_DELAY}
    while True:
        valid_execute_chars = ('h', 's', 'x')
        valid_setting_chars = ('c', 'd', 'v', 'p', 'r')
        print_logo()
        print(f"actual settings: "
            f"number of cells: {variable_dict['num_of_cells']}, "
            f"number of cars: {variable_dict['num_of_cars']}, "
            f"v_max: {variable_dict['v_max']} ==> {variable_dict['v_max']*27} km/h, "
            f"probability: {int(variable_dict['probability']*100)} %, "              
            f"delay: {int(variable_dict['delay']*1000)} ms\n"
              )
        print("""     c - cells (number of cells)
     d - density (number of cars)
     v - v_max (1..5)
     p - probability
     r - round delay (between each simulation round)
     h - help
     s - start simulation >>> use CNTL-C to stop <<<
     x - exit""")
        answer = input("\n  ==> ").lower().split()
        if len(answer) == 0:
            pass
        elif answer[0] in valid_execute_chars:
            match answer[0]:
                case 's':
                    print("starting simulation ...")
                    return variable_dict
                case 'h':
                    print_help()
                case 'x':
                    clear()
                    exit("normal program end")
                case _:
                    pass
        elif answer[0] in valid_setting_chars and len(answer) == 2:
            if answer[1].isdigit():
                match answer[0]:
                    case 'c':
                        variable_dict.update({"num_of_cells": int(answer[1])})
                    case 'd':
                        variable_dict.update({"num_of_cars": int(answer[1])})
                    case 'v':
                        variable_dict.update({"v_max": int(answer[1])})
                    case 'p':
                        variable_dict.update({"probability": int(answer[1])/100})
                    case 'r':
                        variable_dict.update({"delay": float(answer[1])/1000})
                    case _:
                        pass


if __name__ == "__main__":
    print(get_parameters())
