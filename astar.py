from queue import PriorityQueue

import pygame

from map import make_map, draw, get_clicked_pos, draw_path;

CANVAS_SIZE = 800
CANVAS = pygame.display.set_mode((CANVAS_SIZE, CANVAS_SIZE))
pygame.display.set_caption("A* Path Finding Algorithm")


def h_score(start_node_pos, goal_pos):  # Calculates the h score
    x_start_node, y_start_node = start_node_pos
    x_goal, y_goal = goal_pos
    return abs(x_start_node - x_goal) + abs(y_start_node - y_goal)


def astar(draw, map, start_node, goal):
    count = 0
    open_list = PriorityQueue()
    open_list.put((0, count, start_node))
    previous_node = {}  # dictionary of previously visited nodes
    g_score = {node: float("inf")
               for row in map for node in row}  # each node start_nodes with a value of infinity
    g_score[start_node] = 0
    f_score = {node: float("inf")
               for row in map for node in row}
    f_score[start_node] = h_score(start_node.get_pos(), goal.get_pos())

    open_list_temp = {start_node}

    while not open_list.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current_node = open_list.get()[2]  # [2] is the actual node being inspected and [0] is the f score of that node
        open_list_temp.remove(current_node)

        if current_node == goal:
            draw_path(previous_node, goal, draw)
            goal.make_goal()
            return True

        for parent in current_node.parents:
            temp_g_score = g_score[current_node] + 1  # Traversing to the next parent

            if temp_g_score < g_score[parent]:  # Finding the shortest path
                previous_node[parent] = current_node
                g_score[parent] = temp_g_score
                f_score[parent] = temp_g_score + h_score(parent.get_pos(), goal.get_pos())
                if parent not in open_list_temp:
                    count += 1
                    open_list.put((f_score[parent], count, parent))
                    open_list_temp.add(parent)
                    parent.make_open()

        draw()

        if current_node != start_node:
            current_node.make_closed()

    return False


def main(canvas, width):
    ROWS = 50
    map = make_map(ROWS, width)

    start_node = None
    goal = None

    run = True
    while run:
        draw(canvas, map, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT CLICK
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = map[row][col]
                if not start_node and node != goal:
                    start_node = node
                    start_node.make_start_node()

                elif not goal and node != start_node:
                    goal = node
                    goal.make_goal()

                elif node != goal and node != start_node:
                    node.make_wall()

            elif pygame.mouse.get_pressed()[2]:  # RIGHT CLICK
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = map[row][col]
                node.reset()
                if node == start_node:
                    start_node = None
                elif node == goal:
                    goal = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start_node and goal:
                    for row in map:
                        for node in row:
                            node.find_paths(map)

                    astar(lambda: draw(canvas, map, ROWS, width), map, start_node, goal)

                if event.key == pygame.K_r:
                    start_node = None
                    goal = None
                    map = make_map(ROWS, width)

    pygame.quit()


main(CANVAS, CANVAS_SIZE)
