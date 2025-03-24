import cv2

dropped = 0 # drop frames count

vid = cv2.VideoCapture('http://192.168.80.116/live') # open webcam capture

while True:
    ret, frame = vid.read() # get frame-by-frame
    print(vid.isOpened(), ret)
    if frame is not None:
        if dropped > 0: dropped = 0 # reset
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Blur the image for better edge detection
        frame_blur = cv2.GaussianBlur(frame_gray, (3,3), 0) 
            
            # Sobel Edge Detection
        sobelx = cv2.Sobel(src=frame_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
        sobely = cv2.Sobel(src=frame_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
        sobelxy = cv2.Sobel(src=frame_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
        # Display Sobel Edge Detection Images
        #cv2.imshow('Sobel X', sobelx)
        #cv2.waitKey(10)
        cv2.imshow('Sobel Y', sobely)
        #cv2.waitKey(10)
        #cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
        #cv2.waitKey(10)          
            # Canny Edge Detection
        #edges = cv2.Canny(image=frame_blur, threshold1=100, threshold2=200) # Canny Edge Detection
            # Display Canny Edge Detection Image
        #cv2.imshow('Canny Edge Detection', edges)
        if cv2.waitKey(22) & 0xFF == ord('q'): # press q to quit
            break
    else:
        dropped += 1
        if dropped > 100:
           print("Server is down")
           break

# Done, clear all resources
vid.release()
cv2.destroyAllWindows()
print("Video stop")

"""
# Display original image
cv2.imshow('Original', frame)
cv2.waitKey(0)
 
# Convert to graycsale
frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
frame_blur = cv2.GaussianBlur(frame_gray, (3,3), 0) 
 
# Sobel Edge Detection
sobelx = cv2.Sobel(src=frame_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=frame_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=frame_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey(0)
 
# Canny Edge Detection
edges = cv2.Canny(image=frame_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)"""