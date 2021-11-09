import unittest
from DocumentProcessor import DocumentProcessor


class TestStringMethods(unittest.TestCase):

    documentProcessor = DocumentProcessor()

    contractNumbers = [['test.png', '1253748']]

    def test_1(self):
        documentProcessor = DocumentProcessor()

        for files in self.contractNumbers:
            self.assertEqual(documentProcessor.retrieveContractNumber("inputfiles/" + files[0]), files[1])
            print (files[0], files[1])


        self.assertEqual(documentProcessor.retrieveContractNumber("inputfiles/test.png"), '1253748')

if __name__ == '__main__':
    unittest.main()