# for each of the images in Data, create a 3 guassian blurred way of the image
# same for changing the brightness of the image for slightly darker, much darker, slightly lighter, and much lighter

import cv2
import numpy as np
import os
from PIL import ImageEnhance, Image

# Path to the data
data_path = "Data"
# Path to the new data
new_data_path = "Data"

# load all the images in the data folder, save them in a list and return the list
def load_images():
    images = []
    images_filenames = []
    for filename in os.listdir(data_path):
        img = cv2.imread(os.path.join(data_path, filename))
        if img is not None:
            images.append(img)
            images_filenames.append(filename)
    return images, images_filenames

# perform a guassian blurr on the image
def guassian_blur(img):
    # create 3 guassian blurred images
    img1 = cv2.GaussianBlur(img, (5, 5), 0)
    img2 = cv2.GaussianBlur(img, (9, 9), 0)
    img3 = cv2.GaussianBlur(img, (13, 13), 0)
    img4 = cv2.GaussianBlur(img, (17, 17), 0)
    img5 = cv2.GaussianBlur(img, (21, 21), 0)
    img6 = cv2.GaussianBlur(img, (25, 25), 0)
    img7 = cv2.GaussianBlur(img, (29, 29), 0)
    img8 = cv2.GaussianBlur(img, (33, 33), 0)
    img9 = cv2.GaussianBlur(img, (37, 37), 0)

    # add all the images to a list
    images = [img1, img2, img3, img4, img5, img6, img7, img8, img9]

    return images


# show image
def show_image(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# from the list of images, save all of them to save path, which is new_path_data
def save_images(images, org_name):
    # keep the orignal image name + {number} + .jpg
    i = 0
    for img in images:
        cv2.imwrite(os.path.join(new_data_path, org_name + str(i) + ".jpg"), img)
        i += 1
    


# perform a brightness change on the image
def brightness(img_org):
    # convert the image to a PIL image
    img = Image.fromarray(img_org)
    # create a brightness enhancer
    enhancer = ImageEnhance.Brightness(img)
    # create 4 different brightness levels
    img1 = enhancer.enhance(0.5)
    img2 = enhancer.enhance(0.75)
    img3 = enhancer.enhance(1.25)
    img4 = enhancer.enhance(1.5)
    # convert the images back to a numpy array
    img1 = np.array(img1)
    img2 = np.array(img2)
    img3 = np.array(img3)
    img4 = np.array(img4)

    # add of the images to a list
    images = [img1, img2, img3, img4]

    return images


# pixelate the image
def pixelation(img):
    # get the height and width of the image
    h, w = img.shape[:2]
    
    # perform 5 different resizes, to vary pixelation, factor of 5, until /30
    img1 = cv2.resize(img, (w//3, h//3), interpolation=cv2.INTER_LINEAR)
    img2 = cv2.resize(img, (w//6, h//6), interpolation=cv2.INTER_LINEAR)
    img3 = cv2.resize(img, (w//9, h//9), interpolation=cv2.INTER_LINEAR)
    img4 = cv2.resize(img, (w//12, h//12), interpolation=cv2.INTER_LINEAR)
    img5 = cv2.resize(img, (w//15, h//15), interpolation=cv2.INTER_LINEAR)

    # resize the images back to the original size
    img1 = cv2.resize(img1, (w, h), interpolation=cv2.INTER_LINEAR)
    img2 = cv2.resize(img2, (w, h), interpolation=cv2.INTER_LINEAR)
    img3 = cv2.resize(img3, (w, h), interpolation=cv2.INTER_LINEAR)
    img4 = cv2.resize(img4, (w, h), interpolation=cv2.INTER_LINEAR)
    img5 = cv2.resize(img5, (w, h), interpolation=cv2.INTER_LINEAR)

    # add all the images to a list
    images = [img1, img2, img3, img4, img5]

    return images

# perform pixelation and then guassian
def pixelation_guassian(img):
    
    pixelated_images = pixelation(img)



    guassian_images = []
    for img in pixelated_images:
        guassian_images += guassian_blur(img)
    

    return guassian_images


# main function
def main():
    # load all the images
    images, filenames = load_images()

    counter = 0
    # for all the images, perform the guassian blur, brightness change, and save the images
    for img in images:
        guassian_images = guassian_blur(img)
        brightness_images = brightness(img)
        pixelation_images = pixelation(img)
        pixel_guass_images = pixelation_guassian(img)

        # get the name of the file and remove the .jpg
        name = filenames[counter].split(".")[0]
        # save the images
        save_images(guassian_images, name)
        save_images(brightness_images, name)
        save_images(pixelation_images, name)
        save_images(pixel_guass_images, name)

        counter += 1

if __name__ == "__main__":
    main()


       