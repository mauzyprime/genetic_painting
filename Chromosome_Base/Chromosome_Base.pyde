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
    #randomSeed(100)
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
    #the craziness below is what we used to test the functionality of the fitness funciton
    #chromosome1.display()
    #chromosome1.pg.beginDraw()
    #chromosome1.pg.endDraw()
   # chromosome1.pg.save("chromosome.png")
    #originalImg = loadImage("chromosome.png")
    #chromosome1.fitness(originalImg)
    
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
    def mutate(self):
        for i in range(len(polygonsArr)): #For every polygon in the image
            for i2 in range(len(polygonsArr[i].vertexCoords)):#for every vertex of a polygon
                polygonsArr[i].vertexCoords[i2][1] +=10 #add 10 to the y value of the vertex
        return 0#placeholder for now.
    
    
    def fitness(self, originalImage):
        #Nolan Wuz Here
        #original image is a PImage; chromosome is a PGraphics
        #print len(originalImage.pixels) #this is 200 x 200. the mona lisa
        self.display()
       # self.pg.endDraw()
        chro = self.pg.get().pixels
        greenTotal = 0
        redTotal = 0
        blueTotal = 0
        org = originalImage.pixels
        totalFitness = 0
        if len(org) == len(chro):
            for i in  range(len(chro)):
                    greenTotal += green(org[i])-green(chro[i])
                    redTotal  += red(org[i])-red(chro[i])
                    blueTotal += blue(org[i])-blue(chro[i])
                    totalFitness += (redTotal * redTotal) + (blueTotal * blueTotal) + (greenTotal * greenTotal)            
        else:
            print "lengths do not match. "
        print totalFitness
        return totalFitness  
        
