import cv2
image=cv2.imread('Frozen.jpg',1)
cv2.line(image,(10,10),(370,560),(255,0,0),3)
cv2.circle(image,(10,15),15,(0,0,250),-1)
cv2.circle(image,(250,10),15,(0,0,250),-1)
cv2.circle(image,(12,370),15,(0,0,250),-1)
cv2.circle(image,(245,370),15,(0,0,250),-1)
cv2.rectangle(image,(100,100),(200,200),(0,255,0),5)
font=cv2.FONT_HERSHEY_PLAIN
cv2.putText(image,"hai",(100,170),font,4,(40,60,190))
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()