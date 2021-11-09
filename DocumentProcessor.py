try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

class DocumentProcessor:

    def retrieveContractNumber(self, filename):
        ocrText = pytesseract \
            .image_to_string(Image.open(filename)) \
            .splitlines
        _lineWithContractNumber = self.__findLineContractNumber(ocrText)
        _contractNumber =  self.__filterContractNumberFromLine(_lineWithContractNumber)
        return _contractNumber

    def __findLineContractNumber(self,stringList):
        print("fineLine")
        for line in stringList:
            if "Contractnummer" in line:
                return line
        return "not found"

    def __filterContractNumberFromLine(self,line):
        line = line.replace("Contractnummer", "")
        line = line.strip()
        return line