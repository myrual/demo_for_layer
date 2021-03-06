# -*- coding: UTF-8 -*-
import pygtk
pygtk.require('2.0')
import pywapi
import gtk


class NavBox:
    def __init__(self):
        self.Nav_Box = gtk.HBox()
        Nav_Label = gtk.Label("Navigation Label in box")
        Nav_Label.show()
        self.Nav_Box.add(Nav_Label)
        self.Nav_Box.show()
        return
class MessageBox:
    def __init__(self):
        self.MessageBox = gtk.HBox()
        Message_Label = gtk.Label("You should see all message here: email, qq, weibo, sms")
        Message_Label.show()
        self.MessageBox.add(Message_Label)
        self.MessageBox.show()
        return
class HelloNoteBook:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_border_width(10)
        
        self.NavBox = NavBox().Nav_Box
        self.NavBox.show()
        self.MessageBox = MessageBox().MessageBox
        self.MessageBox.show()
        self.NearByBox = gtk.HBox()
        self.NearByBox.show()
        self.ChangeBox = gtk.HBox()
        self.ChangeBox.show()
        self.MainMenu = gtk.Notebook()
        self.window.add(self.MainMenu)
        self.MainMenu.set_tab_pos(gtk.POS_LEFT)
        
        mylabel = gtk.Label("Navigation")
        self.MainMenu.append_page(self.NavBox, mylabel)
        
        mylabel = gtk.Label("Message")
        self.MainMenu.append_page(self.MessageBox, mylabel)
        mylabel = gtk.Label("Nearby")
        self.MainMenu.append_page(self.NearByBox, mylabel)
        mylabel = gtk.Label("Change")
        self.MainMenu.append_page(self.ChangeBox, mylabel)
        
        self.MainMenu.show()
        self.window.show()
        return
