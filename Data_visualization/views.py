import json
import xlrd
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def data_visualization(request):
    return render(request, 'data_visualization.html')


def process_data(request):
    efile = xlrd.open_workbook(r'D:\temp\test1.xlsx')
    data = pie_and_simple_bar(efile)
    return HttpResponse(json.dumps(data), content_type="application/json")


def pie_and_simple_bar(excelfile):
    sheet = excelfile.sheet_by_index(1)
    title = sheet.cell(0,0).value
    mtype = sheet.row_values(1)
    num = sheet.row_values(2)

    piedata = []
    for value,name in zip(num,mtype):
        temp_dict = {'value':value,'name':name}
        piedata.append(temp_dict)

    unit = '数量'
    data = {"bar":{"name": mtype,       # 坐标系横坐标
                    "data": num,        # 图像数据
                    "title": title,     # 图像标题
                    "present": unit,    # 图例
            },
            "pie":{
                    "data":piedata,     # 图表数据
                    "title":title,      # 图表标题
                    "present":mtype,    # 图例数据数组
                    "unit":unit         # 图表图例


            }
        }
    return data

def scatter(excelfile):
    sheet = excelfile.sheet_by_index(0)
    col1 = sheet.col_values(0)[1:]
    col2 = sheet.col_values(1)[1:]
    xAxis = col1[0]
    yAxis = col2[0]
    data = list(map(list,zip(col1[1:],col2[1:])))
    
