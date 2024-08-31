from colors import Colors
import pygame as pg

class Grid:
    def __init__(self) -> None:
        self.rows = 20
        self.cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]
        self.colors = Colors.get_cell_colors()

    # Prints the grid
    def print_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end = " ")
        
    # Checks if the current is within the borders of the grid
    def is_inside(self, row, col):
        if row >= 0 and row < self.rows and col >= 0 and col < self.cols:
            return True
        return False
    
     # Checks if a cell is empty
    def is_empty(self, row, col):
        if self.grid[row][col] == 0:
            return True
        return False
    
     # Checks if the row is full
    def is_row_full(self, row):
        for col in range(self.cols):
           if self.grid[row][col] == 0:
               return False
        return True
    
    # Clears the row
    def clear_row(self, row):
        for col in range(self.cols):
            self.grid[row][col] = 0

    # After rows have been cleared move down all non cleared rows and adjust the grid accordingly
    def move_row_down(self, row, num_rows):
        for col in range(self.cols):
            self.grid[row+num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0
    
    # Reset the whole grid
    def reset(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col] = 0

    # Starting from the bottom clear any full rows, move down rows, and return the number of completed rows
    def clear_full_rows(self):
        completed = 0
        for row in range(self.rows-1, 0 , -1):
           if self.is_row_full(row):
               self.clear_row(row)
               completed += 1
           elif completed > 0:
               self.move_row_down(row, completed)
        return completed
    
    # Draws the grid
    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_value = self.grid[row][col]
                cell_rect = pg.Rect(col * self.cell_size + 11, row * self.cell_size + 11,
                                    self.cell_size - 1, self.cell_size - 1)
                pg.draw.rect(screen, self.colors[cell_value], cell_rect)