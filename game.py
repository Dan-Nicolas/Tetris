from grid import Grid
from blocks import *
import random
import pygame as pg

class Game:
    def __init__(self) -> None:
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), SBlock(), Square(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        pg.mixer.music.load("Sounds/music.ogg")
        pg.mixer.music.play(-1) # sound plays indefinitely
        self.rotate_sound = pg.mixer.Sound("Sounds/rotate.ogg")
        self.clear_sound = pg.mixer.Sound("Sounds/clear.ogg")

    # Updates score when lines are cleared and for each 'down' pressed
    def update_score(self, lines_cleared, move_down_pts):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 1000
        self.score += move_down_pts

    # Gets a random block for this current block 
    # removes the chosen block from the list so every block is used each cycle 
    def get_random_block(self):
        if len(self.blocks) == 0: # resets the pool of blocks to randomly choose
            self.blocks = [IBlock(), JBlock(), LBlock(), SBlock(), Square(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    # Draws the grid current block into the starting position 
    # as well as draws the next block to be used in the "Next" window
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen,11, 11)
        if self.next_block.id == 3: # this block is placed differently to accommodate its shaped to be centered in the "Next" window
            self.next_block.draw(screen, 255, 270)
        elif self.next_block.id == 4: # this block is placed differently to accommodate its shaped to be centered in the "Next" window
            self.next_block.draw(screen, 260, 260)
        else:
            self.next_block.draw(screen, 270, 250)

    # Moves the block to the left while its within the borders of the grid or doesn't mesh with other existing blocks
    def move_left(self):
        self.current_block.move(0,-1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,1)

    # Moves the block to the right while its within the borders of the grid or doesn't mesh with other existing blocks
    def move_right(self):
        self.current_block.move(0,1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,-1)
    
    # Moves the block to the down while its within the borders of the grid or doesn't mesh with other existing blocks
    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1,0)
            self.lock_block()
    
    # locks the block in place once it has
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for pos in tiles:
            self.grid.grid[pos.row][pos.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True

    # Checks to see if the current block and all its parts fits in the grid appropriately, 
    # returns True or False if so
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.col) == False:
                return False
        return True
    
    # Resets the whole game 
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), SBlock(), Square(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    # Rotates the current block, 
    # undoes rotation if new rotation makes the block to be in an illegal position or
    # plays a sound
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotate()
        else:
            self.rotate_sound.play()

    # Checks if the block is with the borders of the grid, returns True or False
    def block_inside(self):
         tiles = self.current_block.get_cell_positions()
         for tile in tiles:
             if self.grid.is_inside(tile.row, tile.col) == False:
                 return False
         return True
         