import cv2
cv2.imread("solar-system.jpg")
cv2.imshow
cv2.waitKey(10)
cv2.putText(img,
            "sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.imwrite("Solar_systemwithname.jpg",img)