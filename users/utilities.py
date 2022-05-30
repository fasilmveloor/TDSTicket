import fitz


def getVaccinationStatus(vaccinationCertificate):
    with fitz.open(vaccinationCertificate) as pdf:
        for page in pdf:
            for text in page.getText():
                if text.find('Fully Vaccinated') or text.find('Partially Vaccinated'):
                    return True
    return False
    
    