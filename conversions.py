import os

with open(os.path.join("global_data", "TILE_SIZE.txt"), 'r') as f:
    TILE_SIZE = f.read()
    TILE_SIZE = int(TILE_SIZE)
    
def convert_vals_real(i, j, z):
    grid_x = ((i * 1 + j * -1) * TILE_SIZE / 2) - TILE_SIZE /2
    grid_y = ((i * 0.5 + j * 0.5) * TILE_SIZE / 2) - TILE_SIZE/2
    grid_y -= z * TILE_SIZE / 2 - 1
    return grid_x, grid_y

def convert_vals_virtual(grid_x, grid_y):
    i = (16*grid_y + 2*grid_x + 9 * TILE_SIZE) / 4*TILE_SIZE
    j = (16 * grid_y + 9 * TILE_SIZE - 2 * grid_x) / 8 * TILE_SIZE

    return round(i), round(j)
