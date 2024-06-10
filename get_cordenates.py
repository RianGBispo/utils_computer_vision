import cv2

# Função para redimensionar a imagem pela metade
def resize_image(image):
    width = int(image.shape[1] * 0.5)
    height = int(image.shape[0] * 0.5)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized


# Função de callback para lidar com cliques do mouse
def get_coordinates(event, x, y, flags, param):
    global point, img_copy
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x*2, y*2)  # Ajusta as coordenadas para a imagem original
        img_copy = img_resized.copy()
        cv2.circle(img_copy, point, 5, (0, 0, 255), -1)  # Desenha um círculo vermelho no ponto clicado
        cv2.imshow("Image", img_copy)
        print(point)


# Carrega a imagem
image_path = r"C:\Users\Rian.bispo\PycharmProjects\mecanizacao1\mecanizacao\lubrificacao\static\lubrificacao\images\modelo_lub.png"
img = cv2.imread(image_path)
img_resized = resize_image(img)
img_copy = img_resized.copy()

point = None

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", get_coordinates)

while True:
    cv2.imshow("Image", img_copy)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Pressiona 'ESC' para sair
        break

cv2.destroyAllWindows()

if point is not None:
    print(f"Coordenadas do ponto selecionado: {point}")
else:
    print("Nenhum ponto foi selecionado.")
