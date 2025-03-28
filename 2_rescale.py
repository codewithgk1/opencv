import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    # For Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def ChangeRes(width,height):
    # For Live Videos
    capture.set(3,width)
    capture.set(4,height)

## Reading Videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    frame_resized_20 = rescaleFrame(frame,0.20)
    cv.imshow('Video_Resized',frame_resized)
    cv.imshow('Video_Resized_20',frame_resized_20)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()