#	Project Name	:	Visual Python IDE for 2.6#	Date	        :	13-12-2009#	Author		    :	macrocoders team#	Contact		    :	macrocoders@gmail.com#	Web			    :	http://visualpython.org#	Python Ver.     :	2.6# -*- coding: utf-8 -*-from Tkinter import *from tkMessageBox import *# -- Do not change. You may experience problems with the design file. -- #
#
# -*- coding: UTF-8 -*-
import pygtk
pygtk.require('2.0')
import gtk

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
        for i in (self.NavBox, self.MessageBox, self.NearByBox, self.SettingBox):
            i.connect("clicked", self.BackToMainEntry, "pressed")
            self.ContentBox.put(i, 1, 1)
        return
    def BackToMainEntry(self, widget, data):
        self.HideAllBox()
        self.Box_Entry.show()
        return
    def HideAllBox(self):
        self.Box_Entry.hide()
        self.NavBox.hide()
        self.MessageBox.hide()
        self.NearByBox.hide()
        self.SettingBox.hide()
        return

    def Button_Nav(self, widget, data):
        self.HideAllBox()
        self.NavBox.show()
        print "You pressed Nav button"
        return

    def Button_Message(self, widget, data):
        self.HideAllBox()
        self.MessageBox.show()
        print "You want to see message"
        return
    def Button_changed(self, widget, data):
        self.HideAllBox()
        self.SettingBox.show()
        print "Play video, audio, fm, online radio, podcast"
        return
    def Button_Near(self, widget, data):
        self.HideAllBox()
        self.NearByBox.show()
        print "Play video, audio, fm, online radio, podcast"
        return       
if __name__ == "__main__":
    tuto = HellowFromGlade()
    tuto.window.show()
    gtk.main()
#Do not change spaces! description page is here#
