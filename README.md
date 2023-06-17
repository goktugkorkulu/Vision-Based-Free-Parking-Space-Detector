# Vision Based Free Parking Space Detector

The Free Parking Space Detector is a computer vision-based system that detects and counts the number of free parking spaces in a parking lot. It utilizes the OpenCV library and an object detection algorithm to analyze live or recorded video footage from a bird's eye view perspective.

## Features

- Real-time detection and counting of free parking spaces
- Easy setup and configuration
- Adjustable threshold for detection accuracy

## Requirements

- Python 3.7 or later
- OpenCV
- cvzone
- NumPy

## Files and Detailed Descriptions

### FreeSpaceFinder.py
This file is responsible for selecting and storing the coordinates of parking spaces.

> #### Step 1
> The required packages, `cv2` and `pickle`, are imported.

> #### Step 2
> The image is loaded and displayed in a loop to allow for manual selection of parking spaces. The loop runs until the program is terminated.

> #### Step 3
> The average width and height values of parking spaces are obtained from the selected image.

> #### Step 4
> The initial positions (left-upper corners) of the parking space rectangles are stored in an array called `startingCoordinates`. The `cv2.setMouseCallback()` function is used to enable mouse click selection.

> #### Step 5
> The selected coordinates are stored in a file called "finalCoordinates" using the `pickle.dump()` function, ensuring the data is saved even after program termination.

### Main.py
This file is responsible for counting the free parking spaces using the coordinates obtained from `FreeSpaceFinder.py`.

> #### Step 1
> The video file, "carPark.mp4", is opened and played in a loop. The loop restarts the video once it reaches the end, ensuring continuous observation.

> #### Step 2
> The coordinates of the parking spaces are imported from the "finalCoordinates" file using the `pickle.load()` function.

> #### Step 3
> The video frames are cropped to the regions defined by the parking space coordinates, creating smaller video frames for each parking space.

> #### Step 4
> The cropped images are converted to grayscale and then blurred. The goal is to identify whether a parking space is occupied or free based on the count of white pixels in the image.


## How to Use

1. Set up the environment:

   - Install Python 3 on your system if it is not already installed.
   - Install the required libraries by running the following command:
     ```
     pip install opencv-python cvzone numpy
     ```

2. Prepare the parking lot image:

   - Capture or obtain an image of the parking lot from a bird's eye view.
   - Make sure the image has clear visibility of the parking spaces without any obstructions.
   - Save the image in a suitable format (e.g., JPEG or PNG).

3. Run the `FreeSpaceFinder.py` script:

   - Open a command prompt or terminal window and navigate to the directory containing the script.
   - Run the following command to start the script:
     ```
     python FreeSpaceFinder.py
     ```
   - The parking lot image will be displayed.
   - Click on the left-upper corner of each parking space in the image using the left mouse button.
   - If you make a mistake or want to remove a parking space, click inside an existing rectangle using the right mouse button.
   - Repeat the process for each parking space until all spaces are marked.
   - Close the image window to save the parking space coordinates.

4. Run the `main.py` script:

   - Open a command prompt or terminal window and navigate to the directory containing the script.
   - Run the following command to start the script:
     ```
     python main.py
     ```
   - The parking lot video will be displayed.
   - The parking space rectangles will be overlaid on each frame of the video.
   - If a car is detected in a parking space, the corresponding rectangle will be marked as occupied.
   - You can observe the real-time detection of occupied and free parking spaces.

5. Adjust the detection threshold (optional):

   - If the detection results are not accurate, you can adjust the threshold for considering a parking space as occupied or free.
   - Open the `main.py` script in a text editor.
   - Modify the value of the `threshold` variable to a suitable value.
   - A lower threshold will result in stricter detection, while a higher threshold will be more lenient.
   - Save the script and run it again to see the updated results.


## Project Details
This project utilizes computer vision techniques to detect and count free parking spaces in a bird's eye view video. The process involves selecting parking spaces, storing their coordinates, and then analyzing video frames to determine occupancy. The goal is to create a robust system that is minimally affected by minor changes within the parking lot environment. For further details and visualizations, refer to the provided demonstration videos.
