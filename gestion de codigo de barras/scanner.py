import cv2
import pyzbar.pyzbar as pyzbar

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    # Leer un frame de la cámara
    ret, frame = cap.read()

    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar los códigos de barras en el frame
    barcodes = pyzbar.decode(gray)

    # Dibujar los rectángulos alrededor de los códigos de barras detectados
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar la ventana con la cámara y los códigos de barras detectados
    cv2.imshow('Cámara', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()