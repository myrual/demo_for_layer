#	Project Name	:	Visual Python IDE for 2.6#	Date	        :	13-12-2009#	Author		    :	macrocoders team#	Contact		    :	macrocoders@gmail.com#	Web			    :	http://visualpython.org#	Python Ver.     :	2.6# -*- coding: utf-8 -*-from Tkinter import *from tkMessageBox import *# -- Do not change. You may experience problems with the design file. -- #
#
# -*- coding: UTF-8 -*-
import pygtk
pygtk.require('2.0')
import gtk

class HellowFromGlade:
    def __init__(self):
        self.gladefile = "demo_for_layer.glade"
        self.gtkbuilder = gtk.Builder()
        self.gtkbuilder.add_from_file(self.gladefile)
        self.window = self.gtkbuilder.get_object("window1")
        self.Btn_Nav = self.gtkbuilder.get_object("button_nav")
        self.Btn_Nav.connect("clicked", self.Button_Nav, "pressed")
        self.Btn_Message = self.gtkbuilder.get_object("button_message")
        self.Btn_Message.connect("clicked", self.Button_Message, "pressed")
        self.Btn_NearBy = self.gtkbuilder.get_object("button_nearby")
        self.Btn_NearBy.connect("clicked", self.Button_Near, "pressed")
        self.Btn_Change = self.gtkbuilder.get_object("button_changeSetting")
        self.Btn_Change.connect("clicked", self.Button_changed, "pressed")
        self.ContentBox = gtk.Layout()
        self.ContentBox.show()
        self.MainMenuBox = self.gtkbuilder.get_object("Main_hbox")
        self.MainMenuBox.pack_start(self.ContentBox, True, True, 0)



        #init all SubMenu box here
        self.NavBox = gtk.Button("Nav box")
        self.MessageBox = gtk.Button("message box")
        self.NearByBox = gtk.Button("Nearby box")
        self.SettingBox = gtk.Button("Setting")
        return
    def HideAllBox(self):
        self.NavBox.hide()
        self.MessageBox.hide()
        self.NearByBox.hide()
        self.SettingBox.hide()
        return

    def Button_Nav(self, widget, data):
        self.HideAllBox()
        self.NavBox.show()
        self.ContentBox.put(self.NavBox, 0, 0)
        print "You pressed Nav button"
        return

    def Button_Message(self, widget, data):
        self.HideAllBox()
        self.MessageBox.show()
        self.ContentBox.put(self.MessageBox, 0, 30)
        print "You want to see message"
        return
    def Button_changed(self, widget, data):
        self.HideAllBox()
        self.SettingBox.show()
        self.ContentBox.put(self.SettingBox, 30, 0)
        print "Play video, audio, fm, online radio, podcast"
        return
    def Button_Near(self, widget, data):
        self.HideAllBox()
        self.NearByBox.show()
        self.ContentBox.put(self.NearByBox, 30, 30)
        print "Play video, audio, fm, online radio, podcast"
        return       
if __name__ == "__main__":
    tuto = HellowFromGlade()
    tuto.window.show()
    gtk.main()
#Do not change spaces! description page is here#