class StartFromWeather:
    def MakeWeatherInforBox(self, title, min, max, pic = None):
        wbox = gtk.VBox()
        title_label = gtk.Label(title)
        wbox.pack_start(title_label, True, True, 1)
        min_degree = gtk.Label(min+"C" + " ~ " + max+"C")
        wbox.pack_start(min_degree, True, True, 1)
        if(pic <> None):
            weather_pic = gtk.Image()
            weather_pic.set_from_file(pic)
            wbox.pack_start(weather_pic, True, True, 1)
        #max_degree = gtk.Label(max)
        #wbox.pack_start(max_degree, True, True, 1)
        wbox.show_all()
        return wbox
    def MakeWeatherInfoBox_Realtime(self, time):
        wbox = gtk.VBox()
        realtimeinfo = self.ExtractWeatherForButtonLabel(time)
        title_label = gtk.Label(realtimeinfo['time'])
        wbox.pack_start(title_label, True, True, 1)
        unicodelabel = realtimeinfo['low'] +"C" + " ~ " + realtimeinfo['high']+"C"
        min_degree = gtk.Label(unicodelabel)
        wbox.pack_start(min_degree, True, True, 1)
        #max_degree = gtk.Label(max)
        #wbox.pack_start(max_degree, True, True, 1)
        wbox.show_all()
        return wbox        
    def MakeButton(self, title, pic):
        wbox = gtk.VBox()
        intitle = gtk.Label(title)
        inpic = gtk.Image()
        inpic.set_from_file(pic)
        
        wbox.pack_start(intitle, True, True, 1)
        wbox.pack_start(inpic, True, True, 1)
        wbox.show_all()
        return wbox
    def GetWeather(self, city = 'tianjin', country = 'china'):
        self.google_result = pywapi.get_weather_from_google(city)
    def GetWeather_Current(self, city = 'tianjin', country='china'):
        self.current_conditions = self.google_result['current_conditions']
        self.currentdegree = self.current_conditions['temp_c']
        return
    def ChangeTempF2C(self, degree):
        return str((int(degree)-32)*5/9.00)[0:3]
    def ExtractWeatherForButtonLabel(self, day):
        weatherinfo = self.weather_forecast[day]
        low = self.ChangeTempF2C(weatherinfo['low'])
        high = self.ChangeTempF2C(weatherinfo['high'])
        time = weatherinfo['day_of_week']
        
        return {'low':low, 'high':high, 'time':time}
    def GetWeather_forecast(self):
        self.weather_forecast = self.google_result['forecasts']
    def GetCurrentTemperature(self):
        return self.currentdegree
    def __init__(self, city='tianjin'):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_border_width(10)

        self.ContentBox = gtk.Layout()
        self.ContentBox.show()
        self.window.add(self.ContentBox)
                
        self.weather = gtk.VBox()
        self.weather.show()



        
        title = gtk.Label("天气预报：" + city)
        title.show()
        self.weather.pack_start(title, True, True, 0)
        self.GetWeather(city)
        self.GetWeather_forecast()
        weather_info = gtk.HBox()
        weather_info.show_all()
        #today = self.MakeWeatherInforBox("今天", "-1", "10", "sunny.gif")
        today = self.MakeWeatherInfoBox_Realtime(0)
        #today.show()
        #tomorrow = self.MakeWeatherInforBox("明天", "1", "11", "heavyrain.gif")
        tomorrow =self.MakeWeatherInfoBox_Realtime(1)
        tomorrow.show()
        #theday_aftertmo = self.MakeWeatherInforBox("后天", "-1", "10", "cloudy.gif")
        theday_aftertmo = self.MakeWeatherInfoBox_Realtime(2)
        theday_aftertmo.show()
        weather_info.pack_start(today, True, True, 1)
        weather_info.pack_start(tomorrow, True, True, 1)
        weather_info.pack_start(theday_aftertmo, True, True, 1)
        
        self.weather.pack_start(weather_info, True, True, 1)
        
        Home_Next = gtk.HBox()
        HomeBtn = gtk.Button("主界面")
        SkipBtn = gtk.Button("下一步")
        
        SkipBtn.connect("clicked", self.SkipInWeather, "weather")
        HomeBtn.connect("clicked", self.GoHomeMenu, "Weather")
        Home_Next.pack_start(HomeBtn, True, True, 1)
        Home_Next.pack_start(SkipBtn, True, True, 1)
        Home_Next.show()
        Home_Next.show_all()
        self.weather.pack_start(Home_Next, True, True, 1)
        
        
        #blue tooth sync
        self.Phone = gtk.VBox()
        FindingPhone = gtk.Label("正在同步电话")
        self.Phone.pack_start(FindingPhone, True, True, 1)
        Btn = gtk.HBox()
        HomeBtn =  gtk.Button("主界面")
        SkipBtn = gtk.Button("下一步")
        SkipBtn.connect("clicked", self.SkipInPhoneSyn, "Phone")
        HomeBtn.connect("clicked", self.GoHomeMenu, "Inphone")
        Btn.pack_start(HomeBtn, True,True,1)
        Btn.pack_start(SkipBtn, True, True, 1)
        Btn.show_all()
        
        self.Phone.pack_start(Btn, True, True, 1)
        self.Phone.show_all()
        
        #driving box
        self.Nav = gtk.VBox()
        NavTitle = gtk.Label("开始导航")
        Btn = gtk.HBox()
        HomeBtn =  gtk.Button("主界面")
        HomeBtn.connect("clicked", self.GoHomeMenu, "Inphone")
        SkipBtn = gtk.Button("暂停")
        #SkipBtn.connect("clicked", self.SkipInPhoneSyn, "Phone")
        Btn.pack_start(HomeBtn, True,True,1)
        Btn.pack_start(SkipBtn, True, True, 1)
        Btn.show_all()
        self.Nav.pack_start(NavTitle, True, True, 1)
        self.Nav.pack_start(Btn, True, True, 1)
        self.Nav.show_all()
        SkipBtn.connect("clicked", self.SkipInNav, "inNav")
        
        self.MainMenu = gtk.VBox()
        self.GetWeather_Current(city)
        MainTitle = gtk.Label("主界面")
        MainBoxUp = gtk.HBox()
        MainBoxUp.show_all()

        MainBoxDown = gtk.HBox()
        MainBoxDown.show_all()
        
        WeatherBtn = gtk.Button()
        dis = self.MakeButton("当前温度："+self.GetCurrentTemperature(), "sunny.gif")
        #dis = self.MakeWeatherInforBox("今天", "-1", "10", "sunny.gif")
        WeatherBtn.add(dis)
        WeatherBtn.connect("clicked", self.ShowWeather, "Weather")
        
        SettingBtn = gtk.Button()
        dis = self.MakeButton("更改设置", "Settings.png")
        SettingBtn.add(dis)
        PhoneBtn = gtk.Button()
        dis = self.MakeButton("电话", "phone.gif")
        PhoneBtn.add(dis)
        PhoneBtn.connect("clicked", self.ShowPhone, "Phone")
        NavBtn = gtk.Button()
        dis = self.MakeButton("导航", "nav.jpg")
        NavBtn.add(dis)
        #NavBtn.set_image("nav.jpg")
        NavBtn.connect("clicked", self.ShowNav, "Nav")
        
        MainBoxDown.pack_start(WeatherBtn, True, True, 1)
        MainBoxDown.pack_start(SettingBtn, True, True, 1)        
        MainBoxUp.pack_start(NavBtn, True, True, 1)
        MainBoxUp.pack_start(PhoneBtn, True, True, 1)
        self.MainMenu.pack_start(MainBoxUp, True, True, 1)       
        self.MainMenu.pack_start(MainBoxDown, True, True, 1)

        self.MainMenu.show_all()
        
        self.window.show_all()
        self.window.show()

        
        self.ContentBox.put(self.weather, 0, 1)
        self.Phone.hide()
        self.ContentBox.put(self.Phone, 1, 1)
        self.MainMenu.hide()
        self.ContentBox.put(self.MainMenu, 1, 0)
        self.Nav.hide()
        self.ContentBox.put(self.Nav, 1, 2)
        self.ContentBox.show()
        return
    def ShowWeather(self, widget, data):
        self.MainMenu.hide()
        self.weather.show()
        
        return
    def ShowPhone(self, widget, data):
        self.MainMenu.hide()
        self.Phone.show()
        return
    def ShowNav(self, widget, data):
        self.MainMenu.hide()
        self.Nav.show()
        return
    def SkipInWeather(self, widget, data):
        self.weather.hide()
        self.Phone.show()
        """just process skip button in weather"""
        return
    def SkipInPhoneSyn(self, widget, data):
        self.Phone.hide()
        self.Nav.show()
        return
    def SkipInNav(self, widget, data):
        self.Nav.hide()
        self.MainMenu.show()
        return
    def GoHomeMenu(self, widget, data):
        for i in (self.Nav, self.Phone, self.weather):
            i.hide()
        self.MainMenu.show()
        return
