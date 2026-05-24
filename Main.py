from tkinter import *
import Settings
import Utility
from cell import Cell

# Method
root = Tk()

# GUI Settings 
root.configure(bg="white") # Changes Background Color
root.geometry(f"{Settings.WIDTH}x{Settings.HEIGHT}") # Sets Window Size
root.title(Settings.TITLE) # Changes Title of Window
root.resizable(False, False) # Prevents Window resizing

# Creating Frames/Objects
game_frame = Frame (root, bg="red", width=500, height=450)
game_frame.place(x=12, y=82)

top_frame = Frame (root, bg="blue", width=500, height=75)
top_frame.place(x=12, y=2)

for x in range(Settings.GRID_SIZE1):
    for y in range(Settings.GRID_SIZE1):
        c = Cell(x, y)
        c.create_btn_object(game_frame)
        c.cell_btn_object.grid(row=x, column=y)

# print(Cell.all) # Debugging: Print all cell instances to verify they are created correctly  

Cell.randomize_mines() # Call the method to randomize mines (currently a placeholder)
# for c in Cell.all:
#    print(f"Cell at ({c.x}, {c.y}) - Is Mine: {c.is_mine}") # Debugging: Print the status of each cell to verify mine randomization

# Call the label from cell class
Cell.create_cell_count_label(top_frame)
Cell.cell_count_label_object.place(x=0, y=0) # Place the label in the top frame
'''
c1 = Cell(0, 0)
c1.create_btn_object(game_frame)
c1.cell_btn_object.grid(row=0, column=0)


c2 = Cell(0, 1)
c2.create_btn_object(game_frame)
c2.cell_btn_object.grid(row=0, column=1)
'''

# Calling Method
root.mainloop()