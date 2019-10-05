import re
import json

a = input()
while a!="END":
    i = (a.find(','))
    name = a[0:i]
    a = a[i+1:]
    number = re.sub("\D", "", a)
    number = number[0:11]
    a=re.sub(number, '', a)
    a = a.strip('.')
    aa = a.find('省', 1)
    if aa != -1:
        province = a[0:aa+1]
        a = a[aa+1:]
        aa = a.find('市', 1)
        city = a[0:aa+1]
        a = a[aa+1:]
        aa = a.find('县', 1)
        if aa != -1:
            town = a[0:aa+1]
            a = a[aa + 1:]
        else:
            aa = a.find('区', 1)
            if aa != -1:
                town = a[0:aa+1]
                a = a[aa + 1:]
            else:
                aa = a.find('市', 1)
                if aa != -1:
                    town = a[0:aa + 1]
                    a = a[aa + 1:]
                else:
                    aa = a.find('自治州', 1)
                    if aa != -1:
                        town = a[0:aa + 1]
                        a = a[aa + 1:]
                    else:
                        town = ''''''
        aa = a.find('镇', 1)
        if aa != -1:
            road = a[0:aa+1]
            a = a[aa + 1:]
        else:
            aa = a.find('街道', 1)
            if aa != -1:
                road = a[0:aa+1]
                a = a[aa + 1:]
            else:
                aa = a.find('乡', 1)
                if aa != -1:
                    road = a[0:aa + 1]
                    a = a[aa + 1:]
                else:
                    road = ''''''

        d={"姓名":name,"手机":number,"地址":[province,city,town,road,a]}
        d = json.dumps(d, ensure_ascii=False)
        print(d)
        a=input()
    else:
        province = a[0:2]
        city = a[0:2]+'市'
        a = a[3:]
        aa = a.find('县', 1)
        if aa != -1:
            town = a[0:aa + 1]
            a = a[aa + 1:]
        else:
            aa = a.find('区', 1)
            if aa != -1:
                town = a[0:aa + 1]
                a = a[aa + 1:]
            else:
                aa = a.find('市', 1)
                if aa != -1:
                    town = a[0:aa + 1]
                    a = a[aa + 1:]
                else:
                    town = ''''''
        aa = a.find('镇', 1)
        if aa != -1:
            road = a[0:aa + 1]
            a = a[aa + 1:]
        else:
            aa = a.find('街道', 1)
            if aa != -1:
                road = a[0:aa + 1]
                a = a[aa + 1:]
            else:
                aa = a.find('乡', 1)
                if aa != -1:
                    road = a[0:aa + 1]
                    a = a[aa + 1:]
                else:
                    road = ''''''
        d = {"姓名": name, "手机": number, "地址": [province, city, town, road, a]}
        d = json.dumps(d, ensure_ascii=False)
        print(d)
        a=input()