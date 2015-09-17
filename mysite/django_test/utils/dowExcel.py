# coding:utf-8 from django.shortcuts import render
import xlwt#Excel操作
import logging


def doDowExcel(sheetName=None, value=None):
	log = logging.getLogger('test1')
	log.info("测试下载excel文件")
	wb = xlwt.Workbook()
	if sheetName is None:
		ws = wb.add_sheet('Sheetname')
	else:
		ws = wb.add_sheet(sheetName)
    ########################################样式设置方式1
    #style_k=xlwt.easyxf("font: bold on,colour_index green,height 360; 
    #                align: wrap off;
    #                    borders:left 1,right 1,top 1,bottom 1;
    #                    pattern: pattern alt_bars, fore_colour gray25, back_colour gray25;")  
    #font: bold on,colour_index green,height 360,family:Arial; 字体加粗，字体颜色，字体大小,字体类型
    #align: wrap on; 自动折行，哈哈，这个好
    #pattern:fore_colour yellow, back_colour yellow，单元格的背景色，貌似要2个是一样的才生效

    ########################################样式设置方式2 
    #font 、 pattern 等等都为 class,赋值后，这个class 再作为 style的属性值
	fnt =xlwt.Font()
	fnt.name = 'Arial'
	fnt.colour_index = 4
	fnt.bold = True

	pattern=xlwt.Pattern() ###？？貌似不生效
	pattern.pattern = xlwt.Pattern.SOLID_PATTERN  
	pattern.pattern_back_colour=0x3A
	pattern.pattern_fore_colour=0x3A

	borders = xlwt.Borders()
	borders.left = 1
	borders.right = 1
	borders.top = 1
	borders.bottom = 1
	borders.bottom_colour=0x3A    

	style = xlwt.XFStyle()
	style.font = fnt
	style.borders = borders    
	style.pattern = pattern
    ##########################################设置第i列 的cell单元格的宽度
    #for i in range(2,8):
    #        ws.col(i).width = 0x0d00 + 2000
    ##########################################设置第i行 的cell单元格的高度 ？？？？
    #暂时没找到直接的方法或属性，不过可以通过合并单元格的间接方式来满足

    ##########################################往sheet表里写入数据
    #ws.write(row, col, data [,style])
	for line in range(0,len(value)):
		for column in range(0,len(value[line])):
			ws.write(line, column, value[line][column])
			
    #ws.write(0, 0, 'Firstname', style)
    #ws.write(10, 10, 'Firstname')
    ##########################################合并单元格
    #ws.write_merge(0,1,1,1,'Firstname',style) 

    ##########################################数字格式的处理 
    #style.num_format_str='YYYY-MM-DD'

    ##########################################数据超链接
    #n = "HYPERLINK"
    #attach_report=xlwt.Formula(n +'("http://www.baidu.com";"fame.pdf" )')
    #？？往一个单元格里写入多个超链接？？暂未找到方法
	return wb 
