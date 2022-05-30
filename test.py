import fitz # install using: pip install PyMuPDF

with fitz.open("test.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()

if text.find('fully vaccinated'):
	print('fully vaccinated')
print(text)
