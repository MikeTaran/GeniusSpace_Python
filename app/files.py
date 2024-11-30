import logging
import os
import shutil
from fastapi import Depends, APIRouter, Form, File, UploadFile, HTTPException
# from fastapi.responses import FileResponse
from app.schemas import ImageProcessingOptions, FileProcessingOptions, ConversionType
from app.users import current_active_user
from app.db import User
from app.utils import process_image, process_file

file_router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@file_router.post("/upload/")
async def upload_file(
        file: UploadFile = File(...),
        resize: str = Form(None),
        convert_to: str = Form(None),
        grayscale: bool = Form(None),
        flip: str = Form(None),
        xlsx_to_csv: bool = Form(None),
        csv_to_xlsx: bool = Form(None),
        docx_to_pdf: bool = Form(None),
        pdf_to_docx: bool = Form(None),
        user: User = Depends(current_active_user)
):
    # Determine conversion type from form parameters
    conversion_type = None
    if xlsx_to_csv:
        conversion_type = ConversionType.XLSX_TO_CSV
    elif csv_to_xlsx:
        conversion_type = ConversionType.CSV_TO_XLSX
    elif docx_to_pdf:
        conversion_type = ConversionType.DOCX_TO_PDF
    elif pdf_to_docx:
        conversion_type = ConversionType.PDF_TO_DOCX
    user_folder = f"{UPLOAD_DIR}/{user.id}"
    os.makedirs(user_folder, exist_ok=True)
    file_location = os.path.join(user_folder, file.filename)

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        conversion_type = None
        if xlsx_to_csv and file.filename.lower().endswith('.xlsx'):
            conversion_type = ConversionType.XLSX_TO_CSV
        elif csv_to_xlsx and file.filename.lower().endswith('.csv'):
            conversion_type = ConversionType.CSV_TO_XLSX
        elif docx_to_pdf and file.filename.lower().endswith('.docx'):
            conversion_type = ConversionType.DOCX_TO_PDF
        elif pdf_to_docx and file.filename.lower().endswith('.pdf'):
            conversion_type = ConversionType.PDF_TO_DOCX

        # Process image if image options are provided
        if any([resize, convert_to, grayscale, flip]):
            options = ImageProcessingOptions(
                resize=resize,
                convert_to=convert_to,
                grayscale=grayscale,
                flip=flip
            )
            processed_file_location = process_image(file_location, options)
        # Process other file types if conversion type is provided
        elif conversion_type:
            options = FileProcessingOptions(conversion_type=conversion_type)
            processed_file_location = process_file(file_location, options)
            if processed_file_location == file_location:
                raise HTTPException(status_code=400, detail="Conversion failed or not supported for this file type")
        else:
            processed_file_location = file_location

        return {
            "filename": os.path.basename(processed_file_location),
            "location": processed_file_location
        }
    except Exception as e:
        logging.error(f"Error processing file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
