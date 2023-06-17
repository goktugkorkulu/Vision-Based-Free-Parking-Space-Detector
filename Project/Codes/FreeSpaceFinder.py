import cv2
import pickle

width = 110
height = 47

try:
    with open('LotCoordinates', 'rb') as f:
        startingCoordinates = pickle.load(f)
except:
    startingCoordinates = []


def coordinateSelector(events, x, y, flags, parameters):
    if events == cv2.EVENT_LBUTTONDOWN:
        startingCoordinates.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        i = -1;
        for coordinate in startingCoordinates:
            i = i + 1
            xi, yi = coordinate
            if xi < x < xi + width and yi < y < yi + height:
                startingCoordinates.pop(i)

    with open('LotCoordinates', 'wb') as f:
        pickle.dump(startingCoordinates, f)


while True:

    img = cv2.imread('CarParkVisuals\carParkImg.png')

    for coordinate in startingCoordinates:
        cv2.rectangle(img, coordinate, (coordinate[0] + width, coordinate[1] + height), (255, 0, 0), 2)

    cv2.imshow('image', img)

    cv2.setMouseCallback("image", coordinateSelector)

    cv2.waitKey(1)
