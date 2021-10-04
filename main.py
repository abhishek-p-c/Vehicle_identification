import cv2 
  
i=0

vid = cv2.VideoCapture(0) 

while(True): 

    ret, frame = vid.read() 
    path=r"C:\Users\HP\Desktop\CAP\basi"+str(i)+".jpg"
    cv2.imshow('frame', frame) 
    cv2.imwrite(path,frame)
    if cv2.waitKey(1) & 0xFF == 27: 
        break
    i=i+1

vid.release() 

cv2.destroyAllWindows()