import cv2

img = cv2.imread("./hanif.jpg")
cv2.imshow("Pic",img)

img_not = cv2.bitwise_not(img)
cv2.imshow("Invert1",img_not)
cv2.waitKey(0)
cv2.destroyAllWindows()