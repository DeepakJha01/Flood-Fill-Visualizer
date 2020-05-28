import time

max_time = 0.25

def createGrid(gridCanvas, gridWidth, gridHeight, gridGap, gridBorderWidth, gridLineWidth):

    #--create horizontal lines
    gridCanvas.create_line(0, 0, gridWidth, 0, width = gridBorderWidth)
    gridCanvas.create_line(0, gridHeight, gridWidth, gridHeight, width = gridBorderWidth)
    for y in range(0, gridHeight, gridGap):
        gridCanvas.create_line(0, y, gridWidth, y, width = gridLineWidth)

    #--create vertical lines
    gridCanvas.create_line(0, 0, 0, gridHeight, width = gridBorderWidth)
    gridCanvas.create_line(gridWidth, 0, gridWidth, gridHeight, width = gridBorderWidth)
    for x in range(0, gridWidth, gridGap):
        gridCanvas.create_line(x, 0, x, gridHeight, width = gridLineWidth)


def generateGridArray(row, col):
    arr = []
    for _ in range(row):
        arr.append([0]*col)
    return arr


def displayGridArray(gridCanvas,gridArray,gridRow,gridCol,gridGap,allColor,targetCoord,fillBool,sleepTime):
    gridCanvas.delete('square')     #to delete all previous rectangles
    gridCanvas.delete('target')     #to delete previous target grid boundary

    for r in range(gridRow):
        for c in range(gridCol):
            if gridArray[r][c] !=0:
                gridCanvas.create_rectangle(c*gridGap,r*gridGap,c*gridGap +gridGap,r*gridGap +gridGap,tag = 'square',
                                            fill = allColor[gridArray[r][c]-1])

    if targetCoord != [-1,-1]:
        c = targetCoord[1]
        r = targetCoord[0]
        gridCanvas.create_rectangle(c*gridGap,r*gridGap,c*gridGap +gridGap,r*gridGap +gridGap,tag='target',width = 5,
                                    outline='#cc33ff')

    if fillBool:
        time.sleep(max_time - (sleepTime*max_time/100))
