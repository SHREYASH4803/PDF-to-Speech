import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def main():
    pdf_path = "C:/Users/shrey/Downloads/SkillsBuild.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
   # print(extracted_text)  

if __name__ == "__main__":
    main()