class HellowFromGlade:
    def __init__(self):

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_border_width(10)

        self.ContentBox = gtk.Layout()
        self.ContentBox.show()
        self.window.add(self.ContentBox)

        #insert Box_entry for first menu user see
        self.Box_Entry = gtk.HBox(False, 0)
        self.Box_Entry.show()
        self.ContentBox.put(self.Box_Entry, 1, 1)
        #Menu button is an separate box
        self.Box_MainMenuButton = gtk.VBox(False, 0)
        self.Box_MainMenuButton.show()
        #First information after power on 
        self.Box_MainMenuInfor = gtk.VBox(False, 0)
        self.Box_MainMenuInfor.show()

        self.Box_Entry.pack_start(self.Box_MainMenuButton, True, True, 0)
        self.Box_Entry.pack_start(self.Box_MainMenuInfor, True, True, 0)


        self.Btn_Nav = gtk.Button("button_nav")
        self.Btn_Nav.connect("clicked", self.Button_Nav, "pressed")
        self.Btn_Nav.show()

        self.Btn_Message = gtk.Button("button_message")
        self.Btn_Message.connect("clicked", self.Button_Message, "pressed")
        self.Btn_Message.show()

        self.Btn_NearBy = gtk.Button("button_nearby")
        self.Btn_NearBy.connect("clicked", self.Button_Near, "pressed")
        self.Btn_NearBy.show()

        self.Btn_Change = gtk.Button("button_changeSetting")
        self.Btn_Change.connect("clicked", self.Button_changed, "pressed")
        self.Btn_Change.show()

        self.Box_MainMenuButton.pack_start(self.Btn_Nav, True, True, 0)
        self.Box_MainMenuButton.pack_start(self.Btn_Message, True, True, 0)
        self.Box_MainMenuButton.pack_start(self.Btn_NearBy, True, True, 0)
        self.Box_MainMenuButton.pack_start(self.Btn_Change, True, True, 0)

        #init all SubMenu box here
        self.NavBox = gtk.Button("Nav box")
        self.MessageBox = gtk.Button("message box")
        self.NearByBox = gtk.Button("Nearby box")
        self.SettingBox = gtk.Button("Setting")
        self.BtnBackToMain = gtk.Button("Back to main")
        self.BtnBackToMain.connect("clicked", self.BackToMainEntry, "home")
        self.ContentBox.put(self.BtnBackToMain, 1, 1)
        for i in (self.NavBox, self.MessageBox, self.NearByBox, self.SettingBox):
            i.connect("clicked", self.BackToMainEntry, "pressed")
            self.ContentBox.put(i, 1, 30)
        return
    def BackToMainEntry(self, widget, data):
        self.HideAllBox()
        self.BtnBackToMain.hide()
        self.Box_Entry.show()
        return
    def HideAllBox(self):
        for i in (self.Box_Entry, self.NavBox, self.MessageBox, self.NearByBox, self.SettingBox):
            i.hide()
        return

    def Button_Nav(self, widget, data):
        self.HideAllBox()
        self.BtnBackToMain.show()
        self.NavBox.show()
        print "You pressed Nav button"
        return

    def Button_Message(self, widget, data):
        self.HideAllBox()
        self.BtnBackToMain.show()
        self.MessageBox.show()
        print "You want to see message"
        return
    def Button_changed(self, widget, data):
        self.HideAllBox()
        self.BtnBackToMain.show()
        self.SettingBox.show()
        print "Play video, audio, fm, online radio, podcast"
        return
    def Button_Near(self, widget, data):
        self.HideAllBox()
        self.BtnBackToMain.show()
        self.NearByBox.show()
        print "Play video, audio, fm, online radio, podcast"
        return       
if __name__ == "__main__":
    tuto = StartFromWeather('tianjin')
    tuto.window.show()
    gtk.main()
#Do not change spaces! description page is here#
