from polygon import Polygon
import copy


mrKVariable = 5
secondVariable = 10
willHolzmanHomeworkDone = 1
nolanVariable = sqrt(-64)
chromosome1 = None

numPolys = 50
numVertices = 4
originalImg = None


def setup():
    frameRate(0.5)
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
    chromosome2 = Chromosome(numPolys, numVertices, originalImg.height, originalImg.width)
    chromosome2.polygonsArr = chromosome1.polygonsArr
    chromosome2.mutatePercentChange()
    image(chromosome2.display(), 525, 25)
    if chromosome1.fitness(originalImg) > chromosome2.fitness(originalImg):
        chromosome1
    #chromosome1.mutatePercentChange()
    #chromosome1.mutateOnePoly()
    #chromosome1.mutatePosition()
    
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
    def mutatePercentChange(self):
        chanceMutate = .15
        for i in range(len(self.polygonsArr)): #For every polygon in the image
            for i2 in range(len(self.polygonsArr[i].vertexCoords)):#for every vertex of a polygon
                doesMutate = random(1)
                if doesMutate < chanceMutate:
                    self.polygonsArr[i].vertexCoords[i2][1] = random(self.pheight) #set y to random y
                    self.polygonsArr[i].vertexCoords[i2][0] = random(self.pwidth) #set x to random x
                    self.polygonsArr[i].myColor = color(random(255),random(255),random(255),random(255))
        return 0#placeholder for now.
    def mutatePosition(self): #changes every vertex of every polygon
        for i in range(len(self.polygonsArr)):
            for k in range(len(self.polygonsArr[i].vertexCoords)):
                blerg = random(1)
                glerg = random(1)
                if blerg < .5:
                    self.polygonsArr[i].vertexCoords[k][0] += 10 #changes x to something random
                else:
                    self.polygonsArr[i].vertexCoords[k][0] -= 10
                if glerg < .5:
                    self.polygonsArr[i].vertexCoords[k][1] += 10 #also changes y
                else:
                    self.polygonsArr[i].vertexCoords[k][1] -= 10 #also changes y
                    
    def megaMutate(self):
        #random number of polygons within the set
        #change position, color, or both, to a new random number (within a range)
        numberOfPolys = random(len(self.polygonsArr))
        for i in range(numberOfPolys):
            option = random(1)
            #in this current setup it is possible to mutate the same polygon twice oops
            chro = self.polygonsArr[random(len(self.polygonsArr))]
            #the below numbers can be fine-tuned to get a better result. 
            if option < .25:
                redthing = red(chro.myColor) + random(-30,30)
                bluething = blue(chro.myColor) + random(-30,30)
                greenthing = green(chro.myColor) + random(-30,30)
                alphathing = alpha(chro.myColor) + random(-30,30)
                chro.myColor = color(redthing,bluething,greenthing,alphathing)
                # only change color
            elif (option < .5):
                # only change position
                 for k in range(len(chro.vertexCoords)):
                    chro.vertexCoords[k][0] += random(-20,20) #changes x to something random
                    chro.vertexCoords[k][1] += random(-20,20) #also changes y
            else:
                #change both
                redthing = red(chro.myColor) + random(-30,30)
                bluething = blue(chro.myColor) + random(-30,30)
                greenthing = green(chro.myColor) + random(-30,30)
                alphathing = alpha(chro.myColor) + random(-30,30)
                chro.myColor = color(redthing,bluething,greenthing,alphathing)
                for k in range(len(chro.vertexCoords)):
                    chro.vertexCoords[k][0] += random(-20,20) #changes x to something random
                    chro.vertexCoords[k][1] += random(-20,20) #also changes y
    
    def mutateOnePoly(self):
        polygonChosen = int(random(len(self.polygonsArr)))
        Pred = red(self.polygonsArr[polygonChosen].myColor)
        Pblue = blue(self.polygonsArr[polygonChosen].myColor)
        Pgreen = green(self.polygonsArr[polygonChosen].myColor)
        Palpha = alpha(self.polygonsArr[polygonChosen].myColor)
        Pred = Pred +random(-25,25)
        Pblue = Pblue +random(-25,25)
        Pgreen = Pgreen + random(-25,25)
        Palpha = Palpha + random(-25,25)
        if Pred > 255:
            Pred = 255
        if Pred < 0:
            Pred = 0
        if Pblue >255:
            Pblue = 255
        if Pblue < 0:
            Pblue = 0
        if Pgreen > 255:
            Pgreen = 255
        if Pgreen < 0:
            Pgreen = 0
        if Palpha > 255:
            Palpha = 255
        if Palpha < 0:
            Palpha = 0
        self.polygonsArr[polygonChosen].myColor = color(Pred,Pgreen,Pblue,Palpha)
        for i2 in range(len(self.polygonsArr[polygonChosen].vertexCoords)):#for every vertex of a polygon
            self.polygonsArr[polygonChosen].vertexCoords[i2][1] += random(-25,25) #set y to random y
            self.polygonsArr[polygonChosen].vertexCoords[i2][0] += random(-25,25) #set x to random x
            if self.polygonsArr[polygonChosen].vertexCoords[i2][1] > self.pheight:
                self.polygonsArr[polygonChosen].vertexCoords[i2][1] = self.pheight
            if self.polygonsArr[polygonChosen].vertexCoords[i2][1] < 0:
                self.polygonsArr[polygonChosen].vertexCoords[i2][1] = 0
            if self.polygonsArr[polygonChosen].vertexCoords[i2][0] > self.pwidth:
                self.polygonsArr[polygonChosen].vertexCoords[i2][0] = self.pwidth
            if self.polygonsArr[polygonChosen].vertexCoords[i2][0] < 0:
                self.polygonsArr[polygonChosen].vertexCoords[i2][0] = 0
    def fitness(self, originalImage):
        #Nolan Wuz Here
        #original image is a PImage; chromosome is a PGraphics
        #pixel is a one dimensional array; dont panic
        self.display()
        chro = self.pg.get().pixels #gets access to the chromosome's pixel array
        greenTotal = 0
        redTotal = 0
        blueTotal = 0
        org = originalImage.pixels #.pixels is an accessible variable inside processing. 
        totalFitness = 0
        if len(org) == len(chro): #a check in case something goes wrong between the two images
            for i in  range(len(chro)):
                greenTotal += green(org[i])-green(chro[i])
                redTotal  += red(org[i])-red(chro[i])
                blueTotal += blue(org[i])-blue(chro[i])
                #finds delta
                totalFitness += (redTotal * redTotal) + (blueTotal * blueTotal) + (greenTotal * greenTotal)            
        else:
            print "lengths do not match. "
        print totalFitness
        return totalFitness  
        