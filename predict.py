import cv2
import numpy as np

recog=cv2.face.LBPHFaceRecognizer_create()
recog.read("facemodel.yml")

test_image=f"virat.webp"

test_data=cv2.imread(test_image,0)

id,confi=recog.predict(test_data)

print(f'id :{id} , confi : {confi}')

cv2.imshow("Result",test_data)
cv2.waitKey()