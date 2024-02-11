import cv2
import pytesseract

img = cv2.imread("frunze1.png")
#rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
resultado = pytesseract.image_to_string(img, lang='rus')


print("ORIGINAL")
print("========")
print("")
print(resultado)
print("")


'''

Fiz dois códigos em Python para testar leitura de texto em imagens:

O primeiro é um simples leitor de caracteres em portuges / ingles

O segundo é um leitor de russo que traduz pro inglês

vou testar os dois, com alguns arquivos que já separei. 


'''
