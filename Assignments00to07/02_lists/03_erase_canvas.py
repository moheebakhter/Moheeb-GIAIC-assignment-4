import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40

def create_grid(canvas):
     cells = []
     for row in range(0,CANVAS_HEIGHT, CELL_SIZE):
          row_cells = []
          for col in range(0,CANVAS_WIDTH, CELL_SIZE):
               rect = canvas
               