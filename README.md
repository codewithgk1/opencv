# OpenCV Image Processing Project

This project demonstrates various image processing techniques using OpenCV in Python. It includes examples of basic image operations, drawing shapes, and image transformations.

## Project Structure

- `1_read.py`: Basic image and video reading operations
- `2_rescale.py`: Image rescaling functionality
- `3_draw.py`: Drawing shapes and text on images
- `4_basic.py`: Basic image processing operations
- `6_contours.py`: Contour detection and drawing
- `7_split_merge.py`: Color channel splitting and merging
- `Resources/`: Directory containing sample images and videos

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/codewithgk1/opencv.git
cd opencv
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Running the Project

Each Python file demonstrates different OpenCV operations. To run any example:

```bash
python <filename>.py
```

For example:
```bash
python 4_basic.py
```

## File Descriptions and Features

### 1_read.py
This file demonstrates basic image and video reading operations:
- **Image Reading**: Loads and displays an image using `cv.imread()` and `cv.imshow()`
- **Video Reading**: Contains commented code for reading and displaying video frames
- **Key Functions**: `cv.imread()`, `cv.imshow()`, `cv.VideoCapture()`, `cv.waitKey()`

### 2_rescale.py
This file implements image and video rescaling functionality:
- **Rescale Function**: Implements a `rescaleFrame()` function that resizes images and videos
- **Resolution Change**: Includes a `ChangeRes()` function for changing live video resolution
- **Multiple Scale Examples**: Demonstrates rescaling with different scale factors (0.20, 0.50, 0.75)
- **Key Functions**: `cv.resize()`, `cv.INTER_AREA` interpolation

### 3_draw.py
This file demonstrates drawing various shapes and text on images:
- **Blank Image Creation**: Creates a blank black image using NumPy
- **Color Painting**: Paints specific regions of the image with colors
- **Shape Drawing**: Draws rectangles, circles, and lines with different colors and thicknesses
- **Text Rendering**: Adds text to the image with custom font, size, and color
- **Key Functions**: `cv.rectangle()`, `cv.circle()`, `cv.line()`, `cv.putText()`

### 4_basic.py
This file demonstrates fundamental image processing operations:
- **Image Loading**: Loads a sample image of cats
- **Color Space Conversion**: Converts the image to grayscale
- **Blurring**: Applies Gaussian blur to reduce noise
- **Edge Detection**: Uses Canny edge detection to find edges in the image
- **Morphological Operations**:
  - Dilation: Expands the edges
  - Erosion: Shrinks the edges
- **Image Resizing**: Resizes the image to 500x500 pixels
- **Image Cropping**: Crops a specific region of the image
- **Key Functions**: `cv.cvtColor()`, `cv.GaussianBlur()`, `cv.Canny()`, `cv.dilate()`, `cv.erode()`, `cv.resize()`

### 6_contours.py
This file demonstrates contour detection and drawing:
- **Image Preprocessing**: Converts image to grayscale and applies Gaussian blur
- **Edge Detection**: Uses Canny edge detection to find edges
- **Thresholding**: Applies binary thresholding to create a binary image
- **Contour Detection**: Finds contours in the thresholded image
- **Contour Drawing**: Draws detected contours on a blank image
- **Key Functions**: `cv.threshold()`, `cv.findContours()`, `cv.drawContours()`

### 7_split_merge.py
This file demonstrates color channel manipulation:
- **Channel Splitting**: Splits an image into its BGR channels
- **Channel Visualization**: Creates separate images showing each color channel
- **Channel Merging**: Merges the channels back together to recreate the original image
- **Key Functions**: `cv.split()`, `cv.merge()`

## Key Features

- Basic image operations (read, display)
- Color space conversions
- Image filtering and blurring
- Edge detection
- Morphological operations (dilation, erosion)
- Image resizing and cropping
- Drawing shapes and text
- Video processing
- Contour detection and drawing
- Color channel manipulation

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy

## Resources

The project uses sample images and videos located in the `Resources` directory:
- `Resources/Photos/`: Contains sample images
- `Resources/Videos/`: Contains sample videos

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch
3. Making your changes
4. Submitting a pull request

## License

This project is open source and available under the MIT License. 