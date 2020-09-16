import pygame
from Node import Node;

import style;


def get_clicked_pos(pos, rows, width):
    square = width // rows  # Each square in map
    y, x = pos

    row = y // square
    col = x // square

    return row, col


def make_map(rows, width):
    map = []
    square = width // rows
    for i in range(rows):
        map.append([])
        for j in range(rows):
            node = Node(i, j, square, rows)  # square represents the width of each small square in the map
            map[i].append(node)  # appoints each square in the map as a node

    return map


def draw_map(canvas, rows, width):  # draws the map lines
    square = width // rows
    for i in range(rows):
        pygame.draw.line(canvas, style.GREY, (0, i * square), (width, i * square))
        for j in range(rows):
            pygame.draw.line(canvas, style.GREY, (j * square, 0), (j * square, width))


def draw_path(previous_node, current_node, draw):  # visual representation of the shortest path found
    while current_node in previous_node:
        current_node = previous_node[current_node]
        current_node.make_path()
        draw()


def draw(canvas, map, rows, width):
    canvas.fill(style.WHITE)

    for row in map:
        for node in row:
            node.draw_node(canvas)

    draw_map(canvas, rows, width)
    pygame.display.update()