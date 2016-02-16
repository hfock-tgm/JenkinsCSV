import unittest
from at.fock.CSV.CSVReader import CSVReader

class CSVtest(unittest.TestCase):

    def setUp(self):
        self.csv = CSVReader('csv_file.csv')

    def test_load(self):
        try:
            self.csv.loadCSV()
        except IOError as e:
            self.fail("Where is the CSV-file?\n %s" % e)

    def test_save(self):
        try:
            self.csv.saveCSV("")
        except IOError as e:
            self.fail("Nope... Didn't work!\n%s" % e)

    def test_saveText(self):
        try:
            self.csv.saveCSV("1;2;3;")
            text = self.csv.loadCSV()
            assert text == "1;2;3;\n", "Doesn't match OMBRE!"
        except IOError as e:
            self.fail("Where is the CSV-file?\n %s" % e)

    def test_addText(self):
        try:
            added_text = "4;5;6;"
            old_text = self.csv.loadCSV()
            self.csv.saveCSV(old_text+added_text)
            new_text = self.csv.loadCSV()
            self.assertTrue(new_text == old_text+added_text+"\n", "Doesn't match OMBRE!")
        except IOError as e:
            self.fail("Where is the CSV-file?\n%s" % e)

    def test_linebreaks(self):
        try:
            asserted_text = "1;\n2;\n3;"
            added_text = "1;\n\n\n\n\n2;\n\n\n\n\n3;"
            old_text = self.csv.loadCSV()
            self.csv.saveCSV(old_text+added_text)
            new_text = self.csv.loadCSV()
            self.assertFalse(new_text == old_text+added_text, "Blanks no save no save")
            self.assertTrue(new_text == old_text+asserted_text+"\n",   "Blanks no save no save! Ali just cleaning")
        except IOError as e:
            self.fail("Where is the CSV-file?\n%s" % e)

    def cleanItUp(self):
        try:
            self.csv.saveCSV("")
        except IOError as e:
            self.fail("Couldn't clean CSV-file!\n%s" % e)


if __name__ == '__main__':
    unittest.main()