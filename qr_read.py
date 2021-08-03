import cv2
import numpy as np


# -----------------------------------------------------------
# initial
# -----------------------------------------------------------
font = cv2.FONT_HERSHEY_SIMPLEX
FILE_PNG_AB = 'qrcode_AB.png'


# -----------------------------------------------------------
# function_qr_dec
# -----------------------------------------------------------
def function_qrdec_cv2(img_bgr):

    # QRCodeDetectorインスタンス生成
    qrd = cv2.QRCodeDetector()

    # QRコードデコード
    retval, decoded_info, points, straight_qrcode = qrd.detectAndDecodeMulti(img_bgr)

    if retval:
        points = points.astype(np.int)

        for dec_inf, point in zip(decoded_info, points):
            if dec_inf == '':
                continue

            # QRコード座標取得
            x = point[0][0]
            y = point[0][1]

            # QRコードデータ
            print('dec:', dec_inf)
            img_bgr = cv2.putText(img_bgr, dec_inf, (x, y-6), font, .3, (0, 0, 255), 1, cv2.LINE_AA)

            # バウンディングボックス
            img_bgr = cv2.polylines(img_bgr, [point], True, (0, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow('image', img_bgr)
    cv2.waitKey(0)


# -----------------------------------------------------------
# sample program
# -----------------------------------------------------------
img_BGR = cv2.imread(FILE_PNG_AB, cv2.IMREAD_COLOR)
function_qrdec_cv2(img_BGR)