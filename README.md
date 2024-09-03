# Planet Detection and Background Removal

This project provides a set of Python scripts designed to detect planets in images, remove the background, and save the processed images. The planets in the images are assumed to be circular with a black background. The scripts utilize OpenCV for image processing tasks such as circle detection, masking, and cropping.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Usage](#usage)
    - [separate_planet Function](#separate_planet-function)
    - [cropImage Function](#cropImage-function)
    - [planetDetection Function](#planetDetection-function)
4. [Example](#example)
5. [Notes](#notes)
6. [License](#license)

## Project Structure

- `extracting.py`: Main script containing the functions for detecting planets, removing backgrounds, and saving processed images.
- `extracting.ipynb`: Jupyter Notebook for testing and running the image processing pipeline interactively.
- `Data/`: Directory where the processed images are saved.
- `planets/`: Directory containing subdirectories with images of different planets.

## Prerequisites

Before running the scripts, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib (optional, for visualization)

You can install the required packages using pip:

```bash
pip install opencv-python-headless numpy matplotlib
```

## Usage

### `separate_planet` Function

This function detects planets (circular objects) in an image and returns a list of `Planet` objects containing the coordinates and radius of each detected planet.

**Parameters:**

- `image_path` (str): Path to the input image.
- `save_path` (str): Path where the processed image will be saved.
- `show` (int, optional): If set to 1, displays the image with detected circles.

**Returns:**

- `listOfPlanetObjects` (list): List of `Planet` objects containing information about detected planets.

### `cropImage` Function

This function crops the image around the detected planet, removing the background.

**Parameters:**

- `img` (ndarray): Image array.

**Returns:**

- `resized_image` (ndarray): Cropped and resized image of the planet.

### `planetDetection` Function

This function detects planets in a directory of images, removes the background, and saves the processed images.

**Parameters:**

- `input_path` (str): Directory containing images to be processed.
- `output_path` (str): Directory where the processed images will be saved.
- `flag` (int, optional): If set to 1, limits the number of processed images to 21.

### `Planet` Class

A simple class representing a planet with attributes:

- `x`: X-coordinate of the planet's center.
- `y`: Y-coordinate of the planet's center.
- `r`: Radius of the planet.
- `fileName`: Name of the file containing the planet's image.
- `type`: Type of planet (optional, not utilized in the scripts).

## Example

To run the scripts and process images, use the following example code:

```python
# Define directories
earth_dir = "planets/Planets/Earth"
moon_dir = "planets/Planets/Moon"
save_dir = "Data"

# Process images
planetDetection(earth_dir, save_dir)
planetDetection(moon_dir, save_dir)
```

This will process the images in the specified directories and save the results in the `Data/` directory.

## Notes

- The script is designed to work with images of planets that are circular and have a black background.
- The `flag` parameter in `planetDetection` is used to limit the number of processed images to avoid processing too many images at once.
- The processed images are saved in the `Data/` directory with the same name as the input image.

### How It Works

This project is designed to automate the process of detecting, isolating, and saving images of planets from a collection of astronomical images. Below is an explanation of how the process works:

1. **Image Loading and Preprocessing**:
   - The script begins by loading the images from a specified directory using the `cv2.imread()` function from OpenCV. These images are expected to be photographs of planets on a black background.
   - Each loaded image is converted to grayscale using `cv2.cvtColor()`. This simplifies the image data, making it easier to detect circular shapes that represent planets.

2. **Planet Detection**:
   - The Hough Circle Transform (`cv2.HoughCircles()`) is employed to detect circles in the grayscale image. This method is particularly effective for detecting circular shapes, such as planets, by identifying their centers and radii.
   - Detected circles are used to create instances of the `Planet` class, which stores the circle's coordinates (`x`, `y`) and radius (`r`). These `Planet` objects are stored in a list for further processing.

3. **Background Removal**:
   - For each detected planet, a mask is created using the circle's coordinates and radius. This mask is then applied to the original image to isolate the planet from its background. The black background is removed, leaving only the circular planet in the image.
   - The script also detects the contours of the planet and crops the image to fit tightly around the detected planet, further refining the output.

4. **Saving the Results**:
   - The isolated planet images are saved in the `Data` directory. The images are saved with filenames that correspond to the original input files, and they are organized into subdirectories named after each planet.
   - If multiple planets are detected in a single image, each one is saved separately with a unique identifier in the filename.

5. **Batch Processing**:
   - The `planetDetection()` function is used to process all images within a specified directory. This function iterates over all image files, applies the detection and isolation steps, and saves the results automatically.
   - A flag parameter can be used to limit the number of images processed for certain planets, which is useful for large datasets where only a subset of images is needed.

This process allows for efficient and automated extraction of planetary images, facilitating further analysis or use in educational materials, presentations, or other projects.
