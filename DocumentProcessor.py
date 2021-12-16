#

import cv2
import pytesseract
import os

class DocumentProcessor:

    def retrieveContractNumber(self, file):
        img = cv2.imread(file)
        rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        text = pytesseract.image_to_string(rgb_img)
        string_list = text.split()
        most_number_string = ""
        most_number_count = 0
        for string in string_list:
            if '-' not in string:
                number_count = 0
                for char in string:
                    if char in '1234567890':
                        number_count += 1
                if number_count > most_number_count:
                    most_number_count = number_count
                    most_number_string = string
        contract_number = most_number_string

        return contract_number