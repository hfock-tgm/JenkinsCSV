import csv
class CSVReader():
    def __init__(self, filename):
        self.filename = filename

    def loadCSV(self):
        helpVar = ""
        with open(self.filename, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in reader:
                helpVar += ' '.join(row) + "\n"
        return helpVar

    def saveCSV(self, text):
        with open(self.filename, 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            zeilen = text.split("\n")
            for zeile in zeilen:
                if zeile != "":
                    woerter = zeile.split(" ")
                    writer.writerow(woerter)

if __name__ == "__main__":
    print ("test")
    test = CSVReader('csv_file.csv')
    test.saveCSV('1;2;3;4;')
    print (test.loadCSV())
    test.saveCSV('4;3;2;1;')
    print (test.loadCSV())
