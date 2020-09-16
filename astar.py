import pygame

from map import make_map, draw, get_clicked_pos, draw_path;

CANVAS_SIZE = 800
CANVAS = pygame.display.set_mode((CANVAS_SIZE, CANVAS_SIZE))
pygame.display.set_caption("A* Path Finding Algorithm")


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

                if event.key == pygame.K_r:
                    start_node = None
                    goal = None
                    map = make_map(ROWS, width)

    pygame.quit()


main(CANVAS, CANVAS_SIZE)