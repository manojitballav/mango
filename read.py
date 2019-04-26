# This program is to read from the spreadsheet and import it into the database
import xlrd, pymongo
from pymongo import MongoClient

client = MongoClient('10.56.133.13',27017)
db = client['final']
col = db['loki']

def main():
    workbook = xlrd.open_workbook('original.xlsx')
    worksheet = workbook.sheet_by_index(0)
    for val in range(1,worksheet.nrows):
        rank = int((worksheet.cell(val,0)).value)
        channel  = str((worksheet.cell(val,1)).value)
        category = str((worksheet.cell(val,2)).value)
        product = str((worksheet.cell(val,4)).value)
        brand = str((worksheet.cell(val,5)).value)
        size = str((worksheet.cell(val,8)).value)
        link = str((worksheet.cell(val,9)).value)
        link = link[:link.find("&")]

        doc = ({"_id": rank,'channel':channel,'category':category,'product':product,'brand':brand,'size':size,'link':link})
        col.insert_one(doc)
    print("Complete")

if __name__ == '__main__':
    main()
