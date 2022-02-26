# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################


from email import message
from enum import Flag
from msilib.schema import SelfReg
#from typing_extensions import Self
import wx
import wx.xrc
import threading
from post_shool import Shool_Wif
###########################################################################
## Class 菜单
###########################################################################

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class 菜单
###########################################################################

class Shool_Gui( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"校园网认证", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"cook设置", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Referer设置", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menubar1.Append( self.m_menu1, u"首选项" )

		self.SetMenuBar( self.m_menubar1 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"账号·", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gSizer5.Add( self.m_staticText4, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtr_accout = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtr_accout, 0, wx.ALIGN_CENTER|wx.ALL|wx.RIGHT, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gSizer5.Add( self.m_staticText5, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtr_pwd = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtr_pwd, 0, wx.ALL, 5 )


		wSizer1.Add( gSizer5, 1, wx.EXPAND, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_button5, 0, wx.ALL, 5 )


		self.SetSizer( wSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.setting, id = self.m_menuItem1.GetId() )
		self.m_button5.Bind( wx.EVT_BUTTON, self.B_Longin )

		with open("src/accot","r") as accot:
			
			self.a1 = accot.read()
			self.m_textCtr_accout.SetValue(self.a1)
		with open("src/pwd","r") as pwd:
			self.a2 = pwd.read()
			self.m_textCtr_pwd.SetValue(self.a2)
		
	def __del__( self ):
		pass

	def open_if(self):
		pass
		
	# Virtual event handlers, override them in your derived class
	def setting( self, event ):
		event.Skip()

	def B_Longin( self, event ):#登录操作
		self.accot,self.pwd  = self.m_textCtr_accout.GetValue(),self.m_textCtr_pwd.GetValue()
		with open("src/accot","w") as accot:
			accot.write(str(self.accot))
		with open("src/pwd","w") as pwd:
			pwd.write(str(self.pwd))


		with open("src/accot","r") as accot:
			self.ac = accot.read()
			print(self.ac)
		with open("src/pwd","r") as pwd:
			self.pw = pwd.read()
			print(self.pw)
		S_longin = Shool_Wif(self.ac,self.pw)
		S_longin.open_config()
		stat = S_longin.shool_post()
		if(stat == True):
			wx.MessageBox(u"登录成功", u"成功")
        	
		else:
			wx.MessageBox(u"登录失败",u"成功")


		


		


if __name__=="__main__":
    app = wx.App()
    fram = Shool_Gui(None)
    fram.Show(True)
    app.MainLoop()

    #th = threading.Thread()
