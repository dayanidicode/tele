
import cv2
import numpy as np
import urllib.request
url='https://4263-2409-4072-8d9e-1ac2-b0f3-6060-5532-a4bd.in.ngrok.io'
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

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

