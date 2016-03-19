# coding:utf8
'''
Created on Dec 18, 2015
MySQLdb module Test and Data PreProcess
@author: moyang
@version: 1.0
'''
import urllib2
import urllib
from urllib2 import Request, urlopen, URLError, HTTPError  
#response = urllib2.urlopen('http://nba.hupu.com/')  
#html = response.read()  
#print html


#request = urllib2.Request('http://bbs.hupu.com/14965853.html') 
#response2 = urllib2.urlopen(request)
#result = response2.read()  
#print result


#old_url = 'http://nba.hupu.com/'
#request2 = Request(old_url)
#response3 = urllib2.urlopen(request2)
#new_url = response3.geturl()
#print old_url
#print new_url
#print response3.info()


postdata=urllib.urlencode({  
    'username':'muyan',  
    'password':'why888',  
    'continueURI':'http://www.verycd.com/',  
    'fk':'',  
    'login_submit':'登录'  
})  
#req = urllib2.Request(  
#    url = 'http://secure.verycd.com/signin',  
#    data = postdata  
#)  
#result = urllib2.urlopen(req)  
#print result.read()   


# 伪装成浏览器访问

#headers = {
#           'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
#           'Referer':'http://www.cnbeta.com/deliver'
#}
#request = Request(
#                  url = 'http://www.cnbeta.com/deliver',
##                  data = postdata,
#                  headers = headers
#        )
#result = urllib2.urlopen(request)
#print result.read()


#  百度贴吧案例
#import string
#def baidu_tieba(url,beginPage,endPage):
#    for i in range(beginPage,endPage+1):
#        sName = string.zfill(i,5) + '.html'#自动填充成六位的文件名  
#        print '正在下载第' + str(i) + '个网页，并将其存储为' + sName + '......'  
#        f = open('H:/spider/'+sName,'w+')
#        m = urllib2.urlopen(url + str(i)).read()
#        f.write(m)
#        f.close()
#
#bdurl = str(raw_input(u'请输入贴吧的地址，去掉pn=后面的数字：\n'))  
#begin_page = int(raw_input(u'请输入开始的页数：\n'))  
#end_page = int(raw_input(u'请输入终点的页数：\n'))  
#
#baidu_tieba(bdurl,begin_page,end_page)  



# 正则表达式
import re
import string

pattern = re.compile('\d*\.\d+')  

match1 = pattern.match('253')
match2 = pattern.match('4454.0')
match3 = pattern.match('58.23')

if(match1):
    print match1.group(),'是小数！'
else:  
    print 'match1不是小数！'
if(match2):
    print match2.group(),'是小数！'
else:  
    print 'match1不是小数！'
if(match3):
    print match3.group(),'是小数！'
else:  
    print 'match1不是小数！'

m = re.match(r'(\w+) (\w+)(?P<sign>.*)','hello world')
print "m.string:", m.string  
print "m.re:", m.re  
print "m.pos:", m.pos  
print "m.endpos:", m.endpos  
print "m.lastindex:", m.lastindex  
print "m.lastgroup:", m.lastgroup

print "m.group():", m.group()  
print "m.group(1,2):", m.group(1, 2)  
print "m.groups():", m.groups()  
print "m.groupdict():", m.groupdict()  
print "m.start(2):", m.start(2)  
print "m.end(2):", m.end(2)  
print "m.span(2):", m.span(2)  
print r"m.expand(r'\g<2> \g<1>\g<3>'):", m.expand(r'\2 \1\3')  


p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)

print "p.pattern:", p.pattern  
print "p.flags:", p.flags  
print "p.groups:", p.groups  
print "p.groupindex:", p.groupindex  


p2 = re.compile(r'muyan')
match = p2.search('moyang muyanmoyang')
if(match):
    print match.group()
else:
    print '不匹配'


p3 = re.compile(r'\d')
print p3.split('fenwif4fresf5reagr2vfreab5')


p4 = re.compile(r'[a-zA-Z]')
print p4.findall('2f5473ea87n695v860g93-4250=r-4=jkntj436nj5njk46nk53')


p5 = re.compile(r'\d+')
iterator = p5.finditer('fewq454gh t542y 65hbgt dnhy 546t5hv y5fct5')
for m in iterator:
    print m.group() 




