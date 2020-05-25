
from canvasFunctions import createGrid,generateGridArray
import tkinter as tk
from tkinter import ttk

##------FUNCTIONS----------------------------------
def updateGridArray(x,y):
    global gridArray

    if activeColor.get()=='red':
        gridArray[x][y] = 1
    elif activeColor.get()=='blue':
        gridArray[x][y] = 2
    elif activeColor.get()=='yellow':
        gridArray[x][y] = 3
    elif activeColor.get()=='orange':
        gridArray[x][y] = 4
    elif activeColor.get()=='pink':
        gridArray[x][y] = 5
    elif activeColor.get()=='black':
        gridArray[x][y] = 6
    elif activeColor.get()=='green':
        gridArray[x][y] = 7
    elif activeColor.get()=='brown':
        gridArray[x][y] = 8
    elif activeColor.get()=='white':
        gridArray[x][y] = 9

def displayGridArray():
    gridCanvas.delete('square')
    for r in range(len(gridArray)):
        for c in range(len(gridArray[0])):
            if gridArray[r][c] !=0:
                gridCanvas.create_rectangle(c*gridGap,r*gridGap,c*gridGap +gridGap,r*gridGap +gridGap,tag = 'square',fill = allColor[gridArray[r][c]-1])


def getDragCoords(event):
    global gridArray
    x, y = event.x, event.y
    r, c = y // gridGap, x // gridGap
    print(r, c)
    if (r>=0 and r<gridRow) and (c>=0 and c<gridCol):

        updateGridArray(r,c)
        displayGridArray()
    else:
        print("invalid")


def resetCanvas():
    global gridArray
    gridCanvas.delete('square')
    gridArray = generateGridArray(gridRow,gridCol)


###-----------------------------------------------------------------------------------


root = tk.Tk()
root.config(bg='#80ffff')

gridWidth = 800
gridHeight = 600
gridGap = 20
gridRow = gridHeight//gridGap
gridCol = gridWidth//gridGap
gridLineWidth = 1
gridBorderWidth = 5
canvasBGColor = 'white'
allColor = ('red','blue','yellow','orange','pink','black','green','brown','white')
gridArray = generateGridArray(gridRow,gridCol)


#-----  user interface ------inputs---------------------------------
inputFrame = tk.Frame(root,width = gridWidth,height = gridHeight//4,bg = '#80ffff')
inputFrame.pack()

gridCanvas = tk.Canvas(root,bg = canvasBGColor,width = gridWidth,height = gridHeight)
gridCanvas.pack()

colorLabel = tk.Label(inputFrame, text='Choose Color ->',bg='black', fg='white',width = 12,height = 1, font = ('Comic Sans MS',12))
colorLabel.grid(row=0, column=0, padx = 5,pady = 5)

activeColor = ttk.Combobox(inputFrame, values=allColor,width=11, font = ('Comic Sans MS',12))
activeColor.grid(row=0, column=1,padx=5, pady=5)
activeColor.current()

resetButton = tk.Button(inputFrame,text = 'Reset',width = 12,bg = 'blue',fg = 'white',command = resetCanvas, font = ('Comic Sans MS',12))
resetButton.grid(row=1, column=0,padx=5, pady=5)

floodFillButton = tk.Button(inputFrame,text='Fill',width = 12,bg = 'blue',fg = 'white',command = '', font = ('Comic Sans MS',12))
floodFillButton.grid(row=1, column=1,padx=5, pady=5)

selectTargetButton = tk.Button(inputFrame,text='Select Target',width = 12,bg = 'blue',fg = 'white',command = '', font = ('Comic Sans MS',12))
selectTargetButton.grid(row=0, column=2,padx=5, pady=5,rowspan=2)
#-----


#----
createGrid(gridCanvas,gridWidth,gridHeight,gridGap,gridBorderWidth,gridLineWidth)

gridCanvas.bind('<B1-Motion>',getDragCoords)
gridCanvas.bind('<Button-1>',getDragCoords)

#----
root.mainloop()
