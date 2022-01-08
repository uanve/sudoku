import tkinter as tk
from random import randint
from PIL import Image, ImageTk
from initial_solution import csv_to_list

num_size = 70

class Sudoku(tk.Canvas):
    def __init__(self):
        super().__init__(
            width=9*num_size, height=9*num_size, background="white", highlightthickness=0
        )

        self.grid = csv_to_list()
        self.create_grid()
        self.create_game()
        
        self.position = (0,0)

        self.bind("<Button-1>", self.click)
        self.bind_all("<Key>", self.key_press)
        self.bind('<Button-3>', self.delete_cell)

        self.pack()

        

    def create_grid(self):
        self.create_rectangle(0, 0, 9*num_size, 9*num_size, outline="#525d69")
        # horizontal lines
        self.create_line(0,1*num_size,9*num_size,1*num_size,dash=(4, 2))
        self.create_line(0,2*num_size,9*num_size,2*num_size,dash=(4, 2))
        self.create_line(0,3*num_size,9*num_size,3*num_size)
        self.create_line(0,4*num_size,9*num_size,4*num_size,dash=(4, 2))
        self.create_line(0,5*num_size,9*num_size,5*num_size,dash=(4, 2))
        self.create_line(0,6*num_size,9*num_size,6*num_size)
        self.create_line(0,7*num_size,9*num_size,7*num_size,dash=(4, 2))
        self.create_line(0,8*num_size,9*num_size,8*num_size,dash=(4, 2))
        

        # vertical lines
        self.create_line(1*num_size,0,1*num_size,9*num_size,dash=(4, 2))
        self.create_line(2*num_size,0,2*num_size,9*num_size,dash=(4, 2))
        self.create_line(3*num_size,0,3*num_size,9*num_size)
        self.create_line(4*num_size,0,4*num_size,9*num_size,dash=(4, 2))
        self.create_line(5*num_size,0,5*num_size,9*num_size,dash=(4, 2))
        self.create_line(6*num_size,0,6*num_size,9*num_size)
        self.create_line(7*num_size,0,7*num_size,9*num_size,dash=(4, 2))
        self.create_line(8*num_size,0,8*num_size,9*num_size,dash=(4, 2))

    def create_game(self):
        grid = self.grid
        for key in grid.keys():
            i,j = key
            if grid[key] != 0:
                self.create_text((i+0.5)*num_size,(j+0.5)*num_size,text=str(grid[key]))    
                
    

    def click(self,event):

        try:
            self.delete('click_rectangle')
        except:
            pass
        

        self.position = (event.x//num_size, event.y//num_size)
        X,Y = self.position
        x,y = X*num_size, Y*num_size

        self.create_rectangle(x,y,x+num_size,y+num_size,outline='red',tag='click_rectangle')
        

    def key_press(self,event):
        numb = event.char
        
        X,Y = self.position
        self.create_text((X+0.5)*num_size,(Y+0.5)*num_size,text=numb, fill='gray',tag='{}_{}'.format(X,Y)) 

    def delete_cell(self,event):
        X,Y = self.position
        print("trying to delete {}-{}".format(X,Y))
        
        self.delete('{}_{}'.format(X,Y))


root = tk.Tk()
root.title("Sudoku")
root.resizable(False, False)
root.tk.call("tk", "scaling", 4.0)

board = Sudoku()

root.mainloop()