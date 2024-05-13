import cv2
import pyzbar.pyzbar as pyzbar

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

        # draw a bounding box around the barcode and display the text
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, barcode.data.decode("utf-8"), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # print the barcode data to the console
        print(barcode.data.decode("utf-8"))

    # display the frame
    cv2.imshow("Barcode Scanner", frame)

    # exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()