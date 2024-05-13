# import the necessary packages
from pyzbar import pyzbar
import cv2

# initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # read the frame from the camera
    ret, frame = cap.read()

    # decode the barcode from the frame
    barcodes = pyzbar.decode(frame)

    # check if any barcode was detected
    if len(barcodes) > 0:
        # get the first barcode
        barcode = barcodes[0]

        # store the code text in a variable
        barcode_text = barcode.data.decode("utf-8")
        print(barcode_text)

        # release the camera and destroy all windows
        cap.release()
        cv2.destroyAllWindows()

        # exit the loop
        break
cap.release()
cv2.destroyAllWindows()
