import cv2
import pyzxing
from pyzxing import BarcodeFormat, Reader

# Initialize the ZXing barcode reader
reader = Reader()

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to RGB format
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Decode the barcode from the frame
    barcode = None
    try:
        barcode = reader.decode(rgb_frame, formats=[BarcodeFormat.QR_CODE, BarcodeFormat.CODE_128])
    except pyzxing.NotFoundException:
        pass

    # If a barcode was found, print it to the console and break the loop
    if barcode is not None:
        print("Barcode format:", barcode.format)
        print("Barcode text:", barcode.text)
        break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()