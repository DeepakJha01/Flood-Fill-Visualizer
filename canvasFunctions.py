import time

def createGrid(gridCanvas,gridWidth,gridHeight,gridGap,gridBorderWidth,gridLineWidth):
    #--create horizontal lines
    gridCanvas.create_line(0,0,gridWidth,0,width = gridBorderWidth)
    gridCanvas.create_line(0,gridHeight,gridWidth,gridHeight,width = gridBorderWidth)
    for y in range(0,gridHeight,gridGap):
        gridCanvas.create_line(0,y,gridWidth,y,width = gridLineWidth)

    #--create vertical lines
    gridCanvas.create_line(0,0,0,gridHeight,width = gridBorderWidth)
    gridCanvas.create_line(gridWidth,0,gridWidth,gridHeight,width = gridBorderWidth)
    for x in range(0,gridWidth,gridGap):
        gridCanvas.create_line(x,0,x,gridHeight,width = gridLineWidth)



def generateGridArray(row,col):
    arr = []
    for _ in range(row):
        arr.append([0]*col)
    return arr


def displayGridArray(gridCanvas,gridArray,gridGap,allColor,targetCoord):
    gridCanvas.delete('square')
    gridCanvas.delete('target')
    # print('.....START...inside display....')
    for r in range(len(gridArray)):
        for c in range(len(gridArray[0])):
            if gridArray[r][c] !=0:
                gridCanvas.create_rectangle(c*gridGap,r*gridGap,c*gridGap +gridGap,r*gridGap +gridGap,tag = 'square',fill = allColor[gridArray[r][c]])
    if targetCoord != [-1,-1]:
        c = targetCoord[1]
        r = targetCoord[0]
        gridCanvas.create_rectangle(c*gridGap,r*gridGap,c*gridGap +gridGap,r*gridGap +gridGap,tag='target',width = 5,outline='#cc33ff')
    # print('.....END...inside display....')
