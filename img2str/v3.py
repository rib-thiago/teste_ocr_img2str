import argparse
import cv2
import pytesseract
import os

def extract_text(filename, language='eng', save_to_file=False, display=False):
    # Verifica se nenhuma opção foi selecionada
    if not save_to_file and not display:
        print("Nenhuma opção selecionada. O texto não foi exibido nem salvo.")
        return

    try:
        # Carrega a imagem
        img = cv2.imread(filename)

        # Extrai texto da imagem
        resultado = pytesseract.image_to_string(img, lang=language)

        # Imprime o texto extraído
        if display:
            print("Texto Extraído:")
            print("=" * 20)
            print(resultado)
            print("=" * 20)

        # Salva o texto em um arquivo de texto
        if save_to_file:
            with open("texto_extraido.txt", "w", encoding="utf-8") as f:
                f.write(resultado)
            print("Texto extraído salvo em 'texto_extraido.txt'")

    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

if __name__ == "__main__":
    # Configura o parser de argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Extract text from an image")
    parser.add_argument("filename", help="caminho para o arquivo de imagem")
    parser.add_argument("--language", "-l", default="eng", help="idioma para OCR (default: eng)")
    parser.add_argument("--save", "-s", action="store_true", help="salvar o texto extraído em um arquivo de texto")
    parser.add_argument("--display", "-d", action="store_true", help="exibir o texto extraído na tela")

    # Analisa os argumentos da linha de comando
    args = parser.parse_args()

    # Chama a função extract_text com os argumentos fornecidos
    extract_text(args.filename, args.language, args.save, args.display)
