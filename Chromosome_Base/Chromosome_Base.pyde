from polygon import Polygon

mrKVariable = 5
secondVariable = 10
nolanVariable = sqrt(-16)

def setup():
    size(100,100)
    print mrKVariable
    pg = createGraphics(10,10)
    pg.beginDraw()
    pg.background(12,123,234)
    pg.endDraw()
    
    img = createImage(10,10,RGB)
    pg.loadPixels()
    println(img)
    println(img.pixels)
    println(pg)
    println(pg.get())
    #println(pg.get().pixels)
    for i in pg.get().pixels:
        print(red(i))
        print(blue(i))
        print(green(i))
        println("")
    image(img,0,0)
    #pix = pg.get().pixels
    #for i in pix:
        #i = color(127,127,127,127)
    #println(pix)
def draw():
    pass
    
    
class Chromosome:
    def _init_(polygons,vertices,h,w):
        for i in range(polygons):#creates the array of chromosomes
            verticesList = []
            for i in range(vertices):
                verticesList.append([random(w),random(h)])
            nPolygon = Polygon(vertices, color(random(255),random(255),random(255),random(255)),verticesList)
            polygonsArr.append(nPolygon)
        self.numVertices = vertices
        self.numPolygons = polygons
        self.pheight = h#height
        self.pwidth = w#width
        
    def display(pGraphics):
        for i in polygonsArr:
            #i.display(pGraphics)
            print "CHECK"
    def fitness(myPGraphics,originalImage):
        pass