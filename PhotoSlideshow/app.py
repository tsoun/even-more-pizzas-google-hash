class Photo:
    def __init__ (self, photoID, orientation):
        self.photoID = photoID
        self.orientation = orientation
        self.tags = []
    
    def addTag (self, tag):
        self.tags.append(tag)

class Slide:
    def __init__ (self):
        self.photosContained = []
        self.allTags = []
    
    def addPhoto (self, photo):
        self.photosContained.append(photo)

    def findTags (self):
        if len(self.photosContained) == 1: # if slide contains only one photo
            self.allTags = self.photosContained[0].tags # the slide's tags are photo's tags
        else: # if slide contains two photos
            self.allTags = unite (self.photosContained[0].tags, self.photosContained[1].tags) # the slide's tags are the union of photo1's tags and photo2's tags

# The following part of code reads the data and stores them in the photosList

def inputData ():
    for i in range (numberOfPhotos):
        currentPhotoLine = inputFile.readline().split() # read current photo info
        currentPhoto = Photo(i, currentPhotoLine[0])
        photosList.append(currentPhoto) # create current photo, read orientation and append to memory
        for j in range (int(currentPhotoLine[1])): # for each tag
            currentPhoto.addTag(currentPhotoLine[j+2]) # append tag to current photo
        currentPhoto.tags.sort()

# all set

# The following part of code distributes photos to slides without any algorithm, just in the same order they appear at the input file

def distributePhotosToSlides ():
    semiFilledSlides = []
    for i in range (numberOfPhotos): # for each photo
        currentPhoto = photosList[i]
        if currentPhoto.orientation == "H": # if photo is horizontal
            createSlide(currentPhoto) # create a new slide and append photo
        else: # if photo is vertical
            if len(semiFilledSlides) == 0: # if there are no remaining semi-filled slides
                currentSlide = createSlide(currentPhoto) # create a new slide and append photo
                semiFilledSlides.append(currentSlide) # append slide to semi-filled slides
            else: # if there are remaining semi-filled slides
                currentSlide = semiFilledSlides.pop(0) # remove slide from semi-filled slides
                currentSlide.addPhoto(currentPhoto) # append photo

def createSlide (currentPhoto):
    currentSlide = Slide() # create a new slide
    slidesList.append(currentSlide) # append slide to slidesList
    currentSlide.addPhoto(currentPhoto) # add photo to slide
    return currentSlide

# all set

# The following part of code finds the tags of each slide (used in score calculation)

def findSlideTags ():
    for i in range (len(slidesList)): # for each slide
        slidesList[i].findTags() # find tags of current slide

# all set

# The following part of code stores data to output file in the specified format

def saveData ():
    howManySlides = len(slidesList)
    outputFile.write (str(howManySlides) + "\n") # write number of slides
    for i in range (howManySlides): # for each slide
        currentSlide = slidesList[i]
        outputFile.write (str(currentSlide.photosContained[0].photoID)) # write id of photo 1
        if (len(currentSlide.photosContained) == 2): # if slide contains two vertical photos
            outputFile.write (" " + str(currentSlide.photosContained[1].photoID)) # write id of photo 2 as well
        outputFile.write ("\n") # in any case, create a new line

# all set

# The following part of code calculates submission score (probably 3 balls)

def calculateScore ():
    score = 0
    for i in range (len(slidesList) - 1): # for each slide except final
        tagsOfCurrentSlide = slidesList[i].allTags
        tagsOfNextSlide = slidesList[i+1].allTags
        intersection = intersect (tagsOfCurrentSlide, tagsOfNextSlide)
        temp = min(len(in1AndNotIn2(tagsOfCurrentSlide, tagsOfNextSlide)), len(in1AndNotIn2(tagsOfNextSlide, tagsOfCurrentSlide)), len(intersection)) # find the minimum of
        #          tags of current slide that are not tags of the next slide, tags of current slide that are not tags of current slide, common tags of two slides
        score += temp # add to score
    return score

def unite (list1, list2):
    return list(set(list1) | set(list2)) 

def intersect (list1, list2):
    return list(set(list1) & set(list2))

def in1AndNotIn2 (list1, list2):
    return list(set(list1) - set(list2))

# all set

# main point

if __name__ == "__main__":
    inputFile = open("Ins\\a_example.txt", "rt")
    outputFile = open("Outs\\output.txt", "wt")
    photosList = [] # initialize photo memory
    slidesList = []
    numberOfPhotos = int(inputFile.readline())

    inputData()

    distributePhotosToSlides()
    findSlideTags()

    saveData()

    score = calculateScore()
    print(score)




# # good old debug

# # Debug data input (list all photos with their orientation and their tags)

# for i in range (numberOfPhotos):
#     thisPhoto = photosList[i]
#     howManyTags = len(thisPhoto.tags)
#     print("Photo #" + str(i) + " has " + thisPhoto.orientation + "orientation and " + str(howManyTags) + " tags, which are:")
#     for j in range (howManyTags):
#         print("- " + thisPhoto.tags[j])

# # Debug photo distribution (list all slides with their photos)

# numberOfSlides = len(slidesList)

# for i in range (numberOfSlides):
#     thisSlide = slidesList[i]
#     howManyPhotos = len(thisSlide.photosContained)
#     print("Slide #" + str(i) + " contains photos ", end='')
#     for j in range (howManyPhotos):
#         print(str(thisSlide.photosContained[j].photoID), end=' ')
#     print()

# # Debug slide tags (list all slides with their tags)

# for i in range (numberOfSlides):
#     thisSlide = slidesList[i]
#     print("Slide #" + str(i) + "\'s tags: ", end='')
#     for j in range (len(thisSlide.allTags)):
#         print(thisSlide.allTags[j], end=' ')
#     print()