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
    randomSeed(100)
    global chromosome1
    global originalImg
    originalImg = loadImage("monalisa.png")
    size(500,500)
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
    chromosome1.fitness(originalImg)
    
def draw():
    background(127)
    global chromosome1
    #print(chromosome1)
    image(chromosome1.display(), 0,0)
    
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
        self.pg.background(255)
        self.pg.endDraw()
        for i in self.polygonsArr:
            self.pg = i.display(self.pg)
        return self.pg
    def fitness(self, originalImage):
        #Nolan Wuz Here
        #original image is a PImage; chromosome is a PGraphics
        print len(originalImage.pixels) #this is 200 x 200. the mona lisa
        loadPixels()
        print len(pixels) #this then is the current canvas, 500 x 500. which we don't really care about. 
        #print len(self.pg.get().pixels)
        greenTotal = 0
        redTotal = 0
        blueTotal = 0
        #org = originalImage.loadPixels().pixels
        totalFitness = 0
       # if len(org) == len(self.pg.get().pixels):
        #    for i in  self.pg.get(pixels):
        #            greenTotal += green(org[i])-green(self.pg.get(pixels[i]))
        
        #            redTotal  += red(org[i])-red(self.pg.get(pixels[i]))
        #            blueTotal += blue(org[i])-blue(self.pg.get(pixels[i]))
        #            totalFitness += (redTotal * redTotal) + (blueTotal * blueTotal) + (greenTotal * greenTotal)            
       # else:
        #    print "lengths do not match. "
        return totalFitness  
        
