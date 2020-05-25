
from canvasFunctions import createGrid,generateGridArray,displayGridArray
import tkinter as tk
from tkinter import ttk

##------FUNCTIONS----------------------------------
def updateGridArray(x,y):
    global gridArray, targetCoord, targetCoordValue

    color = activeColor.get()
    if drawBool==True and selectTargetBool==False and fillBool==False:
        gridArray[x][y] = allColor.index(color)+1


    elif selectTargetBool==True and drawBool==False and fillBool==False:

        if targetCoord != None:
            prev_x,prev_y = targetCoord
            gridArray[prev_x][prev_y] = targetCoordValue

        targetCoord = x, y
        targetCoordValue = gridArray[x][y]
        gridArray[x][y] = allColor.index(color) + 1



def getDragCoords(event):
    global gridArray
    x, y = event.x, event.y
    r, c = y // gridGap, x // gridGap
    print(r, c)
    if (r>=0 and r<gridRow) and (c>=0 and c<gridCol):

        updateGridArray(r,c)
        displayGridArray(gridCanvas,gridArray,gridGap,allColor)
    else:
        print("invalid")


def resetCanvas():
    global gridArray,drawBool,fillBool,selectTargetBool
    drawBool = False
    fillBool = False
    selectTargetBool = False
    gridCanvas.delete('square')
    gridArray = generateGridArray(gridRow,gridCol)

def drawCanvas():
    global drawBool,fillBool, selectTargetBool
    drawBool = True
    fillBool = False
    selectTargetBool = False

def selectTarget():
    global drawBool, fillBool, selectTargetBool
    selectTargetBool = True
    drawBool = False
    fillBool = False

def fillCanvas():
    global drawBool, fillBool, selectTargetBool
    fillBool = True
    selectTargetBool = False
    drawBool = False
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
targetCoord = None
targetCoordValue = None
drawBool = False
selectTargetBool = False
fillBool = False
frameFont = ('Comic Sans MS',12)
activebg = '#00cc66'
allColor = ('red','blue','yellow','orange','pink','black','green','brown','white')
gridArray = generateGridArray(gridRow,gridCol)


#-----  user interface ------inputs---------------------------------
inputFrame = tk.Frame(root,width = gridWidth,height = gridHeight//4,bg = '#80ffff')
inputFrame.pack()

gridCanvas = tk.Canvas(root,bg = canvasBGColor,width = gridWidth,height = gridHeight)
gridCanvas.pack()

colorLabel = tk.Label(inputFrame, text='Choose Color ->',bg='black', fg='white',width = 12,height=1, font=frameFont)
colorLabel.grid(row=0, column=0, padx = 5,pady = 5)

activeColor = ttk.Combobox(inputFrame, values=allColor,width=11,font=frameFont)
activeColor.grid(row=0, column=1,padx=5, pady=5)
activeColor.current()

drawButton = tk.Button(inputFrame,text='Draw',width=12,bg = '#66ff66',fg ='black',command=drawCanvas,font=frameFont,activebackground=activebg)
drawButton.grid(row=1, column=0,padx=5, pady=5)

resetButton = tk.Button(inputFrame,text='Reset',width=12,bg = '#66ff66',fg ='black',command=resetCanvas,font=frameFont,activebackground=activebg)
resetButton.grid(row=1, column=1,padx=5, pady=5)

floodFillButton = tk.Button(inputFrame,text='Fill',width=12,bg = '#66ff66',fg ='black',command=fillCanvas,font=frameFont,activebackground=activebg)
floodFillButton.grid(row=1, column=2,padx=5, pady=5)

selectTargetButton = tk.Button(inputFrame,text='Select Target',width=12,height=1,bg ='#66ff66',fg='black',command=selectTarget,font=frameFont,activebackground=activebg)
selectTargetButton.grid(row=0, column=2,padx=5, pady=5)

# target = tk.Label(inputFrame, text='target = ('+str(targetCoord[0])+', '+str(targetCoord[1])+')',bg='black', fg='white',width = 12,height = 1, font = ('Comic Sans MS',12))
# target.grid(row=0, column=3, padx = 5,pady = 5)
#-----


#----
createGrid(gridCanvas,gridWidth,gridHeight,gridGap,gridBorderWidth,gridLineWidth)

gridCanvas.bind('<B1-Motion>',getDragCoords)
gridCanvas.bind('<Button-1>',getDragCoords)

#----
root.mainloop()
