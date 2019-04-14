import requests
from bs4 import BeautifulSoup
import time

from datetime import date, datetime, time, timedelta
'''recive={

        "Train_Code": "2133", #車號
        "Class_Code": "1131",
        "Begin_Code": "1001",
        "Begin_Name": "基隆",
        "Begin_EName": "Keelung",
        "End_Code": "1215",
        "End_Name": "嘉義",
        "End_EName": "Chiayi",
        "Over_Night": "0",
        "Direction": "1",
        "MainViaRoad": "1",
        "Handicapped": "N",
        "Package": "N",
        "Dining": "N",
        "TrainType": "0",
        "From_Departure_Time": "0512",
        "To_Arrival_Time": "0516",
        "Fare": '15',
        "Comment": "每日行駛。",
        "Discount_Price_Adult": 'null',
        "Discount_Begin_Date": 'null',
        "Discount_End_Date": 'null',
        "From_Ticket_Code": "092",
        "To_Ticket_Code": "224",
        "Everyday": "Y",
        "TicketLink": "Y"

}'''


def getValue(data, pick):
    if pick == "departure":
        pick = "From_Departure_Time"
    if pick == "arrival":
        pick = "To_Arrival_Time"
    if pick == "number":
        pick = "Train_Code"
    if pick == "fare":
        pick = "fare"
    string = pick
    string = string + "\":"
    # print(string)
    tag1 = str(data).find(string)
    temp = str(data)[tag1 + len(string) + 2:]
    tag2 = str(temp).find("\",")
    ans = temp[:tag2]

    return str(ans)


def myInputTime():
    passFlag = False
    time = input('幾點後的車 : ')
    try:
        if len(time)==4:
            if int(time[0]) == 1 or int(time[0]) == 0:
                if 0 <= int(time[1]) <= 9:
                    if 0 <= int(time[2]) < 6:
                        if int(time[3]) >= 0:
                            passFlag = True
    except:
        myInputTime()
    if passFlag:
        d = {"FromTimeSelect": time}
        return d
    else:
        myInputTime()
def myInputStation():
    passFlag = False
    print("路線 1.三坑->南港 2.三坑->松山 3.三坑->基隆 4.三坑->台北")
    choose = input('路線選擇 : ')
    if int(choose)==1:
        d = {"ToStation": '1006'}
        passFlag=True
    if int(choose)==2:
        d = {"ToStation": '1007'}
        passFlag=True
    if int(choose)==3:
        d = {"ToStation": '1001'}
        passFlag=True
    if int(choose)==4:
        d = {"ToStation": '1008'}
        passFlag=True
    if passFlag:
        return d
    else:
        myInputStation()
def myGetDate():
    t=input('哪天的車 1.今天 2.明天 : ')
    if int(t)==1:
        now=date.today()
        d = {"searchdate": now}
        return d
    elif int(t)==2:
        now=date.today() + timedelta(days=1)
        d = {"searchdate": now}
        return d
    else:
        myGetDate()
load = {
    "FromCity": "0",
    "FromStation": "1029",  # 1006 南港
    "FromStationName": "0",
    "ToCity": "0",
    "ToStation": "1006",  # 1029 三坑 1001基隆
    "ToStationName": "0",
    "TrainClass": "2",
    "searchdate": "2019-04-10",
    "FromTimeSelect": "0820",
    "ToTimeSelect": "2359",
    "Timetype": "1"
}

try:
    load.update(myGetDate())
    load.update(myInputTime())
    load.update(myInputStation())
except:
    print("\n*********************")
    load.update(myGetDate())
    load.update(myInputTime())
    load.update(myInputStation())
res=requests.get('http://twtraffic.tra.gov.tw/twrail/TW_SearchResult.aspx',data=load)
soup=BeautifulSoup(res.text,'html.parser')
sp1=soup.find_all(['script'])
mstring=str(sp1.pop())
p1=mstring.find('"Train_Code"')
p2=mstring.find('},')
first='{   '+mstring[p1:p2+1]
departureTime=getValue(first,'departure')

dt = datetime.combine(date.today(),time(int(departureTime[0:2]), int(departureTime[2:4]))) - timedelta(minutes=22)
dt1 = dt+timedelta(minutes=17)
print('\n鬧鐘時間: '+dt.time().strftime('%H%M'))
print('出門時間: '+dt1.time().strftime('%H%M'))
print("發車時間: "+departureTime)
print("到達時間: "+(getValue(first,'arrival')))

