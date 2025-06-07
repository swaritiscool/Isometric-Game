import pygame
import json
import os
from Tiling_Management import Block, Tiles
from Entities import Player
from conversions import convert_vals_real, convert_vals_virtual

pygame.init()

S_WIDTH, S_HEIGHT = 1300, 700
SCREEN = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
FPS = 60
with open(os.path.join("global_data", "TILE_SIZE.txt"), 'r') as f:
    TILE_SIZE = f.read()
    TILE_SIZE = int(TILE_SIZE)
clock = pygame.time.Clock()
player = Player(0, 0, 0, 0, 100, (0, 0, 0))
Player_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "characters", "br.png")), (TILE_SIZE, TILE_SIZE))
Grass_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tile.png")), (TILE_SIZE, TILE_SIZE))
wood_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "wood.png")), (TILE_SIZE, TILE_SIZE))

def load_map():
    with open('map.json', 'r') as f:
            raw_data = json.load(f)
    map_data = {}
    for key, tile_data in raw_data.items():
        i, j, z = map(int, key.split(","))
        map_data[(i, j, z)] = tile_data

    return map_data

def draw_player(player):
    grid_x, grid_y = convert_vals_real(player.i - 1, player.j - 1, player.z)
    grid_x += S_WIDTH //2
    grid_y += S_HEIGHT // 4
    SCREEN.blit(Player_img, (grid_x, grid_y))

def draw_map():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    hover_offset = 15
    hovered_tile = None
    tiles = Tiles()
    map = {}

    if len(map) == 0:
        map = load_map()

        for (i, j, z), tile_data in map.items():
            lt = list((i, j, z))
            grid_x, grid_y = convert_vals_real(lt[0], lt[1], lt[2])
            grid_x += S_WIDTH // 2
            grid_y += S_HEIGHT // 4

            block = Block(
                tile_data.get("name", "unknown"),
                lt[0], lt[1], lt[2],
                grid_x, grid_y,
                tile_data.get("mov_weight", 1),
                tile_data.get("breakable", 0)  # Default to 0 if key is missing
            )
            tiles.add(block)

            tile_rect = pygame.Rect(grid_x, grid_y, TILE_SIZE, TILE_SIZE // 2)

            if tile_rect.collidepoint(mouse_x, mouse_y):
                hovered_tile = (i, j, z)

    # i is the x pos
    # j is the y pos
    # for z in range (0, 1):
    # for i in range(0, S_HEIGHT // TILE_SIZE + 1):
    # for j in range(0, S_HEIGHT // TILE_SIZE + 1):
    # grid_x, grid_y = convert_vals_real(i, j, z)
    # grid_x += S_WIDTH // 2
    # grid_y += S_HEIGHT // 4
    # grass = Block("grass", i, j, z, grid_x, grid_y, 1)
    # tile_rect = pygame.Rect(grid_x, grid_y, TILE_SIZE, TILE_SIZE // 2)
    # tile_positions.append((grid_x, grid_y, tile_rect, i, j))
    # tiles.add(grass)
    # if tile_rect.collidepoint(mouse_x, mouse_y):
    # hovered_tile = (i, j, z)

    for block in tiles.get():
        if hovered_tile == (block.i, block.j, block.z) and (player.i, player.j) != (block.i, block.j):
            SCREEN.blit(Grass_img, (block.grid_x, block.grid_y - hover_offset))
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                player.destination = (block.i, block.j, block.z)
                print("New Destination Set")
        else:
            SCREEN.blit(Grass_img, (block.grid_x, block.grid_y))
    
    return tiles

def draw_window():
    SCREEN.fill((135, 206, 235))

def handle_save_to_file(tiles):
    map = tiles.get_dict()
    with open("map.json", 'w') as f:
        json.dump(map, f, indent=4)
    print("Saved Map To File")

def add_wood(tiles):
    print("Started")
    mouse_x, mouse_y = pygame.mouse.get_pos()
    i, j = convert_vals_virtual(mouse_x, mouse_y)
    z = 0
    map = tiles.get_dict()
    key = (i, j, z)
    print(key)
    if key not in map:
        print("Key not in map")
        return
    while key in map:
        print("In Map")
        z += 1
        key = (i, j, z)
    print(f"Key: {key}")
    grid_x, grid_y = convert_vals_real(i, j, z)
    block = Block("wood", i, j, z, grid_x, grid_y, 0, 1)
    tiles.add(block)
    SCREEN.blit(wood_img, (grid_x, grid_y))

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    key_pressed = pygame.key.get_pressed()
    draw_window()
    tiles = draw_map()
    draw_player(player)
    if key_pressed[pygame.K_s] and key_pressed[pygame.K_LCTRL]:
        handle_save_to_file(tiles)
    player.move(tiles.get_dict())
    mouse_events = pygame.mouse.get_pressed()
    if mouse_events[2]:
        print("Adding Wood")
        add_wood(tiles)
    pygame.display.update()
