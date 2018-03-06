from polygon import Polygon
from copy import deepcopy
import csv


mrKVariable = 5
secondVariable = 10
willHolzmanHomeworkDone = 1
nolanVariable = sqrt(-64)
bestChromosome = None

initPop = 10
numChildrenPerGeneration = 4
populationArray = []
numPolys = 250
numVertices = 3
originalImg = None

numImprovements = 0.0
numMutations = 0.0

adata = createWriter("run.txt")
adata.print("currently working on riverdale.png\n")
adata.flush()
adata.close()


def setup():
    
    #frameRate(0.5)
    frameRate(100000000)
    #randomSeed(100)
    
    global bestChromosome
    global originalImg
    
    with open('data.csv','wb') as csvfile:
        writer = csv.writer(csvfile,delimiter=',')
    #originalImg = loadImage("monalisa.png")
    #originalImg = loadImage("chrome.png")
    originalImg = loadImage("riverdale.png")
    #originalImg = loadImage("xp_background.png")

    size(2200,700)
    #print mrKVariable
    bestChromosome = Chromosome(numPolys, numVertices, originalImg.height, originalImg.width)

    for i in range(initPop):
        #chromosome = None
        chromosome = Chromosome(numPolys, numVertices, originalImg.height, originalImg.width)
        populationArray.append(chromosome)

def draw():
    global originalImg
    global bestChromosome
    global numImprovements
    global numMutations
    global populationArray
    
    background(200)
    fill(0)
    
    #Write the text labels for the 3 images
    text("Original Image", 25, 20)
    #text("Current Chromosome", 275, 20)
    #text("Test Chromosome", 525, 20)
    
    
    #Draw the 3 images
    image(originalImg, 25, 25)
    #chromosome2 = Chromosome(numPolys, numVertices, originalImg.height, originalImg.width)
    #chromosome2.polygonsArr = deepcopy(chromosome1.polygonsArr)
    
    #chromosome2.mediumMutate()
    #chromosome2.mutatePercentChange()
    #chromosome2.megaMutate()
    #chromosome2.mutateOnePoly()
    #chromosome2.redrawPG()
    
    #image(chromosome2.pg, 525, 25)

    bestFitness = bestChromosome.fitness(originalImg)
    #fitness2 = chromosome2.fitness(originalImg)
    
    text("Best Chromosome", 250, 20)
    image(bestChromosome.pg, 250, 25)
    text("Fitness: "+str(int(bestFitness)), 250, 250)
    text("Digits: "+str(len(str(int(bestFitness)))), 250, 275)
    #drawChromosome(250, bestChromosome, bestFitness, "Best Chromosome")
    #drawChromosome(500, chromosome2, fitness2)
    position = 0
    for c in populationArray:
        c.mutateOnePoly()
        c.redrawPG()
        drawChromosome(position, c, c.fitness(originalImg))
        position = position + 210
    
    #text("Fitness: "+str(int(fitness1)), 275, 250)
    #text("Fitness: "+str(int(fitness2)), 525, 250)
    #text("Digits: "+str(len(str(int(fitness1)))), 275, 275)
    #text("Digits: "+str(len(str(int(fitness2)))), 525, 275)
    
    numMutations = numMutations+1
    
    #if bestFitness > fitness2:
        #chromosome1.polygonsArr = deepcopy(chromosome2.polygonsArr)
        #chromosome1.redrawPG()
        #numImprovements = numImprovements+1
        #writer.writerow(str(fitness1) + "," + str(fitness2) + "," + str(fitness1-fitness2)+ "," + str(numImprovements) +","+str(numMutations)+","+ str(100*(numImprovements/numMutations)))
        
    text("Mutations: "+str(numMutations), 775, 25)
    text("Improvements: "+str(numImprovements), 775, 50)
    pctImprovement = 100*(numImprovements/numMutations)
    text("Percent Improvement: "+str(pctImprovement), 775, 75)


def chooseOnePolyCrossover(parent1, parent2):
    global numPolys
    global numVertices
    global originalImg
    newPolysArr = []
    for i in numPolys/2:
        newPolysArr.append(parent1.polygonsArr[random(numPolys)])
        newPolysArr.append(parent2.polygonsArr[random(numPolys)])
    newChro = Chromosome(numPolys, numVertices, originalImg.height, originalImage.width)
    newChro.polygonsArr = newPolysArr
    newChro.redrawPG()
    return newChro
        

