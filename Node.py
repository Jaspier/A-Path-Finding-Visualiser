import pygame

import style


class Node:
    def __init__(self, row, col, width, canvas_height):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = style.WHITE
        self.parents = []
        self.width = width
        self.canvas_height = canvas_height

    def get_pos(self):
        return self.row, self.col

    def is_open(self):
        return self.color == style.GREEN

    def is_closed(self):
        return self.color == style.DARKGREY

    def is_wall(self):
        return self.color == style.BLACK

    def is_start_node(self):
        return self.color == style.ORANGE

    def is_goal(self):
        return self.color == style.PURPLE

    def reset(self):
        self.color = style.WHITE

    def make_start_node(self):
        self.color = style.ORANGE

    def make_open(self):
        self.color = style.GREEN

    def make_closed(self):
        self.color = style.DARKGREY

    def make_wall(self):
        self.color = style.BLACK

    def make_goal(self):
        self.color = style.PURPLE

    def make_path(self):
        self.color = style.TURQUOISE

    def draw_node(self, canvas):
        pygame.draw.rect(canvas, self.color, (self.x, self.y, self.width, self.width))

    def find_paths(self, grid):
        self.parents = []
        # if current_node row is not exceeding the bottom row
        # and the neighbour below is not a wall
        # append to parents array
        if self.row < self.canvas_height - 1 and not grid[self.row + 1][self.col].is_wall():  # DOWN PARENT
            self.parents.append(grid[self.row + 1][self.col])

        # if current_node row is above the highest row
        # and the neighbour above is not a wall
        # append to parents array
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():  # UP PARENT
            self.parents.append(grid[self.row - 1][self.col])

        # if current_node column is not exceeding the right-most column
        # and the neighbour to the right is not a wall
        # append to parents array
        if self.col < self.canvas_height - 1 and not grid[self.row][self.col + 1].is_wall():  # RIGHT PARENT
            self.parents.append(grid[self.row][self.col + 1])

        # if current_node column is not not exceeding the left-most column
        # and the neighbour to the left is not a wall
        # append to parents array
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():  # LEFT PARENT
            self.parents.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
