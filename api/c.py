import requests

 
 
def getlocalweather(a):
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    key = 'e049d649ad2eee12a967f37c8e6dcaf7'
    data = {'key': key, "city": a}
    req = requests.post(url, data)
    info = dict(req.json())
    info = dict(info)
    print(info)
    newinfo = info['lives'][0]
    print(newinfo)
    print()
    print("你查询的当地天气信息如下：")
    print("省市：",newinfo['province']+newinfo['city'])
    print("城市：", newinfo['city'])
    print("编码：", newinfo['adcode'])
    print("天气：", newinfo['weather'])
    print("气温：", newinfo['temperature']+'℃')
    print("风向：", newinfo['winddirection'])
    print("风力：", newinfo['windpower'])
    print("湿度：", newinfo['humidity'])
    print("报告时间：", newinfo['reporttime'])

    return newinfo


# 填入要合并的文件夹名字
City = input('请输入需要查询的城市\n') 
getlocalweather(City)