# OpenCV Image Processing Project

This project demonstrates various image processing techniques using OpenCV in Python. It includes examples of basic image operations, drawing shapes, and image transformations.

## Project Structure

- `1_read.py`: Basic image and video reading operations
- `2_rescale.py`: Image rescaling functionality
- `3_draw.py`: Drawing shapes and text on images
- `4_basic.py`: Basic image processing operations
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

## Understanding 4_basic.py

`4_basic.py` demonstrates fundamental image processing operations using OpenCV:

1. **Image Loading**: Loads a sample image of cats
2. **Color Space Conversion**: Converts the image to grayscale
3. **Blurring**: Applies Gaussian blur to reduce noise
4. **Edge Detection**: Uses Canny edge detection to find edges in the image
5. **Morphological Operations**:
   - Dilation: Expands the edges
   - Erosion: Shrinks the edges
6. **Image Resizing**: Resizes the image to 500x500 pixels
7. **Image Cropping**: Crops a specific region of the image

The script includes commented lines for each operation. To see the effect of each operation, you can uncomment the corresponding `cv.imshow()` line.

## Key Features

- Basic image operations (read, display)
- Color space conversions
- Image filtering and blurring
- Edge detection
- Morphological operations (dilation, erosion)
- Image resizing and cropping
- Drawing shapes and text
- Video processing

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