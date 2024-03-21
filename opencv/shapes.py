import cv2
image=cv2.imread('Frozen.jpg',1)
cv2.line(image,(0,0),(400,400),(255,0,0),5)
cv2.circle(image,(200,200),50,(0,0,250),-1)
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(image,"snow",(30,30),font,2,(80,45,89))
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()