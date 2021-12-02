'''
feeds the camera source to the screen
'''

import cv2 as cv

def read_feed(cam, res):
    capture = cv.VideoCapture(cam)

    #setting resolution
    capture.set(3, res[0])
    capture.set(4, res[1])
    
    while True:
        isTrue, frame = capture.read()
        cv.imshow("live feed", frame)

        if cv.waitKey(20) & 0xFF == ord('d'):
                break
        if not isTrue:    # to prevent a read error 
                break

def main():
    cam = 0

    #resolution index
    res_index = {
            0 : (640, 480),
            1 : (800, 600),
            2 : (1360, 768),
            3 : (1920, 1080)
        }

    #calling feeder
    read_feed(cam, res=res_index[3])

main()