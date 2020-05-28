#--IMPORTS----------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from canvasFunctions import createGrid,generateGridArray,displayGridArray

##------FUNCTIONS----------------------------------
def updateGridArray(x, y):
    global gridArray, targetCoord, targetCoordValue

    color = activeColor.get()
    if drawBool and not selectTargetBool and not fillBool and not eraseBool:
        if activeColor.get() in allColor:
            gridArray[x][y] = allColor.index(color)+1

    elif selectTargetBool and not drawBool and not fillBool and not eraseBool:
        if targetCoord != [-1,-1]:
            prev_x,prev_y = targetCoord[0],targetCoord[1]
            gridArray[prev_x][prev_y] = targetCoordValue

        targetCoord[0],targetCoord[1] = x, y
        targetCoordValue = gridArray[x][y]

    elif eraseBool and not drawBool and not selectTargetBool and not fillBool:
        gridArray[x][y] = 0

def getDragCoords(event):
    global gridArray
    x, y = event.x, event.y
    r, c = y // gridGap, x // gridGap

    if (r>=0 and r<gridRow) and (c>=0 and c<gridCol):
        updateGridArray(r,c)
        displayGridArray(gridCanvas, gridArray, gridRow, gridCol, gridGap, allColor, targetCoord, fillBool,speedInput.get())


def resetCanvas():
    global gridArray,drawBool,fillBool,selectTargetBool,targetCoord,eraseBool
    drawBool,fillBool,eraseBool,selectTargetBool = True,False,False,False
    targetCoord = [-1,-1]
    gridCanvas.delete('square')
    gridCanvas.delete('target')
    gridArray = generateGridArray(gridRow,gridCol)


def drawCanvas():
    global drawBool,fillBool, selectTargetBool, eraseBool

    if activeColor.get() in allColor:
        drawBool = True
        fillBool, eraseBool, selectTargetBool = False, False, False
    else:
        showinfo('Error','Select Color first!')


def eraseCanvas():
    global drawBool,fillBool,selectTargetBool,eraseBool
    eraseBool = True
    fillBool,selectTargetBool,drawBool = False,False,False


def selectTarget():
    global drawBool, fillBool, selectTargetBool,eraseBool

    if activeColor.get() in allColor:
        selectTargetBool = True
        drawBool, fillBool, eraseBool = False, False, False
    else:
        showinfo('Error','Select Target Color first')


def fillCanvas():
    global drawBool, fillBool, selectTargetBool,targetCoord, eraseBool
    fillBool = True
    drawBool, eraseBool, selectTargetBool = False, False, False

    if targetCoord != [-1,-1]:
        replacementColorValue = allColor.index(activeColor.get())+1
        floodFillAlgorithm(targetCoord, targetCoordValue,replacementColorValue)
        targetCoord = [-1,-1]
        fillBool,drawBool = False,True
    else:
        showinfo('Error','Select Target Co-ordinates first!')


def floodFillAlgorithm(targetCoord, targetCoordValue, replacementColorValue):
    global gridArray,gridRow,gridCol
    displayGridArray(gridCanvas, gridArray, gridRow, gridCol, gridGap, allColor, targetCoord,fillBool,speedInput.get())
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
    root.config(bg='#000066',width=850,height=630)
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
    drawBool, fillBool, eraseBool, selectTargetBool = True, False, False, False
    frameFont = ('Comic Sans MS', 14)
    activebg = '#00cc66'
    allColor = ('red', 'blue', 'yellow', 'orange', 'pink', 'black', 'green', 'brown')
    gridArray = generateGridArray(gridRow, gridCol)

    # -------USER INTERFACE-------INPUTS---------------------------------
    inputFrame = tk.Frame(root, width=gridWidth, height=gridHeight // 4, bg='#000066')
    inputFrame.pack()

    gridCanvas = tk.Canvas(root, bg=canvasBGColor, width=gridWidth, height=gridHeight)
    gridCanvas.pack(padx=10,pady=5)

    colorLabel = tk.Label(inputFrame, text='Choose Color ->', bg='black', fg='white', width=14, height=1, font=frameFont)
    colorLabel.grid(row=0, column=0, padx=5, pady=3)

    activeColor = ttk.Combobox(inputFrame, values=allColor, width=11, font=frameFont)
    activeColor.grid(row=0, column=1, padx=5, pady=3)
    activeColor.current()

    BucketImage = tk.PhotoImage(file='images/bucket.png')
    BucketImage = BucketImage.subsample(10, 10)
    floodFillButton = tk.Button(inputFrame, text='Fill', image=BucketImage, compound='top', width=100,height=90,
                                bg='#66ff66',fg='black',command=fillCanvas, font=frameFont, activebackground=activebg)
    floodFillButton.grid(row=0, column=2, padx=5, pady=3, rowspan=2)

    targetImage = tk.PhotoImage(file='images/target.png')
    targetImage = targetImage.subsample(10, 10)
    selectTargetButton = tk.Button(inputFrame, text='Select Target', image=targetImage, compound='top', width=150,
                                   height = 90,bg='#66ff66',fg='black', command=selectTarget, font=frameFont,activebackground=activebg)
    selectTargetButton.grid(row=0, column=3, padx=5, pady=3,rowspan=2)

    drawImage = tk.PhotoImage(file='images/pen.png')
    drawImage = drawImage.subsample(15,15)
    drawButton = tk.Button(inputFrame, text='Draw',image = drawImage,compound = 'left', width=150, bg='#66ff66', fg='black',
                           command=drawCanvas,font=frameFont, activebackground=activebg)
    drawButton.grid(row=1, column=0, padx=5, pady=3)

    eraserImage = tk.PhotoImage(file='images/eraser.png')
    eraserImage = eraserImage.subsample(15, 15)
    eraserButton = tk.Button(inputFrame, text='Erase', image=eraserImage, compound='left', width=150, bg='#66ff66',fg='black',
                             command=eraseCanvas,font=frameFont, activebackground=activebg)
    eraserButton.grid(row=1, column=1, padx=5, pady=3)

    speedInput = tk.Scale(inputFrame, from_=0, to=100, resolution=1, length=450, orient='horizontal',label='Visualization Speed',
                          bg='#66ff66',activebackground='black')
    speedInput.grid(row=2, column=0, padx=5, pady=3, columnspan=3)
    speedInput.set(90)

    resetImage = tk.PhotoImage(file='images/reset.png')
    resetImage = resetImage.subsample(15, 15)
    resetButton = tk.Button(inputFrame, text='Reset', image=resetImage, compound='left', width=150,height=50, bg='#ff0066',fg='black',
                            command=resetCanvas, font=frameFont, activebackground=activebg)
    resetButton.grid(row=2, column=3, padx=5, pady=3)

    createGrid(gridCanvas, gridWidth, gridHeight, gridGap, gridBorderWidth, gridLineWidth)

    gridCanvas.bind('<B1-Motion>', getDragCoords)
    gridCanvas.bind('<Button-1>', getDragCoords)


    root.mainloop()
