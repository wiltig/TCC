import cv2

webCamera = cv2.VideoCapture (0)
ClassificadorVideoCahorro = cv2.CascadeClassifier('cascade5.xml')

while True:
    camera, frame = webCamera.read()

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detecta = ClassificadorVideoCahorro.detectMultiScale(cinza, scaleFactor=17, minNeighbors=20, minSize=(50, 50))
    for (x, y, w, h) in detecta:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Video WebCamera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webCamera.release()
cv2.destroyAllWindows()





