from colors import Colors
import pygame as pg
from position import Position

class Block:
    def __init__(self, id) -> None:
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.col_offset = 0
        self.state = 0
        self.color = Colors.get_cell_colors()

    # Each block is made of cells in specific positions depending on the current state of the block 
    # returns a list of tiles that were moved into new rows and columns
    def get_cell_positions(self):
        tiles = self.cells[self.state]
        moved_tiles = []
        for position in tiles:
                position = Position(position.row + self.row_offset, position.col + self.col_offset)
                moved_tiles.append(position)
        return moved_tiles
    
    # Moves the block into the correct rows and columns
    def move(self, rows, cols):
         self.row_offset += rows
         self.col_offset += cols
    
    # Rotates the block qnd resets the rotation state to its original state once all rotations have been done
    def rotate(self):
         self.state += 1
         if self.state == 4:
              self.state = 0

    # Undoes an illegal rotation, namely when the rotation leaves a portion of the block off the grid 
    # or meshes with an existing block
    def undo_rotate(self):
         self.state -= 1
         if self.state == 0:
              self.state = len(self.cells) - 1

    # Draws the block onto the screen
    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pg.Rect(offset_x + tile.col * self.cell_size, 
				offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1)
            pg.draw.rect(screen, self.color[self.id], tile_rect)