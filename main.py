import fitz  # PyMuPDF
import os

# Путь к PDF
pdf_path = "input.pdf"

# Папка для JPEG
output_folder = "output_jpegs"
os.makedirs(output_folder, exist_ok=True)

# Открываем PDF
doc = fitz.open(pdf_path)

# Проходим по всем страницам и сохраняем как JPEG
for page_number in range(len(doc)):
    page = doc.load_page(page_number)
    pix = page.get_pixmap(dpi=200)  # можно поменять dpi
    output_path = os.path.join(output_folder, f"page_{page_number + 1}.jpg")
    pix.save(output_path)

print(f"Готово! Сохранено {len(doc)} JPEG-файлов.")