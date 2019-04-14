from bs4 import BeautifulSoup
from urllib.request import urlopen
from prettytable import PrettyTable as pt

def HowsWeather(locate):
    if locate=='基隆':
        URL='https://www.cwb.gov.tw/V7/forecast/taiwan/inc/city/Keelung_City.htm'
    if locate=='台北':
        URL='https://www.cwb.gov.tw/V7/forecast/taiwan/inc/city/Taipei_City.htm'
    html=urlopen(URL).read()
    soup=BeautifulSoup(html,'html.parser')
    sp1=soup.find_all(['th'])
    sp2=soup.find_all(['td'])
    sp3 = soup.find_all('img', alt=True)
    alt = [0]
    for t in sp3:
        alt.append(t['alt'])
    for i in range(0, len(alt)):
        if '雨' in str(alt[i]):
            alt[i] = '雨'
        elif '晴' in str(alt[i]):
            alt[i] = '晴'
        # elif '陰' in str(alt[i]):
        #     alt[i] = '陰'
    data1=[];
    data2=[];
    for text in sp1:
        data1.append(text.getText())
    for text2 in sp2:
        temp=text2.getText().replace('\n','');
        temp = temp.replace('\t', '')
        temp=temp.replace(' ','')
        data2.append(temp)
    data3=data2[7:14]
    data2.insert(0,'')
    data3.insert(0,'')
    myTable=pt()
    myTable.add_column(data1[0],[data1[8],data1[9]])
    for i in range(1,8):
        myTable.add_column (''+str(data1[i]),[str(data2[i])+'('+str(alt[i])+")",str(data3[i])+'('+str(alt[i+7])+")"])
    print(myTable)