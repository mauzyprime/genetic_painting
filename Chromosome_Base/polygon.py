class Polygon():
    def __init__(self, numVertices, myColor, vertexCoords):
        self.numVertices = numVertices #Int number of vertices the polygon has. Currently not used, may come in handy
        self.myColor = myColor #Color class object
        self.vertexCoords = vertexCoords #List: [[x1,y1],[x2,y2]...[xn,yn]]
        
    def display(self, pGraphics): #Display this polygon to a PGraphics object, which acts similar to a self-contained canvas
        s = createShape() #Create a custom shape using the vertexCoords array
        s.beginShape()
        s.fill(myColor)
        s.noStroke()
        for c in vertexCoords:
            s.vertex(c[0],c[1]) #Vertex at each coordinate
        s.endShape(CLOSE) #End the shape, join the first and last vertex, and fill in the shape
        
        pGraphics.beginDraw() #Draw the shape to the pGraphics object
        pGraphics.fill(myColor) #Not sure if the shape or the fill needs to be set to the polygon's color, so I'm setting them both
        pGraphics.noStroke()
        pGraphics.shape(s)
        pGraphics.endDraw()
        return(pGraphics)

class katieGit():
    def __init__(self, hello):
        self.message = hello
        