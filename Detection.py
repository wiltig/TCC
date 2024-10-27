import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

Dog = cv2.CascadeClassifier('cascade5.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)

    toy = Dog.detectMultiScale(gray, 15, 20, minSize=(50,50))

    for (x, y, w, h) in toy:
        cv2.rectangle (frame, (x, y), (x+w, y+h),(0, 255, 0), 2)
        cv2.putText(frame,'Cachorro', x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA

    cv2.imshow('Cachorro', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


