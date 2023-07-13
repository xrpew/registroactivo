import cv2
from pyzbar import pyzbar
import requests

def detectar_qr(frame):
    decoded_objects = pyzbar.decode(frame)
    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
        return data
    return None

cap = cv2.VideoCapture(0)
cv2.namedWindow('Cámara')

currentQR = ''
while True:
    ret, frame = cap.read()

    cv2.imshow('Cámara', frame)

    # Esperar hasta que se presione una tecla
    key = cv2.waitKey(1)
    qr_data = detectar_qr(frame)
    if qr_data is not None and currentQR != qr_data:
        response = requests.get(qr_data)
        currentQR = qr_data
        print(response.text)
        pass

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
