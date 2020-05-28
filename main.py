#--IMPORTS----------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from canvasFunctions import createGrid,generateGridArray,displayGridArray

##------FUNCTIONS----------------------------------
def updateGridArray(x, y):
    global gridArray, targetCoord, targetCoordValue

    color = activeColor.get()
    if drawBool and not selectTargetBool and not fillBool:
        gridArray[x][y] = allColor.index(color)

    elif selectTargetBool and not drawBool and not fillBool:
        if targetCoord != [-1,-1]:
            prev_x,prev_y = targetCoord[0],targetCoord[1]
            gridArray[prev_x][prev_y] = targetCoordValue

        targetCoord[0],targetCoord[1] = x, y
        targetCoordValue = gridArray[x][y]


def getDragCoords(event):
    global gridArray
    x, y = event.x, event.y
    r, c = y // gridGap, x // gridGap

    if (r>=0 and r<gridRow) and (c>=0 and c<gridCol):
        updateGridArray(r,c)
        displayGridArray(gridCanvas, gridArray, gridRow, gridCol, gridGap, allColor, targetCoord, fillBool)


def resetCanvas():
    global gridArray,drawBool,fillBool,selectTargetBool,targetCoord
    drawBool = False
    fillBool = False
    selectTargetBool = False
    targetCoord = [-1,-1]
    gridCanvas.delete('square')
    gridCanvas.delete('target')
    gridArray = generateGridArray(gridRow,gridCol)


def drawCanvas():
    global drawBool,fillBool, selectTargetBool

    if activeColor.get() != '':
        drawBool = True
        fillBool = False
        selectTargetBool = False
    else:
        showinfo('Error','Select Color first!')


def selectTarget():
    global drawBool, fillBool, selectTargetBool

    if activeColor.get() != '':
        selectTargetBool = True
        drawBool = False
        fillBool = False
    else:
        showinfo('Error','Select Target Color first')


def fillCanvas():
    global drawBool, fillBool, selectTargetBool,targetCoord

    fillBool = True
    selectTargetBool = False
    drawBool = False

    if targetCoord != [-1,-1]:
        replacementColorValue = allColor.index(activeColor.get())
        floodFillAlgorithm(targetCoord, targetCoordValue,replacementColorValue)
        targetCoord = [-1,-1]
        fillBool = False
    else:
        showinfo('Error','Select Target Co-ordinates first!')


def floodFillAlgorithm(targetCoord, targetCoordValue, replacementColorValue):
    global gridArray,gridRow,gridCol
    displayGridArray(gridCanvas, gridArray, gridRow, gridCol, gridGap, allColor, targetCoord,fillBool)
    root.update()

    if replacementColorValue == targetCoordValue:
        return
    if (targetCoord[0]<0 or targetCoord[0]>=gridRow) or (targetCoord[1]<0 or targetCoord[1]>=gridCol):
        return
    if gridArray[targetCoord[0]][targetCoord[1]] != targetCoordValue:
        return

    gridArray[targetCoord[0]][targetCoord[1]] = replacementColorValue

    floodFillAlgorithm([targetCoord[0]-1, targetCoord[1]], targetCoordValue, replacementColorValue) #North
    floodFillAlgorithm([targetCoord[0], targetCoord[1]+1], targetCoordValue, replacementColorValue) #East
    floodFillAlgorithm([targetCoord[0], targetCoord[1]-1], targetCoordValue, replacementColorValue) #West
    floodFillAlgorithm([targetCoord[0]+1, targetCoord[1]], targetCoordValue, replacementColorValue) #South


#Driver Code--------------------------------------------------
if __name__ == '__main__':
    root = tk.Tk()
    root.config(bg='#80ffff')
    root.title('Flood-Fill Algorithm Visualizer')

    #GLOBAL VARIABLES-----------------------------------------
    gridWidth = 800
    gridHeight = 600
    gridGap = 20  # do not decrease from 20-> causes maximum recursion depth exceeded
    gridRow = gridHeight // gridGap
    gridCol = gridWidth // gridGap
    gridLineWidth = 1
    gridBorderWidth = 5
    canvasBGColor = 'white'
    targetCoord = [-1, -1]
    targetCoordValue = None
    drawBool = False
    selectTargetBool = False
    fillBool = False
    frameFont = ('Comic Sans MS', 12)
    activebg = '#00cc66'
    allColor = ('white', 'red', 'blue', 'yellow', 'orange', 'pink', 'black', 'green', 'brown')
    gridArray = generateGridArray(gridRow, gridCol)

    # -------USER INTERFACE-------INPUTS---------------------------------
    inputFrame = tk.Frame(root, width=gridWidth, height=gridHeight // 4, bg='#80ffff')
    inputFrame.pack()

    gridCanvas = tk.Canvas(root, bg=canvasBGColor, width=gridWidth, height=gridHeight)
    gridCanvas.pack()

    colorLabel = tk.Label(inputFrame, text='Choose Color ->', bg='black', fg='white', width=12, height=1, font=frameFont)
    colorLabel.grid(row=0, column=0, padx=5, pady=5)

    activeColor = ttk.Combobox(inputFrame, values=allColor, width=11, font=frameFont)
    activeColor.grid(row=0, column=1, padx=5, pady=5)
    activeColor.current()

    drawButton = tk.Button(inputFrame, text='Draw', width=12, bg='#66ff66', fg='black', command=drawCanvas, font=frameFont, activebackground=activebg)
    drawButton.grid(row=1, column=0, padx=5, pady=5)

    resetButton = tk.Button(inputFrame, text='Reset', width=12, bg='#66ff66', fg='black', command=resetCanvas, font=frameFont, activebackground=activebg)
    resetButton.grid(row=1, column=1, padx=5, pady=5)

    floodFillButton = tk.Button(inputFrame, text='Fill', width=12, bg='#66ff66', fg='black', command=fillCanvas, font=frameFont, activebackground=activebg)
    floodFillButton.grid(row=1, column=2, padx=5, pady=5)

    selectTargetButton = tk.Button(inputFrame, text='Select Target', width=12, height=1, bg='#66ff66', fg='black', command=selectTarget, font=frameFont, activebackground=activebg)
    selectTargetButton.grid(row=0, column=2, padx=5, pady=5)

    createGrid(gridCanvas, gridWidth, gridHeight, gridGap, gridBorderWidth, gridLineWidth)

    gridCanvas.bind('<B1-Motion>', getDragCoords)
    gridCanvas.bind('<Button-1>', getDragCoords)


    root.mainloop()
