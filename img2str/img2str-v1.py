"""
Este script extrai texto de uma imagem usando OCR (Optical Character Recognition) e fornece opções para exibir o texto na tela ou salvá-lo em um arquivo de texto.

Usage:
    python script.py <filename> [--language LANGUAGE] [--save] [--display]

Arguments:
    filename (str): Caminho para o arquivo de imagem a ser processado.

Options:
    --language LANGUAGE, -l LANGUAGE: Idioma para o reconhecimento de caracteres OCR (padrão: eng).
    --save, -s: Salvar o texto extraído em um arquivo de texto.
    --display, -d: Exibir o texto extraído na tela.

Exemplos de uso:
    # Extrair texto da imagem 'imagem.png' e exibi-lo na tela
    python script.py imagem.png --display

    # Extrair texto da imagem 'imagem.png' usando o idioma 'por' e salvá-lo em um arquivo de texto
    python script.py imagem.png --language por --save
"""

import argparse
import cv2
import pytesseract
import os

def extract_text(filename, language='eng', save_to_file=False, display=False):
    """
    Extrai texto de uma imagem usando OCR (Optical Character Recognition) e fornece opções para exibir o texto na tela ou salvá-lo em um arquivo de texto.

    Args:
        filename (str): Caminho para o arquivo de imagem a ser processado.
        language (str, optional): Idioma para o reconhecimento de caracteres OCR (padrão: 'eng').
        save_to_file (bool, optional): Se True, salva o texto extraído em um arquivo de texto (padrão: False).
        display (bool, optional): Se True, exibe o texto extraído na tela (padrão: False).

    Returns:
        None

    Raises:
        FileNotFoundError: Se o arquivo de imagem especificado não for encontrado.
        Exception: Se ocorrer um erro ao processar a imagem.

    """
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
