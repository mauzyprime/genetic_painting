from polygon import Polygon

mrKVariable = 5
secondVariable = 10
willHolzmanHomeworkDone = 1
nolanVariable = sqrt(-64)
chromosome1 = None

numPolys = 50
numVertices = 4
originalImg = None


def setup():
    global chromosome1
    global originalImg
    originalImg = loadImage("monalisa.png")
    size(1000,500)
    #print mrKVariable
    
    chromosome1 = Chromosome(numPolys, numVertices, originalImg.height, originalImg.width)

    # pg = createGraphics(10,10)
    # pg.beginDraw()
    # pg.background(12,123,234)
    # pg.endDraw()
    
    # img = createImage(10,10,RGB)
    # pg.loadPixels()
    # println(img)
    # println(img.pixels)
    # println(pg)
    # println(pg.get())
    #println(pg.get().pixels)
    #for i in pg.get().pixels:
        #print(red(i))
        #print(blue(i))
        #print(green(i))
        #println("")
    #image(img,0,0)
    #pix = pg.get().pixels
    #for i in pix:
        #i = color(127,127,127,127)
    #println(pix)
def draw():
    global originalImg
    global chromosome1
    
    background(255)
    fill(0)
    
    #Write the text labels for the 3 images
    text("Original Image", 25, 20)
    text("Current Chromosome", 275, 20)
    text("Stand-in Same Chromosome", 525, 20)
    
    #Draw the 3 images
    image(originalImg, 25, 25)
    image(chromosome1.display(), 275, 25)
    image(chromosome1.display(), 525, 25)
    
class Chromosome:
    def __init__(self, numPolys,numVertices,h,w):
        self.polygonsArr = []
        for i in range(numPolys):#creates the array of chromosomes
            verticesList = []
            for i in range(numVertices):
                verticesList.append([random(w),random(h)])
            nPolygon = Polygon(numVertices, color(random(255),random(255),random(255),random(255)),verticesList)
            self.polygonsArr.append(nPolygon)
        self.numVertices = numVertices
        self.numPolygons = numPolys
        self.pheight = h#height
        self.pwidth = w#width
        self.pg = createGraphics(w,h)
        
    def display(self):
        self.pg.beginDraw()
        self.pg.background(0)
        self.pg.endDraw()
        for i in self.polygonsArr:
            self.pg = i.display(self.pg)
        return self.pg
    def fitness(self, originalImage):
        #Nolan Wuz Here
        greenTotal = 0
        redTotal = 0
        blueTotal = 0
        org = originalImage.loadPixels().pixels
        for i in  self.pg.get(pixels):
            for j in self.pg.get(pixels[i]):
                greenTotal += green(org[i][j])-green(pixels[i][j])
                redTotal  += red(org[i][j])-red(pixels[i][j])
                blueTotal += blue(org[i][j])-blue(pixels[i][j])
            
            
        
        