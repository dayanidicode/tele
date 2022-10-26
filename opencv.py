import time
import cv2
import numpy as np
import urllib.request
url='https://3f62-2409-4072-8d9e-1ac2-7d00-be31-254e-64db.in.ngrok.io/1600x1200.jpg'
#cap = cv2.VideoCapture(0)
while True:
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgnp,-1)
    # Capture image frame-by-frame
    #ret, img = cap.read()
    # Our operations on the frame come here
    # Display the resulting frame
    cv2.imwrite('frame.jpg',img)
    time.sleep(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

