import json
import xlrd
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def data_visualization(request):
    return render(request, 'data_visualization.html')


def process_data(request):
    efile = xlrd.open_workbook(r'D:\temp\test1.xlsx')
    print (efile.sheet_names())
    sheet = efile.sheet_by_index(0)
    print(sheet.row_values(0))



    mtype = ["上衣", "裤子", "鞋子", "袜子", "衬衫", "短袖"]
    num = [210,540,123,150,900,620]
    title = '服装销售趋势'
    present = '数量'
    data = {"name": mtype,
            "data": num,
            "title": title,
            "present": present,
            "type": ["pie", "bar"],
            }
    return HttpResponse(json.dumps(data), content_type="application/json")
