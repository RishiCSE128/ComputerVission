'''
Process images with 
    1. Gray scaling
    2. Thresholding 
    3. Edge Detection
    4. Contour Detection and overlaying 
'''

import cv2 as cv


def image_proc(img):
    #gray scaling 
    frame_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    #Thresholding
    thresh = 125
    ret, frame_thresold = cv.threshold(frame_gray, 
                                thresh=thresh, 
                                maxval=255, 
                                type=cv.THRESH_BINARY)
   

    #Blurring (reduces contour size)
    conv = 5      # has to be an odd number
    frame_blur = cv.GaussianBlur(frame_gray, 
                                ksize=(conv, conv),  # convolution size (odd number)
                                sigmaX=0,
                                borderType=cv.BORDER_DEFAULT)
    

    #edge detection 
    frame_edge = cv.Canny(frame_blur, threshold1=100, threshold2=200)
    
    #contour detection
    # cont = list of contours 
    # hier = shape hierarchy 
    cont, hier = cv.findContours(frame_edge,          # edge detected source
                                mode=cv.RETR_LIST,    # mode of contour finding, RETR_LIST = all cont found
                                method=cv.CHAIN_APPROX_SIMPLE) # approximation method [NONE = all, SIMPLE = compressed into one]
    
    frame_cont = cv.drawContours(img, cont, -1, (0,0,255),thickness=2)

    cv.putText(frame_cont,
                text=f'Contour found = {len(cont)}',
                org=(10,50), 
                fontFace=cv.FONT_HERSHEY_PLAIN,
                fontScale=2,
                color=(0,0,255),
                thickness=2
            )

    ret_dict = {
        'gray'      : {'frame': frame_gray},
        'threshold' : {'frame': frame_thresold, 
                        'thresh':thresh},
        'blur'      : {'frame': frame_blur, 
                       'conv': conv},
        'edge'      : {'frame' : frame_edge, 
                       'thresh' : [100,200]},
        'contour'   : {'frame': frame_cont, 
                       'count' : len(cont)}
    }
    return ret_dict
    
def read_feed(cam, res):
    capture = cv.VideoCapture(cam)

    #setting resolution
    capture.set(3, res[0])
    capture.set(4, res[1])
    
    while True:
        isTrue, frame = capture.read()
        cv.imshow("live feed", frame)

        proc_dict = image_proc(img=frame)

        cv.imshow("live feed (gray)", proc_dict['gray']['frame'])

        cv.imshow(f"live feed (thresholded {proc_dict['threshold']['thresh']})", 
                   proc_dict['threshold']['frame']
        )

        cv.imshow(f"live feed (Blur with conv = {proc_dict['blur']['conv']})",
                  proc_dict['blur']['frame']
        )

        cv.imshow("live feed (Edge)",proc_dict['edge']['frame'])

        cv.imshow("live feed (contours)",proc_dict['contour']['frame'])

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
    read_feed(cam, res=res_index[1])

main()