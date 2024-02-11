import argparse
import cv2
import pytesseract

def extract_text(filename, language='eng'):
    try:
        # Carrega a imagem
        img = cv2.imread(filename)
        
        # Extrai texto da imagem
        resultado = pytesseract.image_to_string(img, lang=language)

        # Imprime o texto extraído
        print("Texto Extraído:")
        print("=" * 20)
        print(resultado)
        print("=" * 20)
    except Exception as e:
        print(f"Ocorreu um erro ao processar a imagem: {e}")

if __name__ == "__main__":
    # Configura o parser de argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Extract text from an image")
    parser.add_argument("filename", help="caminho para o arquivo de imagem")
    parser.add_argument("--language", "-l", default="eng", help="idioma para OCR (default: eng)")

    # Analisa os argumentos da linha de comando
    args = parser.parse_args()

    # Chama a função extract_text com os argumentos fornecidos
    extract_text(args.filename, args.language)