def bestSelection(populationArray):
    bestArray = []
    numberKept = 3
    for i in populationArray:
        bestArray.append(i.fitness(originalImg))
    bestArray.sort()
    return bestArray[:numberKept]

def drawChromosome(position, chromosome, fitness, topText=""):
    text(topText, position, 320)
    image(chromosome.pg, position, 325)
    text("Fitness: "+str(int(fitness)), position, 550)
    text("Digits: "+str(len(str(int(fitness)))), position, 575)



class Chromosome:
    def __init__(self, numPolys,numVertices,h,w):
        self.polygonsArr = []
        for i in range(numPolys):#creates the array of chromosomes
            verticesList = []
            for i in range(numVertices):
                verticesList.append([random(w),random(h)])
            #nPolygon = Polygon(numVertices, color(random(255),random(255),random(255),random(255)),verticesList)
            nPolygon = Polygon(numVertices, color(0,0,0,1),verticesList)
            self.polygonsArr.append(nPolygon)
        self.numVertices = numVertices
        self.numPolygons = numPolys
        self.pheight = h#height
        self.pwidth = w#width
        self.myFitness = 0
        self.pg = createGraphics(w,h)
        self.redrawPG()
        
    def __cmp__(self, other): #This is a manually defined function that is used by the built-in sorted() function
        if self.myFitness > other.myFitness:
            return 1
        elif self.myFitness < other.myFitness:
            return -1
        else:
            return 0
        
    def redrawPG(self):
        self.pg.beginDraw()
        self.pg.background(255)
        self.pg.endDraw()
        for i in self.polygonsArr:
            self.pg = i.display(self.pg)
        return self.pg
    
    def mediumMutate(self):
        poly = self.polygonsArr[int(random(len(self.polygonsArr)))]
        option = random(1)
        redthing = int(random(0,255))
        bluething = int(random(0,255))
        greenthing = int(random(0,255))
        alphathing = int(random(0,255))
        if option < .25:
            poly.myColor = color(redthing,blue(poly.myColor),green(poly.myColor),alpha(poly.myColor))
        elif option < .5:
            poly.myColor = color(red(poly.myColor),bluething,green(poly.myColor),alpha(poly.myColor))
        elif option < .75:
            poly.myColor = color(red(poly.myColor),blue(poly.myColor),greenthing,alpha(poly.myColor))
        else:
            poly.myColor = color(red(poly.myColor),blue(poly.myColor),green(poly.myColor),alphathing)
        vertex1 = int(random(len(poly.vertexCoords)))
        poly.vertexCoords[vertex1][0] = int(random(0,200))
        poly.vertexCoords[vertex1][1] = int(random(0,200))
        
    def mutatePercentChange(self):
        chanceMutate = .002
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
        for i in range(int(numberOfPolys)):
            option = random(1)
            #in this current setup it is possible to mutate the same polygon twice oops
            chro = self.polygonsArr[int(random(len(self.polygonsArr)))]
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
        Pred = Pred +random(-120,120)
        Pblue = Pblue +random(-120,120)
        Pgreen = Pgreen + random(-120,120)
        Palpha = Palpha + random(-120,120)
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
            self.polygonsArr[polygonChosen].vertexCoords[i2][1] += random(-100,100) #set y to random y
            self.polygonsArr[polygonChosen].vertexCoords[i2][0] += random(-100,100) #set x to random x
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
        #self.display()
        chro = self.pg.get().pixels #gets access to the chromosome's pixel array
        greenTotal = 0
        redTotal = 0
        blueTotal = 0
        org = originalImage.pixels #.pixels is an accessible variable inside processing. 
        totalFitness = 0
        if len(org) == len(chro): #a check in case something goes wrong between the two images
            for i in  range(len(chro)):
                greenTotal += abs(green(org[i])-green(chro[i]))
                redTotal  += abs(red(org[i])-red(chro[i]))
                blueTotal += abs(blue(org[i])-blue(chro[i]))
                #finds delta
                totalFitness += sqrt((redTotal * redTotal) + (blueTotal * blueTotal) + (greenTotal * greenTotal))            
        else:
            print "lengths do not match. "
        print totalFitness
        self.myFitness = totalFitness
        return totalFitness  
        