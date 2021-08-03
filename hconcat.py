import cv2

FILE_PNG_A = 'qrcode_A.png'
FILE_PNG_B = 'qrcode_B.png'
FILE_PNG_AB = 'qrcode_AB.png'

im1 = cv2.imread(FILE_PNG_A)
im2 = cv2.imread(FILE_PNG_B)

im_h = cv2.hconcat([im1, im2])
cv2.imwrite(FILE_PNG_AB, im_h)

cv2.imshow('image', im_h)
cv2.waitKey(0)