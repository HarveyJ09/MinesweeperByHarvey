from tkinter import Button, Label
import random
import Settings
import ctypes
import sys

class Cell:
    all = []
    cell_count_label_object = None
    cell_count = Settings.CELL_COUNT

    def __init__(self,x,y, is_mine=False):
        self.x = x
        self.y = y
        self.is_opened = False
        self.is_mine = is_mine
        self.cell_btn_object = None

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            text="",
            width=5,
            height=2,
        )
        btn.bind('<Button-1>', self.left_click_actions)
        self.cell_btn_object = btn
        btn.bind('<Button-3>', self.right_click_actions)

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=f"Cells Left:{Settings.CELL_COUNT}",
            width=12,
            height=4,
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrrounded_cells_mines_length == 0:
                for cell in self.surrounded_cells:
                    cell.show_cell()
            self.show_cell()
        # print(event) # Debugging: Print the event object to see details
        # print("Left Clicked")

        self.cell_btn_object.unbind('<Button-1>') # Unbind left click to prevent multiple clicks on the same cell
        self.cell_btn_object.unbind('<Button-3>') # Unbind left click to prevent multiple clicks on the same cell

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
        return None
    
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1), # Top-left
            self.get_cell_by_axis(self.x - 1, self.y), # Left
            self.get_cell_by_axis(self.x - 1, self.y + 1), # Bottom-left
            self.get_cell_by_axis(self.x, self.y - 1), # Top
            self.get_cell_by_axis(self.x, self.y + 1), # Bottom
            self.get_cell_by_axis(self.x + 1, self.y - 1), # Top-right
            self.get_cell_by_axis(self.x + 1, self.y), # Right
            self.get_cell_by_axis(self.x + 1, self.y + 1), # Bottom-right
        ]
        
        cells = [cell for cell in cells if cell is not None]
        return cells

    

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=str(self.surrrounded_cells_mines_length), bg="lightgrey") # Example: Change button text to the number of surrounding mines and background to light grey

            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells Left:{Cell.cell_count}") # Update the cell count label to reflect the number of cells left (you may need to implement logic to track this count)
        self.is_opened = True

    @property
    def surrrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_mine(self):
        self.cell_btn_object.configure(text="M", bg="red") # Example: Change button text to "M" and background to red to indicate a mine
        ctypes.windll.user32.MessageBoxW(0, "Game Over!", "Minesweeper", 1)
        sys.exit() # Exit the game after showing the message box


    def right_click_actions(self, event):
        # Toggle flag: if already flagged, remove it; otherwise place a flag
        try:
            current_text = self.cell_btn_object.cget('text')
        except Exception:
            current_text = None

        if current_text == 'F':
            # remove flag
            self.cell_btn_object.configure(text='', bg='SystemButtonFace')
        else:
            # place flag
            self.cell_btn_object.configure(text='F', bg='yellow')
        if current_text == 'M':
            self.cell_btn_object.configure(text='M', bg='red') # Ensure mines remain visible even when flagged


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, Settings.MINES_COUNT) # Example usage, randomly selects the specified number of items from the list
        for picked_cell in picked_cells:
            picked_cell.is_mine = True # Set the is_mine attribute to True for the randomly selected cells
        print(picked_cells) # Debugging: Print the randomly selected items to verify functionality

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"