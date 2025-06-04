import os

with open(os.path.join("global_data", "TILE_SIZE.txt"), 'r') as f:
    TILE_SIZE = f.read()
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
