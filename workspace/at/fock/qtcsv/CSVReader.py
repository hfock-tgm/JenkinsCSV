import csv
class CSVReader():
    def __init__(self):
        pass

    def readCsv(self):
        with open('csv_file.csv', "rt", encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in reader:
                print (', '.join(row))

if __name__ == "__main__":
    test = CSVReader()
    test.readCsv()
