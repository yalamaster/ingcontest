# ingcontest
ING Contest: who writes the best document reading tool

In this contest you are gonna play with opensource OCR tooling. The contest is based
on real project. Due to migration of all archives to a new archive, documents where stored
under wrong contractnumbers. Before putting the documents in the target archive the correct
documentsnumbers must be retracted from the contract using OCR tooling.

Unfortunately all documents were not scanned very accurate, so you need to do some tricks to
retrieve the right contractnumbers. Can you write a DocumentProcessor class that recognises all
the right contractnumbers?

You can test your DocumentProcessor using the testSuite.

Please feel free not to use Tesseract but use your own tools.

Good luck!




To run this programm you need to first:
Windows:
- install the Tesseract software (https://youtu.be/QJkKDsjj1oA) - windows
- install pytesseract using pip: pip install pytesseract
- make sure in the DocumentProcessor you add the location of the Tesseract executable

Mac:
- install the Tesseract software using homebrew: brew install tesseract - mac users
- install pytesseract using pip: pip install pytesseract
- remove the line with the location of Tesseract.exe in DocumentProcessor
