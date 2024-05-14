import cv2

# Cargar el clasificador de códigos de barras
barcodes_cascade = cv2.CascadeClassifier('barcodes.xml')

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Crear una variable para almacenar los códigos de barras leídos
barcodes_read = []

while True:
    # Leer un frame de la cámara
    ret, frame = cap.read()

    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar los códigos de barras en el frame
    barcodes = barcodes_cascade.detectMultiScale(gray)

    # Dibujar los rectángulos alrededor de los códigos de barras detectados
    for (x, y, w, h) in barcodes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Leer el código de barras
        barcode = gray[y:y+h, x:x+w]
        barcode_text = cv2.readBarcodes(barcode, cv2.Barcode.DECODE_ALL)[0][0]

        # Almacenar el código de barras leído
        barcodes_read.append(barcode_text)

    # Mostrar la ventana con la cámara y los códigos de barras detectados
    cv2.imshow('Cámara', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()

# Imprimir los códigos de barras leídos
print("Códigos de barras leídos:")
for barcode in barcodes_read:
    print(barcode)