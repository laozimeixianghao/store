'''
1.完成衣服销售数据的统计和分析
1.1计算总销售额
1.2计算平均每日销售数量
1.3 计算每个种类月销售量占比
2.上传代码到云端仓库，并把仓库地址发到组长，组长统一一下发到群里
'''
print("--------十二月销售数据----------")
print("日期	服装名称	价格/件	库存数量	销售量/每日")
print("1号	羽绒服	253.6	500	      10")
print("8号	羽绒服	253.6	500	      69")
print("10号	羽绒服	253.6	500	      140")
print("17号	羽绒服	253.6	500	      10")
print("28号	羽绒服	253.6	500	      10")

print("2号	牛仔裤	86.3	600	      60")
print("7号	牛仔裤	86.3	600	      72")
print("9号	牛仔裤	86.3	600	      35")
print("11号	牛仔裤	86.3	600	      90")
print("15号	牛仔裤	86.3	600	      60")
print("20号	牛仔裤	86.3	600	      60")
print("24号	牛仔裤	86.3	600	      140")

print("3号	风衣	    96.8	335	      43")
print("14号	风衣	    96.8	335	      25")
print("18号	风衣	    96.8	335	      43")
print("22号	风衣	    96.8	335	      60")
print("26号	风衣	    96.8	335	      43")
print("30号	风衣	    96.8	335	      78")

print("4号	皮草	    135.9	855    	  63")
print("12号	皮草	    135.9	855    	  24")
print("21号	皮草     135.9	855	      63")
print("27号	皮草	    135.9	855	      57")

print("5号	T血	    65.8	632	      63")
print("13号	T血	    65.8	632	      45")
print("16号	T血  	65.8	632 	  129")
print("19号	T血	    65.8	632	      63")
print("23号	T血	    65.8	632	      58")
print("25号	T血	    65.8	632	      48")
print("29号	T血	    65.8	632	      63")

print("6号	衬衫	    49.3	562	      120")
yrf=(10+69+140+10+10)
nzk=(60+72+35+90+60+60++140)
fy=(43+25+43+60+43+78)
pc=(63+24+63+57)
tx=(63+45+129+63+58+48+63)
cs=(120)
yrfprice = yrf * 253.6
nzkprice = nzk * 86.3
fyprice  = fy * 96.8
pcprice  = pc * 135.9
txprice  = tx * 65.8
csprice  = cs * 49.3
num=yrf+nzk+fy+pc+tx+cs
print("销售总额为:",yrfprice+nzkprice+fyprice+pcprice+txprice+csprice)
print("平均每日销售量：",(yrf+nzk+fy+pc+tx+cs)/30)
print("羽绒服月销售量占比为:{:.2f}%".format(yrf/num*100))
print("牛仔裤月销售量占比为:{:.2f}%".format(nzk/num*100))
print("风衣月销售量占比为:{:.2f}%".format(fy/num*100))
print("皮草月销售量占比为:{:.2f}%".format(pc/num*100))
print("T血月销售量占比为:{:.2f}%".format(tx/num*100))
print("衬衫月销售量占比为:{:.2f}%".format(cs/num*100))



