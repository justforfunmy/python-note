import urllib.request
import urllib.parse
'''
# 存到本地
urllib.request.urlretrieve('http://www.hellobi.com',filename='./files/1.html')
# 清缓存
urllib.request.urlcleanup()

file = urllib.request.urlopen('http://www.hellobi.com',timeout=1)
print(file.info())
# 状态码
file.getcode()
# url
file.geturl()
'''

'''
for i in range(1,100):
    try:
        file = urllib.request.urlopen('http://www.hellobi.com',timeout=1)
        data = file.read()
        print(len(data))
    except Exception as e:
        print('error')
'''
'''
# 模拟http get请求
keyword = 'python'
# 中文编码
keyword = urllib.request.quote('中文')
# 默认不爬https
url = 'http://www.baidu.com/s?wd=' + keyword
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
file = open('./files/2.html','wb')
file.write(data)
file.close()
'''
# post
url = 'https://www.iqianyue.com/mypost/'
# 表单信息
myData = urllib.parse.urlencode({
    'name':'1234',
    'pass':'5678'
}).encode('utf-8')

req = urllib.request.Request(url,myData)
data = urllib.request.urlopen(req).read()
file = open('./files/3.html','wb')
file.write(data)
file.close()
