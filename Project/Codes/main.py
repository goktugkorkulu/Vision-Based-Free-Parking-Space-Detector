import cv2
import pickle
import cvzone
import numpy as np

width, height = 110, 47
with open('LotCoordinates', 'rb') as f:
    startingCoordinates = pickle.load(f)

videoCapture = cv2.VideoCapture('CarParkVisuals\carParkVideo.mp4')

while True:

    if videoCapture.get(cv2.CAP_PROP_POS_FRAMES) == videoCapture.get(cv2.CAP_PROP_FRAME_COUNT):
        videoCapture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, image = videoCapture.read()

    # STEP4
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageBlurred = cv2.GaussianBlur(imageGray, (5, 5), 1)
    imageBinary = cv2.adaptiveThreshold(imageBlurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25,
                                        16)
    imageMedianBlur = cv2.medianBlur(imageBinary, 5)
    kernel = np.ones((3, 3), np.uint8)
    imageDilate = cv2.dilate(imageMedianBlur, kernel, iterations=1)

    emptySpaceAmount = 0

    for coordinate in startingCoordinates:

        x, y = coordinate
        croppedImage = imageDilate[y:y + height, x:x + width]
        
        threshold = 850
        whiteCount = cv2.countNonZero(croppedImage)
        if whiteCount < threshold:
            color = (0, 255, 0)
            thickness = 4
            emptySpaceAmount += 1
        else:
            color = (0, 0, 0)
            thickness = 2

        cv2.rectangle(image, coordinate, (coordinate[0] + width, coordinate[1] + height), color, thickness)

        cvzone.putTextRect(image, str(whiteCount), (x + 2, y + height - 2), offset=0, thickness=2, scale=1,
                           colorR=color)

    cvzone.putTextRect(image, str('Free:' + str(emptySpaceAmount) + '/' + str(len(startingCoordinates))), (375, 60),
                       offset=10, thickness=2, scale=3, colorR=(203, 26, 163))

    cv2.imshow("Image", image)
    # cv2.imshow("ImageGray", imageGray)
    # cv2.imshow("ImageBlur", imageBlurred)
    # cv2.imshow("ImageBinary", imageBinary)
    # cv2.imshow("ImageMedianBlur", imageMedianBlur)
    # cv2.imshow("ImageDilate", imageDilate)

    cv2.waitKey(1)
