import pygame
import os
from Tiling_Management import Block, Tiles

pygame.init()

S_WIDTH, S_HEIGHT = 1300, 700
SCREEN = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
FPS = 60
TILE_SIZE = 70
clock = pygame.time.Clock()
Tile = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tile.png")), (TILE_SIZE, TILE_SIZE))

def convert_vals_real(i, j, z):
    grid_x = ((i * 1 + j * -1) * TILE_SIZE / 2) - TILE_SIZE /2
    grid_y = (i * 0.5 + j * 0.5) * TILE_SIZE / 2 - TILE_SIZE/2
    grid_y -= z * TILE_SIZE / 2 - 1
    return grid_x, grid_y

def convert_vals_virtual(grid_x, grid_y):
    gx = grid_x + TILE_SIZE / 2
    gy = grid_y + TILE_SIZE / 2

    i = (2 * gx + 4 * gy) / (2 * TILE_SIZE)
    j = (4 * gy - 2 * gx) / (2 * TILE_SIZE)

    return round(i), round(j)

def draw_floor():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    hover_offset = 15
    hovered_tile = None
    tiles = Tiles()

    # i is the x pos
    # j is the y pos
    for z in range (0, 1):
        for i in range(0, S_HEIGHT // TILE_SIZE + 1):
            for j in range(0, S_HEIGHT // TILE_SIZE + 1):
                grid_x, grid_y = convert_vals_real(i, j, z)
                grid_x += S_WIDTH // 2
                grid_y += S_HEIGHT // 4
                grass = Block("grass", i, j, z, grid_x, grid_y, Tile, 1)

                tile_rect = pygame.Rect(grid_x, grid_y, TILE_SIZE, TILE_SIZE // 2)
                # tile_positions.append((grid_x, grid_y, tile_rect, i, j))
                tiles.add(grass)

                if tile_rect.collidepoint(mouse_x, mouse_y):
                    hovered_tile = (i, j, z)

    for block in tiles.get():
        if hovered_tile == (block.i, block.j, block.z):
            SCREEN.blit(Tile, (block.grid_x, block.grid_y - hover_offset))
        else:
            SCREEN.blit(Tile, (block.grid_x, block.grid_y))
    
    return tiles

def draw_window():
    SCREEN.fill((135, 206, 235))

def handle_save_to_file(tiles):
    if pygame.mouse.get_pressed()[0]:
        for block in tiles.get():
            print((block.i, block.j, block.z))

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    draw_window()
    tiles = draw_floor()
    handle_save_to_file(tiles)
    pygame.display.update()
