import cv2 as cv


mouseX = mouseY= None

# operation when a mouse click is detected 
def click_event(event, x, y, flags, param):
    global mouseX
    global mouseY
    if event == cv.EVENT_LBUTTONDBLCLK:   # click detected
        mouseX = x
        mouseY = y

def draw_text(img, text):
    '''
    img: image ref
    loc: loc of the text
    txt: text string
    ''' 
    cv.putText(img,
               text, 
               (mouseX, mouseY), 
               fontFace=cv.FONT_HERSHEY_SIMPLEX,
               color=(255,255,0),
               fontScale=1)
    print(f'{mouseX},{mouseY}')
    return img

def draw_rect(img, loc):
    '''
    
    '''

def read_feed(cam, title, res):
    capture = cv.VideoCapture(cam)

    #setting resolution
    capture.set(3, res[0])
    capture.set(4, res[1])
   
    while True:
        isTrue, frame = capture.read()
        frame = draw_text(frame, 
                          text=f'{mouseX},{mouseX}')   # modifies the frame with overlay text
        
        cv.imshow(title, frame)    # shows the frame
        cv.setMouseCallback(title, click_event)  #detect a mouse click event and calls click_event() function

        if cv.waitKey(20) & 0xFF == ord('d'):
                break
        if not isTrue:    # to prevent a read error 
                break
    
    cv.waitKey(0)
    cv.destroyAllWindows()


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
    read_feed(cam, title='testCam', res=res_index[3])

main()