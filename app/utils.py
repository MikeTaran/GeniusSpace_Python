import logging
import os
import re
from PIL import Image, ImageOps
import pandas as pd
from pdf2docx import Converter
from app.schemas import ImageProcessingOptions, FileProcessingOptions, ConversionType
from docx import Document
from fpdf import FPDF


class FileConverter:
    @staticmethod
    def xlsx_to_csv(file_path: str) -> str:
        logging.info(f"Converting XLSX to CSV: {file_path}")
        try:
            df = pd.read_excel(file_path)
            output_path = f"{os.path.splitext(file_path)[0]}.csv"
            df.to_csv(output_path, index=False)
            logging.info(f"Successfully converted to CSV: {output_path}")
            return output_path
        except Exception as e:
            logging.error(f"Error converting XLSX to CSV: {str(e)}")
            raise

    @staticmethod
    def csv_to_xlsx(file_path: str) -> str:
        df = pd.read_csv(file_path)
        output_path = f"{os.path.splitext(file_path)[0]}.xlsx"
        df.to_excel(output_path, index=False)
        return output_path

    @staticmethod
    def docx_to_pdf(file_path: str) -> str:
        output_path = f"{os.path.splitext(file_path)[0]}.pdf"
        logging.info(f"Output path for PDF: {output_path}")
        document = Document(file_path)
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        pdf.add_font("Arial", "", "C:/Windows/Fonts/arial.ttf", uni=True)
        pdf.set_font("Arial", size=10)

        for paragraph in document.paragraphs:
            pdf.multi_cell(0, 10, paragraph.text, align="L")
            pdf.ln(10)

        pdf.output(output_path)
        return output_path

    @staticmethod
    def pdf_to_docx(file_path: str) -> str:
        output_path = f"{os.path.splitext(file_path)[0]}.docx"
        logging.info(f"Output path for DOCX: {output_path}")
        cv = Converter(file_path)
        cv.convert(output_path)
        cv.close()
        return output_path


def process_file(file_location: str, options: FileProcessingOptions) -> str:
    logging.info(f"Processing file: {file_location} with options: {options}")
    converter = FileConverter()
    conversion_map = {
        ConversionType.XLSX_TO_CSV: converter.xlsx_to_csv,
        ConversionType.CSV_TO_XLSX: converter.csv_to_xlsx,
        ConversionType.DOCX_TO_PDF: converter.docx_to_pdf,
        ConversionType.PDF_TO_DOCX: converter.pdf_to_docx,
    }

    if options.conversion_type:
        convert_func = conversion_map.get(options.conversion_type)
        if convert_func:
            try:
                return convert_func(file_location)
            except Exception as e:
                logging.error(f"Error during file conversion: {str(e)}")
                raise Exception(f"File conversion failed: {str(e)}")
    return file_location


def process_image(file_location: str, options: ImageProcessingOptions) -> str:
    with Image.open(file_location) as img:
        if options.resize:
            match = re.match(r'(\d+)x(\d+)', options.resize)
            if match:
                width, height = map(int, match.groups())
                img = img.resize((width, height))

        if options.grayscale:
            img = ImageOps.grayscale(img)

        if options.flip:
            if options.flip == 'horizontal':
                img = ImageOps.mirror(img)
            elif options.flip == 'vertical':
                img = ImageOps.flip(img)

        if options.convert_to:
            file_location = f"{os.path.splitext(file_location)[0]}.{options.convert_to}"
            img.save(file_location, options.convert_to.upper())
        else:
            img.save(file_location)
    return file_location
