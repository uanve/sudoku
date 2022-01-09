import tkinter as tk
from random import randint
from PIL import Image, ImageTk
from initial_solution import *

num_size = 70
GAME_SPEED = 20

class Sudoku(tk.Canvas):
    def __init__(self):
        super().__init__(
            width=9*num_size, height=9*num_size, background="white", highlightthickness=0
        )

        self.grid = csv_to_list() #dictionary with current values
        self.create_grid()
        self.create_game()
        self.initial_grid = csv_to_list()
        
        self.position = (0,0)

        self.bind("<Button-1>", self.click)
        self.bind_all("<Key>", self.key_press)
        self.bind('<Button-3>', self.delete_cell)
        self.current_trial = (0,0)

        self.pack()

        self.after(GAME_SPEED, self.backtracking)

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
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    self.create_text((i+0.5)*num_size,(j+0.5)*num_size,text=str(grid[i][j]))    
                
    

    def click(self,event):

        self.delete('click_rectangle')
        
        self.position = (event.x//num_size, event.y//num_size)
        X,Y = self.position
        x,y = X*num_size, Y*num_size

        self.create_rectangle(x,y,x+num_size,y+num_size,outline='red',tag='click_rectangle')
        

    def key_press(self,event):
        numb = int(event.char)
        
        X,Y = self.position
        self.create_text((X+0.5)*num_size,(Y+0.5)*num_size,text=numb, fill='gray',tag='{}_{}'.format(X,Y)) 
        self.grid[X][Y] = numb
        print("(X,Y) added: correct =",is_correct(self.grid))
        


    def delete_cell(self,event):
        X,Y = self.position
               
        self.delete('{}_{}'.format(X,Y))
        self.grid[X][Y] = 0
        

    def delete_row(self):
        j = self.current_row
        for i in range(9):
            if self.initial_grid[i][j]==0:
                self.delete('{}_{}'.format(i,j))
                self.grid[i][j] = 0

    def delete_all(self):
        for j in range(9):
            for i in range(9):
                if self.initial_grid[i][j]==0:
                    self.delete('{}_{}'.format(i,j))
                    self.grid[i][j] = 0

    def add_row(self):
        j = self.current_row
        grid = self.grid
        new_line,is_added = line(j,grid.copy())
               
        for i in range(9):
            grid[i][j] = new_line[i]
            if is_added[i]:
                self.create_text((i+0.5)*num_size,(j+0.5)*num_size,text=str(grid[i][j]), fill='red', tag='{}_{}'.format(i,j))


    def new_trial(self):
        i,j = self.current_trial[:]
        while self.grid[i][j] != 0:
            i += 1
            if i>=9:
                i = 0
                j += 1
        
        self.current_trial = (i,j)

        new_numb = new_number(i,j,self.grid)
        self.grid[i][j] = new_numb
        print(self.grid[i][j])
        self.create_text((i+0.5)*num_size,(j+0.5)*num_size,text=str(self.grid[i][j]), fill='red', tag='{}_{}'.format(i,j))


        
       


    def backtracking(self):
        
        I,J = self.current_trial
        self.new_trial()
        


        if self.grid[I][J] == -1:
            self.delete_all()
            self.current_trial = (0,0)
        
        # if (I,J) == ()
        
            

        
        
        
        self.after(GAME_SPEED, self.backtracking)
        

        
        




root = tk.Tk()
root.title("Sudoku")
root.resizable(False, False)
root.tk.call("tk", "scaling", 4.0)

board = Sudoku()

root.mainloop()