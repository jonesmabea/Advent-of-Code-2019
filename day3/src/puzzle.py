import numpy as np

move_dict = {"R": [1, 0], "L": [-1, 0], "D": [0, -1], "U": [0, 1]}

def parse_input():
    wires = dict()
    with open("input_d3.txt", "r") as ifh:
        for ind, line in enumerate(ifh):
            wires[ind] = [x.strip() for x in line.split(',')]
    return wires

def parse_action(action):
    dir, length = action[0], eval(action[1:])
    return dir, length

def get_cartesian_plane(move_list):
    start = [0, 0]
    move_list_in_cp ={}
    cnt = 0
    for dir, length in move_list:
        move_in_cp = move_dict[dir]
        for _ in range(length):
            start = np.add(start, move_in_cp)
            cnt+=1
            if tuple(start) not in move_list_in_cp:
                move_list_in_cp[tuple(start)] = cnt
    return move_list_in_cp
def calculate_shortest_manhattan_dist(intersecting_points):
    return np.min(np.sum(np.abs(intersecting_points), axis=1))

def calculate_shortest_wires(intersecting_points, wire1_path, wire2_path):
    return np.min([np.add(wire1_path[point],wire2_path[point]) for point in intersecting_points])


if __name__ == "__main__":

    wires = parse_input()
    wire1, wire2 = wires.values()
    parse_action_fn = lambda x : parse_action(x)
    wire1 = [parse_action_fn(x) for x in wire1]
    wire2 = [parse_action_fn(x) for x in wire2]

    wire1_cp= get_cartesian_plane(wire1)
    wire2_cp = get_cartesian_plane(wire2)


    intersecting_points = tuple(set(wire1_cp.keys()).intersection(set(wire2_cp.keys())))


    shortest_path = calculate_shortest_manhattan_dist(intersecting_points)

    shortest_dist = calculate_shortest_wires(intersecting_points, wire1_cp, wire2_cp)

    print(f"Puzzle 1: {shortest_path} Puzzle 2: {shortest_dist}")
