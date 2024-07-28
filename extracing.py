class Planet:
    def __init__(self, x, y, r):
        # x and y are the coordinates of the center of the circle
        self.x = x
        self.y = y
        self.r = r
        self.fileName = ""
        self.type = ""
    
    # create getter methods for the x, y, and r attributes
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getR(self):
        return self.r
    
    def setFileName(self, fileName):
        self.fileName = fileName
    
    def setType(self, type):
        self.type = type
    
    def returnPath(self):
        return self.fileName


# Separate planets from background
# Save the image with the planets separated from the background
# into folder called separatedPlanets[time]

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
    

def separate_planet(image_path, save_path, show=1):
    # Load the image
    # Replace with the actual path to your image
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

        
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and help circle detection
    gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    # Use Hough Circle Transform to detect circles
    circles = cv2.HoughCircles(
        gray_blurred,
        cv2.HOUGH_GRADIENT,
        dp=1,  # inverse ratio of the accumulator resolution
        minDist=100,  # minimum distance between the centers of detected circles
        param1=20,  # gradient value for edge detection
        param2=20,  # accumulator threshold for circle detection
        minRadius=60,  # minimum radius of the detected circle
        maxRadius=100,  # maximum radius of the detected circle
    )

    listOfPlanetObjects = []

    # If circles are found, draw them on the image
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
            # Need to create a new Planet object and save it to the list
            planet = Planet(i[0], i[1], i[2])
            planet.setFileName(fromPathGetFileName(image_path))
            listOfPlanetObjects.append(planet)
        
    else:
        print("No circles detected.")

    # show the image with the detected circles


    return listOfPlanetObjects

def fromPathGetFileName(path):
    return os.path.basename(path)


def cropImage(img):
        # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find contours in the image
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the maximum area (assuming it represents the planet)
    max_contour = max(contours, key=cv2.contourArea)

    # Create a mask for the planet using the maximum contour
    mask = np.zeros_like(gray)
    cv2.drawContours(mask, [max_contour], 0, 255, thickness=cv2.FILLED)

    # Bitwise AND operation to apply the mask to the original image
    result = cv2.bitwise_and(img, img, mask=mask)

    # Find the bounding box of the planet
    x, y, w, h = cv2.boundingRect(max_contour)

    # Crop the image to the bounding box
    cropped_image = result[y:y+h, x:x+w]

    # Resize the cropped image to your desired dimensions
    desired_size = (300, 300)  # specify the dimensions you want
    resized_image = cv2.resize(cropped_image, desired_size)


    return resized_image

# now a generic function
# it will, take the image path, the save path, and the planet object
# it will try to detect the planet in the image
# then it will remove the background and save the image to the save path
def planetDetection(input_path, output_path, flag=0):

    files = os.listdir(input_path)
    
    counter_outer = 0
    # Iterate over each file
    for file in files:
        counter_outer += 1

        # if counter is greater than 21 and flag is 1, break
        # if counter_outer > 21 and flag == 1:
        #     break
        # might be better to have many classifications for each planet
        
        file_path = os.path.join(input_path, file)

        listOfPlanetObjects = separate_planet(file_path, output_path, 1)

        counter = -1
        for planet in listOfPlanetObjects:
            counter += 1
            # read the image
            img = cv2.imread(file_path, cv2.IMREAD_COLOR)

            # create a mask
            mask = np.zeros(img.shape[:2], np.uint8)
            cv2.circle(mask, (planet.x, planet.y), planet.r, (255, 255, 255), -1)
            # apply the mask
            result = cv2.bitwise_and(img, img, mask=mask)
            # crop it
            result = cropImage(result)
            # save the image
            # change the output path to include a counter so that the images are not overwritten
            # it should look like Planets/[name of the image]_[counter].jpg
            # save the circular images in "Data/" folder with the name of the file being the planet it represents and the number (which is the default image name anyways) 

            # show result
            # cv2.imshow("Result", result)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            save_dir = "Data"
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            save_path = os.path.join(save_dir, file)
            cv2.imwrite(save_path, result)




# Usage example
earth_dir = "planets/Planets/Earth"
moon_dir = "planets/Planets/Moon"
# same but for now Jupiter, Mars, Mercury, Neptune, Pluto, Uranus, Venus
ju_dir = "planets/Planets/Jupiter"
mars_dir = "planets/Planets/Mars"
mercury_dir = "planets/Planets/Mercury"
neptune_dir = "planets/Planets/Neptune"
pluto_dir = "planets/Planets/Pluto"
uranus_dir = "planets/Planets/Uranus"
venus_dir = "planets/Planets/Venus"

# save path
save = "Data"


# use planetDectection on all input paths, same output path
planetDetection(earth_dir, save)
planetDetection(moon_dir, save)
planetDetection(ju_dir, save, 1)
planetDetection(mars_dir, save, 1)
planetDetection(mercury_dir, save,1)
planetDetection(neptune_dir, save, 1)
planetDetection(pluto_dir, save, 1)
planetDetection(uranus_dir, save, 1)
planetDetection(venus_dir, save, 1)
