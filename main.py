import numpy as np
import cv2
import LPR as lpr
import LCD as lcd

# yakalamayı başlat
cap = cv2.VideoCapture(0)
# LCD'yi başlat
lcd.start()
lcd.write("Ahmet KOKEN", 2)

# sonsuza kadar devam et
while True:

    # kare yakala
    ret, frame = cap.read()
    # kareyi LPR'ye gönder ve gelen görüntüyü a
    img = lpr.rec(frame)
    # gelen görüntüyü ekranda göster
    cv2.imshow('frame', img)
    # q tuşuna basılırsa çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# döngü bittiğinde yakalamayı durdur
cap.release()
cv2.destroyAllWindows()
