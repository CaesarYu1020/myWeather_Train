from mWeather import HowsWeather
from mTrain import myTrain

run=True
while(run):
    print('**********************')
    print('請選擇你的功能 W:台北/基隆天氣週報 T:火車、鬧鐘時刻 Q:離開程式')
    print('**********************')
    func=input('選擇 : ')
    if func=='w' or func=="W":
        HowsWeather('台北')
        HowsWeather('基隆')
    if func=='t' or func=="T":
        myTrain()
    if func == 'q' or func == "Q":
        run=False
