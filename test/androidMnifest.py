# coding=utf-8
import xml.sax
import xlwt

data_list = []

all_permission=[]

class MyContentHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.permission=""
        self.currentData = ""
        self.exported=""
        self.row=0
        self.column=0

    def startDocument(self):
        print("开始解析xml")

    def endDocument(self):
        print("解析xml结束")

    # name-标签 attrs-标签中的属性
    def startElement(self, name, attrs):
        self.currentData=name
        # setup-1
        if name == "uses-permission":
           permission=attrs["android:name"]
           data_list.append(permission)
           sheet1.write(self.row, 0, permission) # 第1行第1列数据
           sheet1.write(self.row,1,"1")
           self.row+=1
        # setup-2
        # if name == "activity" or name =="service" or name =="provider" or name =="receiver":
        #     exported=attrs["exported"]
        #     if exported==None or exported=='':
        #         #  并判断是否等于true  如果等于true，就再excel里面设置为1
        #         if exported=="true":
                    1
        #setup-3 继续通过上面那两个工具  提取url、危险api  然后放入excel中的列


if __name__ == '__main__':
    # 创建 excel 指令：pip install xlwt、pip install xlrd
    workbook = xlwt.Workbook(encoding='utf-8')       #新建工作簿
    sheet1=workbook.add_sheet("androidPermission") # sheet
    # 解析xml
    saxParse = xml.sax.make_parser()
    saxParse.setFeature(xml.sax.handler.feature_namespaces, 0)  # 关闭命名解析
    handler = MyContentHandler()
    saxParse.setContentHandler(handler)
    saxParse.parse('1.xml')
    # 保存
    workbook.save(r"C:\Users\22365\Desktop\xml\permission.xlsx")
    print(data_list)


