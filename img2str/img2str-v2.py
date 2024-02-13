"""
Este script extrai texto de uma ou várias imagens usando OCR (Optical Character Recognition) e salva os textos extraídos em arquivos de texto.

Usage:
    python script.py <image_path> [--output_folder OUTPUT_FOLDER] [--language LANGUAGE]

Arguments:
    image_path (str): Caminho para o arquivo de imagem ou diretório contendo imagens a serem processadas.

Options:
    --output_folder OUTPUT_FOLDER, -o OUTPUT_FOLDER: Caminho para a pasta de saída onde os arquivos de texto extraídos serão salvos (padrão: 'output').
    --language LANGUAGE, -l LANGUAGE: Idioma para o reconhecimento de caracteres OCR (padrão: 'eng').

Exemplos de uso:
    # Extrair texto de uma única imagem 'imagem.png' e salvar o texto extraído em 'output/imagem_extracted_text.txt'
    python script.py imagem.png

    # Extrair texto de todas as imagens em um diretório 'imagens/' e salvar os textos extraídos em 'output/'
    python script.py imagens/ -o output

    # Extrair texto de todas as imagens em um diretório 'imagens/' usando o idioma 'por' e salvar os textos extraídos em 'output/'
    python script.py imagens/ -o output -l por
"""

import argparse
import cv2
import pytesseract
import os

def extract_text_from_image(image_path, output_folder, language='eng'):
    """
    Extrai texto de uma ou várias imagens e salva os textos extraídos em arquivos de texto.

    Args:
        image_path (str): Caminho para o arquivo de imagem ou diretório contendo imagens a serem processadas.
        output_folder (str): Caminho para a pasta de saída onde os arquivos de texto extraídos serão salvos.
        language (str, optional): Idioma para o reconhecimento de caracteres OCR (padrão: 'eng').

    Returns:
        None

    Raises:
        FileNotFoundError: Se o arquivo ou diretório de imagem especificado não for encontrado.
        Exception: Se ocorrer um erro ao processar a imagem.

    """
    try:
        # Verificar se o diretório de saída existe, se não, criá-lo
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Verificar se o caminho é um arquivo ou diretório
        if os.path.isdir(image_path):
            for filename in os.listdir(image_path):
                image_file = os.path.join(image_path, filename)
                if os.path.isfile(image_file):
                    extract_text_from_single_image(image_file, output_folder, language)
        else:
            extract_text_from_single_image(image_path, output_folder, language)

    except FileNotFoundError:
        print(f"Diretório ou arquivo '{image_path}' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

def extract_text_from_single_image(image_path, output_folder, language='eng'):
    """
    Extrai texto de uma única imagem e salva o texto extraído em um arquivo de texto.

    Args:
        image_path (str): Caminho para o arquivo de imagem a ser processado.
        output_folder (str): Caminho para a pasta de saída onde o arquivo de texto extraído será salvo.
        language (str, optional): Idioma para o reconhecimento de caracteres OCR (padrão: 'eng').

    Returns:
        None

    Raises:
        Exception: Se ocorrer um erro ao processar a imagem.

    """
    try:
        # Carrega a imagem
        img = cv2.imread(image_path)

        # Extrai texto da imagem
        result = pytesseract.image_to_string(img, lang=language)

        # Salva o texto em um arquivo de texto
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        output_file = os.path.join(output_folder, f"{base_name}_extracted_text.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Texto extraído de {image_path} salvo em '{output_file}'")

    except Exception as e:
        print(f"Erro ao processar a imagem '{image_path}': {e}")

if __name__ == "__main__":
    # Configura o parser de argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Extract text from image(s)")
    parser.add_argument("image_path", help="caminho para o arquivo de imagem ou diretório contendo imagens")
    parser.add_argument("--output_folder", "-o", default="output", help="caminho para a pasta de saída (default: output)")
    parser.add_argument("--language", "-l", default="eng", help="idioma para OCR (default: eng)")

    # Analisa os argumentos da linha de comando
    args = parser.parse_args()

    # Chama a função extract_text com os argumentos fornecidos
    extract_text_from_image(args.image_path, args.output_folder, args.language)
