#read sheert and insert into db
import xlrd
from pymongo import MongoClient

client = MongoClient('127.0.0.1',27017)
db = client['Mono']
col = db['data']

workbook = xlrd.open_workbook('original.xlsx')
worksheet = workbook.sheet_by_index(0)
for val in range(1,worksheet.nrows):
    # rank = int((worksheet.cell(val,0)).value)
    channel  = str((worksheet.cell(val,1)).value)
    category = str((worksheet.cell(val,2)).value)
    product = str((worksheet.cell(val,4)).value)
    brand = str((worksheet.cell(val,5)).value)
    # size = str((worksheet.cell(val,8)).value)
    link = str((worksheet.cell(val,9)).value)
    link = link[:link.find("&")]
    try:
        col.update_one({'link':link},{'$set':{'channel':channel,'category':category,'product':product,'brand':brand}})
    except Exception as e:
        print(e)
