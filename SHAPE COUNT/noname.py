# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class frame_tugas
###########################################################################

class frame_tugas ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1500,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.panel_utama = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_utama.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer1.Add( self.panel_utama, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.login_frameSize )
		self.panel_utama.Bind( wx.EVT_SIZE, self.size_frameLogin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def login_frameSize( self, event ):
		event.Skip()

	def size_frameLogin( self, event ):
		event.Skip()


###########################################################################
## Class D_af
###########################################################################

class D_af ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1500,800 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer397 = wx.BoxSizer( wx.VERTICAL )


		bSizer397.Add( ( 0, 120), 0, wx.EXPAND, 5 )

		self.m_staticText519 = wx.StaticText( self, wx.ID_ANY, u"DAFTAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText519.Wrap( -1 )

		self.m_staticText519.SetFont( wx.Font( 28, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText519.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer397.Add( self.m_staticText519, 0, wx.ALIGN_CENTER, 5 )

		fgSizer236 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer236.SetFlexibleDirection( wx.BOTH )
		fgSizer236.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText520 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText520.Wrap( -1 )

		self.m_staticText520.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )
		self.m_staticText520.SetMinSize( wx.Size( -1,35 ) )

		fgSizer236.Add( self.m_staticText520, 0, wx.ALL, 5 )

		self.d_nama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		self.d_nama.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer236.Add( self.d_nama, 0, wx.ALL, 5 )

		self.m_staticText521 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText521.Wrap( -1 )

		self.m_staticText521.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )
		self.m_staticText521.SetMinSize( wx.Size( -1,35 ) )

		fgSizer236.Add( self.m_staticText521, 0, wx.ALL, 5 )

		self.d_alamat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		self.d_alamat.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer236.Add( self.d_alamat, 0, wx.ALL, 5 )

		self.m_staticText522 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText522.Wrap( -1 )

		self.m_staticText522.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )
		self.m_staticText522.SetMinSize( wx.Size( -1,35 ) )

		fgSizer236.Add( self.m_staticText522, 0, wx.ALL, 5 )

		self.d_email = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		self.d_email.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer236.Add( self.d_email, 0, wx.ALL, 5 )

		self.m_staticText523 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText523.Wrap( -1 )

		self.m_staticText523.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )
		self.m_staticText523.SetMinSize( wx.Size( -1,35 ) )

		fgSizer236.Add( self.m_staticText523, 0, wx.ALL, 5 )

		self.d_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		self.d_username.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer236.Add( self.d_username, 0, wx.ALL, 5 )

		self.m_staticText524 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText524.Wrap( -1 )

		self.m_staticText524.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )
		self.m_staticText524.SetMinSize( wx.Size( -1,35 ) )

		fgSizer236.Add( self.m_staticText524, 0, wx.ALL, 5 )

		self.d_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), wx.TE_PASSWORD )
		self.d_password.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer236.Add( self.d_password, 0, wx.ALL, 5 )


		bSizer397.Add( fgSizer236, 0, wx.ALIGN_CENTER, 5 )

		bSizer398 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1667 = wx.Button( self, wx.ID_ANY, u"Daftar", wx.DefaultPosition, wx.Size( 200,35 ), 0 )
		self.m_button1667.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )

		bSizer398.Add( self.m_button1667, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		fgSizer237 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer237.SetFlexibleDirection( wx.BOTH )
		fgSizer237.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText526 = wx.StaticText( self, wx.ID_ANY, u"Sudah punya akun?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText526.Wrap( -1 )

		self.m_staticText526.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )
		self.m_staticText526.SetMinSize( wx.Size( -1,40 ) )

		fgSizer237.Add( self.m_staticText526, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText527 = wx.StaticText( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText527.Wrap( -1 )

		self.m_staticText527.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )
		self.m_staticText527.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_staticText527.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		fgSizer237.Add( self.m_staticText527, 0, wx.ALL, 5 )


		bSizer398.Add( fgSizer237, 0, wx.ALIGN_CENTER, 5 )


		bSizer397.Add( bSizer398, 0, wx.ALIGN_CENTER, 5 )


		self.SetSizer( bSizer397 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.keluar_daf )
		self.m_button1667.Bind( wx.EVT_BUTTON, self.tombol_daftar )
		self.m_staticText527.Bind( wx.EVT_LEFT_UP, self.t_masuk )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def keluar_daf( self, event ):
		event.Skip()

	def tombol_daftar( self, event ):
		event.Skip()

	def t_masuk( self, event ):
		event.Skip()


###########################################################################
## Class m_gin
###########################################################################

class m_gin ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )


		bSizer2.Add( ( 0, 190), 0, wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"LOGIN NOW!!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 48, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.input_username = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		self.input_username.SetMinSize( wx.Size( 200,35 ) )

		fgSizer1.Add( self.input_username, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.input_password = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), wx.TE_PASSWORD )
		self.input_password.SetMinSize( wx.Size( 200,35 ) )

		fgSizer1.Add( self.input_password, 0, wx.ALL, 5 )

		bSizer395 = wx.BoxSizer( wx.VERTICAL )


		fgSizer1.Add( bSizer395, 1, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( fgSizer1 )
		self.m_panel2.Layout()
		fgSizer1.Fit( self.m_panel2 )
		bSizer2.Add( self.m_panel2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.Size( 150,40 ), 0 )
		self.m_button1.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button1.SetForegroundColour( wx.Colour( 0, 54, 98 ) )
		self.m_button1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer2.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		fgSizer234 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer234.SetFlexibleDirection( wx.BOTH )
		fgSizer234.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText514 = wx.StaticText( self, wx.ID_ANY, u"Apakah sudah punya akun?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText514.Wrap( -1 )

		self.m_staticText514.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer234.Add( self.m_staticText514, 0, wx.ALL, 5 )

		self.m_staticText515 = wx.StaticText( self, wx.ID_ANY, u"Daftar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText515.Wrap( -1 )

		self.m_staticText515.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText515.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer234.Add( self.m_staticText515, 0, wx.ALL, 5 )


		bSizer2.Add( fgSizer234, 1, wx.ALIGN_CENTER, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.tombol_login )
		self.m_staticText515.Bind( wx.EVT_LEFT_UP, self.tombol_daftar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tombol_login( self, event ):
		event.Skip()

	def tombol_daftar( self, event ):
		event.Skip()


###########################################################################
## Class panel_dashbord
###########################################################################

class panel_dashbord ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1500,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		fgSizer43 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer43.SetFlexibleDirection( wx.BOTH )
		fgSizer43.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"SHAPE COUNT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 26, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer43.Add( self.m_staticText4, 0, wx.ALL, 5 )


		fgSizer43.Add( ( 500, 0), 1, wx.EXPAND, 5 )


		fgSizer43.Add( ( 600, 0), 1, wx.EXPAND, 5 )

		self.log_out = wx.StaticText( self, wx.ID_ANY, u"LOG OUT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.log_out.Wrap( -1 )

		self.log_out.SetFont( wx.Font( 26, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.log_out.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer43.Add( self.log_out, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		fgSizer43.Add( ( 25, 0), 1, wx.EXPAND, 5 )


		bSizer3.Add( fgSizer43, 1, wx.EXPAND, 5 )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Keliling Bangun Datar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button12 = wx.Button( self.m_panel3, wx.ID_ANY, u"Persegi", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button12.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		fgSizer2.Add( self.m_button12, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 15, 0), 1, wx.EXPAND, 5 )

		self.m_button18 = wx.Button( self.m_panel3, wx.ID_ANY, u"Lingkaran", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button18.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button18.SetBackgroundColour( wx.Colour( 181, 0, 0 ) )

		fgSizer2.Add( self.m_button18, 0, wx.ALL, 5 )

		self.m_button13 = wx.Button( self.m_panel3, wx.ID_ANY, u"Persegi Panjang", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button13.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button13.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button13.SetBackgroundColour( wx.Colour( 0, 176, 0 ) )

		fgSizer2.Add( self.m_button13, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button14 = wx.Button( self.m_panel3, wx.ID_ANY, u"Segitiga", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button14.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button14.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		fgSizer2.Add( self.m_button14, 0, wx.ALL, 5 )

		self.m_button15 = wx.Button( self.m_panel3, wx.ID_ANY, u"Belah Ketupat", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button15.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button15.SetBackgroundColour( wx.Colour( 0, 240, 0 ) )

		fgSizer2.Add( self.m_button15, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button16 = wx.Button( self.m_panel3, wx.ID_ANY, u"Trapesium", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button16.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button16.SetBackgroundColour( wx.Colour( 255, 108, 108 ) )

		fgSizer2.Add( self.m_button16, 0, wx.ALL, 5 )

		self.m_button17 = wx.Button( self.m_panel3, wx.ID_ANY, u"Layang-Layang", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button17.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button17.SetBackgroundColour( wx.Colour( 151, 255, 151 ) )

		fgSizer2.Add( self.m_button17, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button19 = wx.Button( self.m_panel3, wx.ID_ANY, u"Jajar Genjang", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button19.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button19.SetBackgroundColour( wx.Colour( 255, 200, 200 ) )

		fgSizer2.Add( self.m_button19, 0, wx.ALL, 5 )


		bSizer5.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Luas Bangun Datar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		fgSizer21 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button121 = wx.Button( self.m_panel3, wx.ID_ANY, u"Persegi", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button121.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button121.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button121.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		fgSizer21.Add( self.m_button121, 0, wx.ALL, 5 )


		fgSizer21.Add( ( 15, 0), 1, wx.EXPAND, 5 )

		self.m_button181 = wx.Button( self.m_panel3, wx.ID_ANY, u"Lingkaran", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button181.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button181.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button181.SetBackgroundColour( wx.Colour( 181, 0, 0 ) )

		fgSizer21.Add( self.m_button181, 0, wx.ALL, 5 )

		self.m_button131 = wx.Button( self.m_panel3, wx.ID_ANY, u"Persegi Panjang", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button131.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button131.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button131.SetBackgroundColour( wx.Colour( 0, 176, 0 ) )

		fgSizer21.Add( self.m_button131, 0, wx.ALL, 5 )


		fgSizer21.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button141 = wx.Button( self.m_panel3, wx.ID_ANY, u"Segitiga", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button141.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button141.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button141.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		fgSizer21.Add( self.m_button141, 0, wx.ALL, 5 )

		self.m_button151 = wx.Button( self.m_panel3, wx.ID_ANY, u"Belah Ketupat", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button151.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button151.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button151.SetBackgroundColour( wx.Colour( 0, 240, 0 ) )

		fgSizer21.Add( self.m_button151, 0, wx.ALL, 5 )


		fgSizer21.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button161 = wx.Button( self.m_panel3, wx.ID_ANY, u"Trapesium", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button161.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button161.SetBackgroundColour( wx.Colour( 255, 108, 108 ) )

		fgSizer21.Add( self.m_button161, 0, wx.ALL, 5 )

		self.m_button171 = wx.Button( self.m_panel3, wx.ID_ANY, u"Layang-Layang", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button171.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button171.SetBackgroundColour( wx.Colour( 151, 255, 151 ) )

		fgSizer21.Add( self.m_button171, 0, wx.ALL, 5 )


		fgSizer21.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button191 = wx.Button( self.m_panel3, wx.ID_ANY, u"Jajar Genjang", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button191.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button191.SetBackgroundColour( wx.Colour( 255, 200, 200 ) )

		fgSizer21.Add( self.m_button191, 0, wx.ALL, 5 )


		bSizer51.Add( fgSizer21, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer51, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer4 )
		self.m_panel3.Layout()
		bSizer4.Fit( self.m_panel3 )
		self.m_notebook1.AddPage( self.m_panel3, u"Kalkulator Bangun Datar", True )
		self.m_panel4 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Luas Permukaan Bangun Ruang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button122 = wx.Button( self.m_panel4, wx.ID_ANY, u"Kubus", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button122.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button122.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button122.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		fgSizer22.Add( self.m_button122, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 15, 0), 1, wx.EXPAND, 5 )

		self.m_button182 = wx.Button( self.m_panel4, wx.ID_ANY, u"Balok", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button182.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button182.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button182.SetBackgroundColour( wx.Colour( 181, 0, 0 ) )

		fgSizer22.Add( self.m_button182, 0, wx.ALL, 5 )

		self.m_button132 = wx.Button( self.m_panel4, wx.ID_ANY, u"Prisma Segitiga", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button132.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button132.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button132.SetBackgroundColour( wx.Colour( 0, 176, 0 ) )

		fgSizer22.Add( self.m_button132, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button142 = wx.Button( self.m_panel4, wx.ID_ANY, u"Prisma Segiempat", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button142.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button142.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button142.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		fgSizer22.Add( self.m_button142, 0, wx.ALL, 5 )

		self.m_button152 = wx.Button( self.m_panel4, wx.ID_ANY, u"Kerucut", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button152.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button152.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button152.SetBackgroundColour( wx.Colour( 0, 240, 0 ) )

		fgSizer22.Add( self.m_button152, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button162 = wx.Button( self.m_panel4, wx.ID_ANY, u"Bola", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button162.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button162.SetBackgroundColour( wx.Colour( 255, 108, 108 ) )

		fgSizer22.Add( self.m_button162, 0, wx.ALL, 5 )

		self.luas_limasSegiempat = wx.Button( self.m_panel4, wx.ID_ANY, u"Limas Segiempat", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.luas_limasSegiempat.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.luas_limasSegiempat.SetBackgroundColour( wx.Colour( 151, 255, 151 ) )

		fgSizer22.Add( self.luas_limasSegiempat, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button192 = wx.Button( self.m_panel4, wx.ID_ANY, u"Tabung", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button192.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button192.SetBackgroundColour( wx.Colour( 255, 200, 200 ) )

		fgSizer22.Add( self.m_button192, 0, wx.ALL, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )

		self.m_staticText52 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Volume Bangun Ruang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		self.m_staticText52.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText52.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText52, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer521 = wx.BoxSizer( wx.VERTICAL )

		fgSizer221 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer221.SetFlexibleDirection( wx.BOTH )
		fgSizer221.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button1221 = wx.Button( self.m_panel4, wx.ID_ANY, u"Kubus", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button1221.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button1221.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button1221.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )

		fgSizer221.Add( self.m_button1221, 0, wx.ALL, 5 )


		fgSizer221.Add( ( 15, 0), 1, wx.EXPAND, 5 )

		self.m_button1821 = wx.Button( self.m_panel4, wx.ID_ANY, u"Balok", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button1821.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button1821.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button1821.SetBackgroundColour( wx.Colour( 181, 0, 0 ) )

		fgSizer221.Add( self.m_button1821, 0, wx.ALL, 5 )

		self.m_button1321 = wx.Button( self.m_panel4, wx.ID_ANY, u"Prisma Segitiga", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button1321.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button1321.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button1321.SetBackgroundColour( wx.Colour( 0, 176, 0 ) )

		fgSizer221.Add( self.m_button1321, 0, wx.ALL, 5 )


		fgSizer221.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button1421 = wx.Button( self.m_panel4, wx.ID_ANY, u"Prisma Segiempat", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button1421.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button1421.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button1421.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		fgSizer221.Add( self.m_button1421, 0, wx.ALL, 5 )

		self.m_button1521 = wx.Button( self.m_panel4, wx.ID_ANY, u"Kerucut", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button1521.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button1521.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button1521.SetBackgroundColour( wx.Colour( 0, 240, 0 ) )

		fgSizer221.Add( self.m_button1521, 0, wx.ALL, 5 )


		fgSizer221.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button1621 = wx.Button( self.m_panel4, wx.ID_ANY, u"Bola", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button1621.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button1621.SetBackgroundColour( wx.Colour( 255, 108, 108 ) )

		fgSizer221.Add( self.m_button1621, 0, wx.ALL, 5 )

		self.volume_limasSegiempat = wx.Button( self.m_panel4, wx.ID_ANY, u"Limas Segiempat", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.volume_limasSegiempat.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.volume_limasSegiempat.SetBackgroundColour( wx.Colour( 151, 255, 151 ) )

		fgSizer221.Add( self.volume_limasSegiempat, 0, wx.ALL, 5 )


		fgSizer221.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button1921 = wx.Button( self.m_panel4, wx.ID_ANY, u"Tabung", wx.DefaultPosition, wx.Size( 180,40 ), 0 )
		self.m_button1921.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_button1921.SetBackgroundColour( wx.Colour( 255, 200, 200 ) )

		fgSizer221.Add( self.m_button1921, 0, wx.ALL, 5 )


		bSizer521.Add( fgSizer221, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer521, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer41 )
		self.m_panel4.Layout()
		bSizer41.Fit( self.m_panel4 )
		self.m_notebook1.AddPage( self.m_panel4, u"Kalkulator Bangun Ruang", False )
		self.m_panel5 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer79 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel8 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 7, 2, 0, 0 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_datar = wx.Button( self.m_panel8, wx.ID_ANY, u"Bangun Datar", wx.DefaultPosition, wx.Size( 180,50 ), 0 )
		self.tombol_datar.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_datar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_datar.SetBackgroundColour( wx.Colour( 0, 198, 198 ) )

		gSizer1.Add( self.tombol_datar, 0, wx.ALL, 5 )

		self.tombol_ruang = wx.Button( self.m_panel8, wx.ID_ANY, u"Bangun Ruang", wx.DefaultPosition, wx.Size( 180,50 ), 0 )
		self.tombol_ruang.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_ruang.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_ruang.SetBackgroundColour( wx.Colour( 0, 128, 128 ) )

		gSizer1.Add( self.tombol_ruang, 0, wx.ALL, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel8.SetSizer( gSizer1 )
		self.m_panel8.Layout()
		gSizer1.Fit( self.m_panel8 )
		bSizer79.Add( self.m_panel8, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.m_panel5.SetSizer( bSizer79 )
		self.m_panel5.Layout()
		bSizer79.Fit( self.m_panel5 )
		self.m_notebook1.AddPage( self.m_panel5, u"Katalog Rumus", False )
		self.m_panel6 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer791 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel81 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer11 = wx.GridSizer( 7, 2, 0, 0 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_datar1 = wx.Button( self.m_panel81, wx.ID_ANY, u"Bangun Datar", wx.DefaultPosition, wx.Size( 180,50 ), 0 )
		self.tombol_datar1.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_datar1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_datar1.SetBackgroundColour( wx.Colour( 0, 198, 198 ) )

		gSizer11.Add( self.tombol_datar1, 0, wx.ALL, 5 )

		self.tombol_ruang1 = wx.Button( self.m_panel81, wx.ID_ANY, u"Bangun Ruang", wx.DefaultPosition, wx.Size( 180,50 ), 0 )
		self.tombol_ruang1.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_ruang1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_ruang1.SetBackgroundColour( wx.Colour( 0, 128, 128 ) )

		gSizer11.Add( self.tombol_ruang1, 0, wx.ALL, 5 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel81.SetSizer( gSizer11 )
		self.m_panel81.Layout()
		gSizer11.Fit( self.m_panel81 )
		bSizer791.Add( self.m_panel81, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.m_panel6.SetSizer( bSizer791 )
		self.m_panel6.Layout()
		bSizer791.Fit( self.m_panel6 )
		self.m_notebook1.AddPage( self.m_panel6, u"Spesifikasi", False )
		self.m_panel10 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 5, 1, 0, 0 )


		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_cat = wx.Button( self.m_panel10, wx.ID_ANY, u"Buka Catatan", wx.DefaultPosition, wx.Size( 180,50 ), 0 )
		self.tombol_cat.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_cat.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_cat.SetBackgroundColour( wx.Colour( 0, 198, 198 ) )

		gSizer3.Add( self.tombol_cat, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel10.SetSizer( gSizer3 )
		self.m_panel10.Layout()
		gSizer3.Fit( self.m_panel10 )
		self.m_notebook1.AddPage( self.m_panel10, u"Catatan", False )

		bSizer3.Add( self.m_notebook1, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		# Connect Events
		self.log_out.Bind( wx.EVT_LEFT_UP, self.tombol_logout )
		self.m_button12.Bind( wx.EVT_BUTTON, self.persegi_keliling )
		self.m_button18.Bind( wx.EVT_BUTTON, self.lingkaran_keliling )
		self.m_button13.Bind( wx.EVT_BUTTON, self.persegi_panjang_keliling )
		self.m_button14.Bind( wx.EVT_BUTTON, self.segitiga_keliling )
		self.m_button15.Bind( wx.EVT_BUTTON, self.belah_ketupat_keliling )
		self.m_button16.Bind( wx.EVT_BUTTON, self.trapesium_keliling )
		self.m_button17.Bind( wx.EVT_BUTTON, self.layang_keliling )
		self.m_button19.Bind( wx.EVT_BUTTON, self.jajar_genjang_keliling )
		self.m_button121.Bind( wx.EVT_BUTTON, self.persegi_luas )
		self.m_button181.Bind( wx.EVT_BUTTON, self.lingkaran_keliling_luas )
		self.m_button131.Bind( wx.EVT_BUTTON, self.persegi_panjang_luas )
		self.m_button141.Bind( wx.EVT_BUTTON, self.segitiga_keliling_luas )
		self.m_button151.Bind( wx.EVT_BUTTON, self.belah_ketupat_luas )
		self.m_button161.Bind( wx.EVT_BUTTON, self.trapesium_keliling_luas )
		self.m_button171.Bind( wx.EVT_BUTTON, self.layang_keliling_luas )
		self.m_button191.Bind( wx.EVT_BUTTON, self.jajar_genjang_keliling_luas )
		self.m_button122.Bind( wx.EVT_BUTTON, self.kubus_luas )
		self.m_button182.Bind( wx.EVT_BUTTON, self.balok_luas )
		self.m_button132.Bind( wx.EVT_BUTTON, self.prisma_segitiga_luas )
		self.m_button142.Bind( wx.EVT_BUTTON, self.prisma_segiempat_luas )
		self.m_button152.Bind( wx.EVT_BUTTON, self.kerucut_luas )
		self.m_button162.Bind( wx.EVT_BUTTON, self.bola_luas )
		self.luas_limasSegiempat.Bind( wx.EVT_BUTTON, self.limas_segiempat_LuasP )
		self.m_button192.Bind( wx.EVT_BUTTON, self.tabung_luas )
		self.m_button1221.Bind( wx.EVT_BUTTON, self.kubus_volume )
		self.m_button1821.Bind( wx.EVT_BUTTON, self.balok_volume )
		self.m_button1321.Bind( wx.EVT_BUTTON, self.prisma_segitiga_volume )
		self.m_button1421.Bind( wx.EVT_BUTTON, self.prisma_segiempat_volume )
		self.m_button1521.Bind( wx.EVT_BUTTON, self.kerucut_volume )
		self.m_button1621.Bind( wx.EVT_BUTTON, self.bola_volume )
		self.volume_limasSegiempat.Bind( wx.EVT_BUTTON, self.limas_segiempat_volume )
		self.m_button1921.Bind( wx.EVT_BUTTON, self.tabung_volume )
		self.tombol_datar.Bind( wx.EVT_BUTTON, self.tombol_bang_datar )
		self.tombol_ruang.Bind( wx.EVT_BUTTON, self.tombol_bang_ruang )
		self.tombol_datar1.Bind( wx.EVT_BUTTON, self.tombol_bang_datar1 )
		self.tombol_ruang1.Bind( wx.EVT_BUTTON, self.tombol_bang_ruang1 )
		self.tombol_cat.Bind( wx.EVT_BUTTON, self.tombol_buka_catatan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tombol_logout( self, event ):
		event.Skip()

	def persegi_keliling( self, event ):
		event.Skip()

	def lingkaran_keliling( self, event ):
		event.Skip()

	def persegi_panjang_keliling( self, event ):
		event.Skip()

	def segitiga_keliling( self, event ):
		event.Skip()

	def belah_ketupat_keliling( self, event ):
		event.Skip()

	def trapesium_keliling( self, event ):
		event.Skip()

	def layang_keliling( self, event ):
		event.Skip()

	def jajar_genjang_keliling( self, event ):
		event.Skip()

	def persegi_luas( self, event ):
		event.Skip()

	def lingkaran_keliling_luas( self, event ):
		event.Skip()

	def persegi_panjang_luas( self, event ):
		event.Skip()

	def segitiga_keliling_luas( self, event ):
		event.Skip()

	def belah_ketupat_luas( self, event ):
		event.Skip()

	def trapesium_keliling_luas( self, event ):
		event.Skip()

	def layang_keliling_luas( self, event ):
		event.Skip()

	def jajar_genjang_keliling_luas( self, event ):
		event.Skip()

	def kubus_luas( self, event ):
		event.Skip()

	def balok_luas( self, event ):
		event.Skip()

	def prisma_segitiga_luas( self, event ):
		event.Skip()

	def prisma_segiempat_luas( self, event ):
		event.Skip()

	def kerucut_luas( self, event ):
		event.Skip()

	def bola_luas( self, event ):
		event.Skip()

	def limas_segiempat_LuasP( self, event ):
		event.Skip()

	def tabung_luas( self, event ):
		event.Skip()

	def kubus_volume( self, event ):
		event.Skip()

	def balok_volume( self, event ):
		event.Skip()

	def prisma_segitiga_volume( self, event ):
		event.Skip()

	def prisma_segiempat_volume( self, event ):
		event.Skip()

	def kerucut_volume( self, event ):
		event.Skip()

	def bola_volume( self, event ):
		event.Skip()

	def limas_segiempat_volume( self, event ):
		event.Skip()

	def tabung_volume( self, event ):
		event.Skip()

	def tombol_bang_datar( self, event ):
		event.Skip()

	def tombol_bang_ruang( self, event ):
		event.Skip()

	def tombol_bang_datar1( self, event ):
		event.Skip()

	def tombol_bang_ruang1( self, event ):
		event.Skip()

	def tombol_buka_catatan( self, event ):
		event.Skip()


###########################################################################
## Class panel_catatan
###########################################################################

class panel_catatan ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer78 = wx.BoxSizer( wx.VERTICAL )


		bSizer78.Add( ( 0, 25), 0, wx.EXPAND, 5 )

		self.m_staticText351 = wx.StaticText( self, wx.ID_ANY, u"My Catatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText351.Wrap( -1 )

		self.m_staticText351.SetFont( wx.Font( 26, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText351.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer78.Add( self.m_staticText351, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer78.Add( ( 0, 25), 0, wx.EXPAND, 5 )

		fgSizer42 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer42.SetFlexibleDirection( wx.BOTH )
		fgSizer42.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText297 = wx.StaticText( self, wx.ID_ANY, u"Deadline", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText297.Wrap( -1 )

		self.m_staticText297.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText297.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer42.Add( self.m_staticText297, 0, wx.ALL, 5 )


		fgSizer42.Add( ( 25, 0), 1, wx.EXPAND, 5 )

		self.m_staticText301 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301.Wrap( -1 )

		fgSizer42.Add( self.m_staticText301, 0, wx.ALL, 5 )

		self.input_deadline = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,40 ), 0 )
		self.input_deadline.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.input_deadline.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.input_deadline.SetBackgroundColour( wx.Colour( 128, 128, 255 ) )

		fgSizer42.Add( self.input_deadline, 0, wx.ALL, 5 )

		self.catatan = wx.StaticText( self, wx.ID_ANY, u"Catatan PR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.catatan.Wrap( -1 )

		self.catatan.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.catatan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer42.Add( self.catatan, 0, wx.ALL, 5 )


		fgSizer42.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText302 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText302.Wrap( -1 )

		fgSizer42.Add( self.m_staticText302, 0, wx.ALL, 5 )

		self.input_cat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,200 ), 0 )
		self.input_cat.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.input_cat.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.input_cat.SetBackgroundColour( wx.Colour( 172, 172, 255 ) )

		fgSizer42.Add( self.input_cat, 0, wx.ALL, 5 )


		fgSizer42.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer78.Add( fgSizer42, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		fgSizer52 = wx.FlexGridSizer( 0, 8, 0, 0 )
		fgSizer52.SetFlexibleDirection( wx.BOTH )
		fgSizer52.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.tombol_tambah_cat = wx.Button( self, wx.ID_ANY, u"TAMBAH", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_tambah_cat.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_tambah_cat.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.tombol_tambah_cat.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )

		fgSizer52.Add( self.tombol_tambah_cat, 0, wx.ALL, 5 )


		fgSizer52.Add( ( 25, 0), 1, wx.EXPAND, 5 )

		self.tombol_edit_catatan = wx.Button( self, wx.ID_ANY, u"EDIT", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_edit_catatan.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_edit_catatan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.tombol_edit_catatan.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )

		fgSizer52.Add( self.tombol_edit_catatan, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		fgSizer52.Add( ( 25, 0), 1, wx.EXPAND, 5 )

		self.tombol_delete_catatan = wx.Button( self, wx.ID_ANY, u"HAPUS", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_delete_catatan.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_delete_catatan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.tombol_delete_catatan.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )

		fgSizer52.Add( self.tombol_delete_catatan, 0, wx.ALL, 5 )


		fgSizer52.Add( ( 25, 0), 1, wx.EXPAND, 5 )

		self.tombol_refresh_catatan = wx.Button( self, wx.ID_ANY, u"REFRESH", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_refresh_catatan.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_refresh_catatan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		self.tombol_refresh_catatan.SetBackgroundColour( wx.Colour( 255, 128, 255 ) )

		fgSizer52.Add( self.tombol_refresh_catatan, 0, wx.ALL, 5 )


		bSizer78.Add( fgSizer52, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer80 = wx.BoxSizer( wx.VERTICAL )

		self.tabel_catatan = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel_catatan.CreateGrid( 11, 2 )
		self.tabel_catatan.EnableEditing( True )
		self.tabel_catatan.EnableGridLines( True )
		self.tabel_catatan.EnableDragGridSize( False )
		self.tabel_catatan.SetMargins( 0, 0 )

		# Columns
		self.tabel_catatan.SetColSize( 0, 200 )
		self.tabel_catatan.SetColSize( 1, 500 )
		self.tabel_catatan.EnableDragColMove( False )
		self.tabel_catatan.EnableDragColSize( True )
		self.tabel_catatan.SetColLabelSize( 30 )
		self.tabel_catatan.SetColLabelValue( 0, u"Deadline" )
		self.tabel_catatan.SetColLabelValue( 1, u"Catatan PR" )
		self.tabel_catatan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_catatan.EnableDragRowSize( True )
		self.tabel_catatan.SetRowLabelSize( 80 )
		self.tabel_catatan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.tabel_catatan.SetLabelBackgroundColour( wx.Colour( 128, 128, 192 ) )
		self.tabel_catatan.SetLabelFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tabel_catatan.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		# Cell Defaults
		self.tabel_catatan.SetDefaultCellBackgroundColour( wx.Colour( 221, 221, 255 ) )
		self.tabel_catatan.SetDefaultCellFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )
		self.tabel_catatan.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		self.tabel_catatan.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )

		bSizer80.Add( self.tabel_catatan, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer78.Add( bSizer80, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.tombol_catatan_kem = wx.Button( self, wx.ID_ANY, u"KEMBALI", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_catatan_kem.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_catatan_kem.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_catatan_kem.SetBackgroundColour( wx.Colour( 83, 83, 255 ) )

		bSizer78.Add( self.tombol_catatan_kem, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer78 )
		self.Layout()

		# Connect Events
		self.tombol_tambah_cat.Bind( wx.EVT_BUTTON, self.tombol_catatan_tambah )
		self.tombol_edit_catatan.Bind( wx.EVT_BUTTON, self.tombol_catatan_edit )
		self.tombol_delete_catatan.Bind( wx.EVT_BUTTON, self.tombol_catatan_del )
		self.tombol_refresh_catatan.Bind( wx.EVT_BUTTON, self.tombol_catatan_res )
		self.tabel_catatan.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.select_cell_tabel )
		self.tombol_catatan_kem.Bind( wx.EVT_BUTTON, self.tombol_catatan_kembali )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tombol_catatan_tambah( self, event ):
		event.Skip()

	def tombol_catatan_edit( self, event ):
		event.Skip()

	def tombol_catatan_del( self, event ):
		event.Skip()

	def tombol_catatan_res( self, event ):
		event.Skip()

	def select_cell_tabel( self, event ):
		event.Skip()

	def tombol_catatan_kembali( self, event ):
		event.Skip()


###########################################################################
## Class k_persegi
###########################################################################

class k_persegi ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Keliling Persegi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Sisi", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 50), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_sisiPersegi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisiPersegi, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_kPersegi = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_kPersegi.Wrap( -1 )

		self.hasil_kPersegi.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_kPersegi.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_kPersegi, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_persegi_keliling = wx.Button( self, wx.ID_ANY, u"Hitung Keliling", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.tombol_persegi_keliling.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_persegi_keliling.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_persegi_keliling.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.tombol_persegi_keliling, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_persegi_Keliling = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_persegi_Keliling.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_persegi_Keliling.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_persegi_Keliling.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer4.Add( self.tombol_kembali_persegi_Keliling, 0, wx.ALIGN_CENTER, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.tombol_persegi_keliling.Bind( wx.EVT_BUTTON, self.persegi_keliling_hitung )
		self.tombol_kembali_persegi_Keliling.Bind( wx.EVT_BUTTON, self.kembali_kel_persegiOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def persegi_keliling_hitung( self, event ):
		event.Skip()

	def kembali_kel_persegiOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class l_persegi
###########################################################################

class l_persegi ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Luas Persegi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Sisi", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 50), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_sisiPersegi2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisiPersegi2, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_LPersegi = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_LPersegi.Wrap( -1 )

		self.hasil_LPersegi.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_LPersegi.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_LPersegi, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_persegi_luas = wx.Button( self, wx.ID_ANY, u"Hitung Luas", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.tombol_persegi_luas.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_persegi_luas.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_persegi_luas.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.tombol_persegi_luas, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_persegi_luas = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_persegi_luas.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_persegi_luas.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_persegi_luas.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer4.Add( self.tombol_kembali_persegi_luas, 0, wx.ALIGN_CENTER, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.tombol_persegi_luas.Bind( wx.EVT_BUTTON, self.persegi_luas_hitung )
		self.tombol_kembali_persegi_luas.Bind( wx.EVT_BUTTON, self.kembali_luas_persegiOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def persegi_luas_hitung( self, event ):
		event.Skip()

	def kembali_luas_persegiOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class k_PPanjang
###########################################################################

class k_PPanjang ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Keliling Persegi Panjang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Panjang", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 50), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_panjang_kel = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_panjang_kel, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_kel_pp = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_kel_pp.Wrap( -1 )

		self.hasil_kel_pp.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_kel_pp.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_kel_pp, 0, wx.ALL, 5 )

		self.m_staticText166 = wx.StaticText( self, wx.ID_ANY, u"Lebar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText166.Wrap( -1 )

		self.m_staticText166.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText166.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText166, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText167 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )

		self.m_staticText167.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText167, 0, wx.ALL, 5 )

		self.input_lebar_luas = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_lebar_luas, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kel_pp = wx.Button( self, wx.ID_ANY, u"Hitung Keliling", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.tombol_kel_pp.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kel_pp.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kel_pp.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.tombol_kel_pp, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.kembali_kel_pp = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.kembali_kel_pp.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.kembali_kel_pp.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.kembali_kel_pp.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer4.Add( self.kembali_kel_pp, 0, wx.ALIGN_CENTER, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.tombol_kel_pp.Bind( wx.EVT_BUTTON, self.persegi_panjang_keliling_hitung )
		self.kembali_kel_pp.Bind( wx.EVT_BUTTON, self.kembali_kel_ppOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def persegi_panjang_keliling_hitung( self, event ):
		event.Skip()

	def kembali_kel_ppOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class l_PPanjang
###########################################################################

class l_PPanjang ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Luas Persegi Panjang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Panjang", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 50), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_p_luas_pp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_p_luas_pp, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_luas_pp = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_luas_pp.Wrap( -1 )

		self.hasil_luas_pp.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_luas_pp.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_luas_pp, 0, wx.ALL, 5 )

		self.m_staticText166 = wx.StaticText( self, wx.ID_ANY, u"Lebar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText166.Wrap( -1 )

		self.m_staticText166.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText166.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText166, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText167 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )

		self.m_staticText167.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText167, 0, wx.ALL, 5 )

		self.input_l_luas_pp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_l_luas_pp, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.hitung_luas_pp = wx.Button( self, wx.ID_ANY, u"Hitung Luas", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.hitung_luas_pp.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hitung_luas_pp.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.hitung_luas_pp.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.hitung_luas_pp, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.luas_pp_kembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.luas_pp_kembali.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.luas_pp_kembali.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.luas_pp_kembali.SetBackgroundColour( wx.Colour( 255, 128, 192 ) )

		bSizer4.Add( self.luas_pp_kembali, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.hitung_luas_pp.Bind( wx.EVT_BUTTON, self.persegi_panjang_luas_hitung )
		self.luas_pp_kembali.Bind( wx.EVT_BUTTON, self.kem_lPP )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def persegi_panjang_luas_hitung( self, event ):
		event.Skip()

	def kem_lPP( self, event ):
		event.Skip()


###########################################################################
## Class k_lingkaran
###########################################################################

class k_lingkaran ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Keliling Lingkaran", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Diameter", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 50), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_diameter = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_diameter, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_kel_lingkaran = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_kel_lingkaran.Wrap( -1 )

		self.hasil_kel_lingkaran.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_kel_lingkaran.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_kel_lingkaran, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.hitung_kel_lingkaran = wx.Button( self, wx.ID_ANY, u"Hitung Keliling", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.hitung_kel_lingkaran.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hitung_kel_lingkaran.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.hitung_kel_lingkaran.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.hitung_kel_lingkaran, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.kembali_kel_lingkaran = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.kembali_kel_lingkaran.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.kembali_kel_lingkaran.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.kembali_kel_lingkaran.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer4.Add( self.kembali_kel_lingkaran, 0, wx.ALIGN_CENTER, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.hitung_kel_lingkaran.Bind( wx.EVT_BUTTON, self.lingkaran_keliling_hitung )
		self.kembali_kel_lingkaran.Bind( wx.EVT_BUTTON, self.kembali_kel_lingOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def lingkaran_keliling_hitung( self, event ):
		event.Skip()

	def kembali_kel_lingOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class l_lingkaran
###########################################################################

class l_lingkaran ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Luas Lingkaran", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Jari-jari", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 50), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_jariluas = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_jariluas, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_luas_lingkaran = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_luas_lingkaran.Wrap( -1 )

		self.hasil_luas_lingkaran.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_luas_lingkaran.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_luas_lingkaran, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_luas_ling = wx.Button( self, wx.ID_ANY, u"Hitung Luas", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.tombol_luas_ling.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_luas_ling.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_luas_ling.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.tombol_luas_ling, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.kembali_luas_linkaran = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.kembali_luas_linkaran.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.kembali_luas_linkaran.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.kembali_luas_linkaran.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer4.Add( self.kembali_luas_linkaran, 0, wx.ALIGN_CENTER, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.tombol_luas_ling.Bind( wx.EVT_BUTTON, self.lingkaran_luas_hitung )
		self.kembali_luas_linkaran.Bind( wx.EVT_BUTTON, self.kembali_luas_lingOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def lingkaran_luas_hitung( self, event ):
		event.Skip()

	def kembali_luas_lingOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class k_segitiga
###########################################################################

class k_segitiga ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Keliling Segitiga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Sisi A", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_sisi_a = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_a, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_kel_seg = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_kel_seg.Wrap( -1 )

		self.hasil_kel_seg.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_kel_seg.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_kel_seg, 0, wx.ALL, 5 )

		self.m_staticText166 = wx.StaticText( self, wx.ID_ANY, u"Sisi B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText166.Wrap( -1 )

		self.m_staticText166.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText166.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText166, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText167 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )

		self.m_staticText167.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText167.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText167, 0, wx.ALL, 5 )

		self.input_sisi_b = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_b, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText129 = wx.StaticText( self, wx.ID_ANY, u"Sisi C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText129.Wrap( -1 )

		self.m_staticText129.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText129.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText129, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 50), 1, wx.EXPAND, 5 )

		self.m_staticText130 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText130.Wrap( -1 )

		self.m_staticText130.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText130.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText130, 0, wx.ALL, 5 )

		self.input_sisi_c = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_c, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 50), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kel_seg = wx.Button( self, wx.ID_ANY, u"Hitung Keliling", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.tombol_kel_seg.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kel_seg.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kel_seg.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.tombol_kel_seg, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.kembali_kel_seg = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.kembali_kel_seg.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.kembali_kel_seg.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.kembali_kel_seg.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer4.Add( self.kembali_kel_seg, 0, wx.ALIGN_CENTER, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.tombol_kel_seg.Bind( wx.EVT_BUTTON, self.segitiga_keliling_hitung )
		self.kembali_kel_seg.Bind( wx.EVT_BUTTON, self.kembali_kel_segOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def segitiga_keliling_hitung( self, event ):
		event.Skip()

	def kembali_kel_segOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class l_segitiga
###########################################################################

class l_segitiga ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Luas Segitiga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Alas", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 50), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_al = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_al, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_luas_segitiga = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_luas_segitiga.Wrap( -1 )

		self.hasil_luas_segitiga.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_luas_segitiga.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_luas_segitiga, 0, wx.ALL, 5 )

		self.m_staticText166 = wx.StaticText( self, wx.ID_ANY, u"Tinggi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText166.Wrap( -1 )

		self.m_staticText166.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText166.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText166, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText167 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )

		self.m_staticText167.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText167, 0, wx.ALL, 5 )

		self.input_t = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_t, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.hitung_luas_sa = wx.Button( self, wx.ID_ANY, u"Hitung Luas", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.hitung_luas_sa.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hitung_luas_sa.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.hitung_luas_sa.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.hitung_luas_sa, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.luas_segitiga_kembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.luas_segitiga_kembali.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.luas_segitiga_kembali.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.luas_segitiga_kembali.SetBackgroundColour( wx.Colour( 255, 128, 192 ) )

		bSizer4.Add( self.luas_segitiga_kembali, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.hitung_luas_sa.Bind( wx.EVT_BUTTON, self.segitiga_luas_hitung )
		self.luas_segitiga_kembali.Bind( wx.EVT_BUTTON, self.kem_segitiga_luas )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def segitiga_luas_hitung( self, event ):
		event.Skip()

	def kem_segitiga_luas( self, event ):
		event.Skip()


###########################################################################
## Class k_belah_ketupat
###########################################################################

class k_belah_ketupat ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Keliling Belah Ketupat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Sisi A", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 10), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_sisi_a2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_a2, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_kel_bel = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_kel_bel.Wrap( -1 )

		self.hasil_kel_bel.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_kel_bel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_kel_bel, 0, wx.ALL, 5 )

		self.m_staticText166 = wx.StaticText( self, wx.ID_ANY, u"Sisi B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText166.Wrap( -1 )

		self.m_staticText166.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText166.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText166, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText167 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )

		self.m_staticText167.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText167.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText167, 0, wx.ALL, 5 )

		self.input_sisi_b2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_b2, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText129 = wx.StaticText( self, wx.ID_ANY, u"Sisi C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText129.Wrap( -1 )

		self.m_staticText129.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText129.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText129, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.m_staticText130 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText130.Wrap( -1 )

		self.m_staticText130.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText130.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText130, 0, wx.ALL, 5 )

		self.input_sisi_c2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_c2, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText178 = wx.StaticText( self, wx.ID_ANY, u"Sisi D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText178.Wrap( -1 )

		self.m_staticText178.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText178.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText178, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.m_staticText179 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText179.Wrap( -1 )

		self.m_staticText179.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText179.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		fgSizer2.Add( self.m_staticText179, 0, wx.ALL, 5 )

		self.input_sisi_d2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_d2, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kel_bel = wx.Button( self, wx.ID_ANY, u"Hitung Keliling", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.tombol_kel_bel.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kel_bel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kel_bel.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.tombol_kel_bel, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.kembali_kel_bb = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.kembali_kel_bb.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.kembali_kel_bb.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.kembali_kel_bb.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer4.Add( self.kembali_kel_bb, 0, wx.ALIGN_CENTER, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.tombol_kel_bel.Bind( wx.EVT_BUTTON, self.bb_keliling_hitung )
		self.kembali_kel_bb.Bind( wx.EVT_BUTTON, self.kembali_kel_bbOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def bb_keliling_hitung( self, event ):
		event.Skip()

	def kembali_kel_bbOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class l_belah_ketupat
###########################################################################

class l_belah_ketupat ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Luas Belah Ketupat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Diagonal 1", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 50), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_diagonal_bb = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_diagonal_bb, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_luas_bb = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_luas_bb.Wrap( -1 )

		self.hasil_luas_bb.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_luas_bb.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_luas_bb, 0, wx.ALL, 5 )

		self.m_staticText166 = wx.StaticText( self, wx.ID_ANY, u"Diagonal 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText166.Wrap( -1 )

		self.m_staticText166.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText166.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText166, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText167 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )

		self.m_staticText167.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText167, 0, wx.ALL, 5 )

		self.input_diagonal_bb2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_diagonal_bb2, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.hitung_luas_bb = wx.Button( self, wx.ID_ANY, u"Hitung Luas", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.hitung_luas_bb.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hitung_luas_bb.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.hitung_luas_bb.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.hitung_luas_bb, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.luas_bb_kembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.luas_bb_kembali.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.luas_bb_kembali.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.luas_bb_kembali.SetBackgroundColour( wx.Colour( 255, 128, 192 ) )

		bSizer4.Add( self.luas_bb_kembali, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.hitung_luas_bb.Bind( wx.EVT_BUTTON, self.bb_luas_hitung )
		self.luas_bb_kembali.Bind( wx.EVT_BUTTON, self.kem_bb )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def bb_luas_hitung( self, event ):
		event.Skip()

	def kem_bb( self, event ):
		event.Skip()


###########################################################################
## Class k_trapesium
###########################################################################

class k_trapesium ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Keliling Trapesium", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Sisi AB", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 10), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_sisi_ab = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_ab, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_kel_trape = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_kel_trape.Wrap( -1 )

		self.hasil_kel_trape.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_kel_trape.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_kel_trape, 0, wx.ALL, 5 )

		self.m_staticText166 = wx.StaticText( self, wx.ID_ANY, u"Sisi BC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText166.Wrap( -1 )

		self.m_staticText166.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText166.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText166, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText167 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )

		self.m_staticText167.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText167.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText167, 0, wx.ALL, 5 )

		self.input_sisi_bc = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_bc, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText129 = wx.StaticText( self, wx.ID_ANY, u"Sisi CD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText129.Wrap( -1 )

		self.m_staticText129.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText129.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText129, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.m_staticText130 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText130.Wrap( -1 )

		self.m_staticText130.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText130.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText130, 0, wx.ALL, 5 )

		self.input_sisi_cd = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_cd, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText178 = wx.StaticText( self, wx.ID_ANY, u"Sisi AD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText178.Wrap( -1 )

		self.m_staticText178.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText178.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText178, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.m_staticText179 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText179.Wrap( -1 )

		self.m_staticText179.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText179.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		fgSizer2.Add( self.m_staticText179, 0, wx.ALL, 5 )

		self.input_sisi_ad = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_ad, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kel_trapesi = wx.Button( self, wx.ID_ANY, u"Hitung Keliling", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.tombol_kel_trapesi.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kel_trapesi.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kel_trapesi.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.tombol_kel_trapesi, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.kembali_kel_trape = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.kembali_kel_trape.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.kembali_kel_trape.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.kembali_kel_trape.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer4.Add( self.kembali_kel_trape, 0, wx.ALIGN_CENTER, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.tombol_kel_trapesi.Bind( wx.EVT_BUTTON, self.trape_keliling_hitung )
		self.kembali_kel_trape.Bind( wx.EVT_BUTTON, self.kembali_kel_trapeOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def trape_keliling_hitung( self, event ):
		event.Skip()

	def kembali_kel_trapeOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class l_trapesium
###########################################################################

class l_trapesium ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Luas Trapesium", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Sisi A", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 10), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_sisi_a_trape = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_a_trape, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_luas_trape = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_luas_trape.Wrap( -1 )

		self.hasil_luas_trape.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_luas_trape.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_luas_trape, 0, wx.ALL, 5 )

		self.m_staticText166 = wx.StaticText( self, wx.ID_ANY, u"Sisi B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText166.Wrap( -1 )

		self.m_staticText166.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText166.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText166, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText167 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )

		self.m_staticText167.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText167.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText167, 0, wx.ALL, 5 )

		self.input_sisi_b_trape = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_b_trape, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText129 = wx.StaticText( self, wx.ID_ANY, u"Tinggi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText129.Wrap( -1 )

		self.m_staticText129.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText129.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText129, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.m_staticText130 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText130.Wrap( -1 )

		self.m_staticText130.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText130.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText130, 0, wx.ALL, 5 )

		self.input_tinggi_trape = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_tinggi_trape, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_luas_trapesi = wx.Button( self, wx.ID_ANY, u"Hitung Keliling", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.tombol_luas_trapesi.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_luas_trapesi.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_luas_trapesi.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.tombol_luas_trapesi, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.kembali_luas_trape = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.kembali_luas_trape.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.kembali_luas_trape.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.kembali_luas_trape.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer4.Add( self.kembali_luas_trape, 0, wx.ALIGN_CENTER, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.tombol_luas_trapesi.Bind( wx.EVT_BUTTON, self.trape_keliling_hitung )
		self.kembali_luas_trape.Bind( wx.EVT_BUTTON, self.kembali_luas_trapeOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def trape_keliling_hitung( self, event ):
		event.Skip()

	def kembali_luas_trapeOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class k_layang
###########################################################################

class k_layang ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 162, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Keliling Layang-Layang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Sisi AB", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 10), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_sisi_ab2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_ab2, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_kel_layang = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_kel_layang.Wrap( -1 )

		self.hasil_kel_layang.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_kel_layang.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_kel_layang, 0, wx.ALL, 5 )

		self.m_staticText166 = wx.StaticText( self, wx.ID_ANY, u"Sisi BC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText166.Wrap( -1 )

		self.m_staticText166.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText166.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText166, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText167 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )

		self.m_staticText167.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText167.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText167, 0, wx.ALL, 5 )

		self.input_sisi_bc2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_bc2, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText129 = wx.StaticText( self, wx.ID_ANY, u"Sisi CD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText129.Wrap( -1 )

		self.m_staticText129.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText129.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText129, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.m_staticText130 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText130.Wrap( -1 )

		self.m_staticText130.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText130.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText130, 0, wx.ALL, 5 )

		self.input_sisi_cd2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_cd2, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText178 = wx.StaticText( self, wx.ID_ANY, u"Sisi AD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText178.Wrap( -1 )

		self.m_staticText178.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText178.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText178, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 10), 1, wx.EXPAND, 5 )

		self.m_staticText179 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText179.Wrap( -1 )

		self.m_staticText179.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText179.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		fgSizer2.Add( self.m_staticText179, 0, wx.ALL, 5 )

		self.input_sisi_ad2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_ad2, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kel_Layang = wx.Button( self, wx.ID_ANY, u"Hitung Keliling", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.tombol_kel_Layang.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kel_Layang.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kel_Layang.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.tombol_kel_Layang, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.kembali_kel_layang = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.kembali_kel_layang.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.kembali_kel_layang.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.kembali_kel_layang.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer4.Add( self.kembali_kel_layang, 0, wx.ALIGN_CENTER, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.tombol_kel_Layang.Bind( wx.EVT_BUTTON, self.layang_keliling_hitung )
		self.kembali_kel_layang.Bind( wx.EVT_BUTTON, self.kembali_kel_layangOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def layang_keliling_hitung( self, event ):
		event.Skip()

	def kembali_kel_layangOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class l_layang
###########################################################################

class l_layang ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Luas Layang-Layang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Diagonal 1", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 50), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_digA_luas_layang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_digA_luas_layang, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_luas_layang = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_luas_layang.Wrap( -1 )

		self.hasil_luas_layang.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_luas_layang.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_luas_layang, 0, wx.ALL, 5 )

		self.m_staticText166 = wx.StaticText( self, wx.ID_ANY, u"Diagonal 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText166.Wrap( -1 )

		self.m_staticText166.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText166.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText166, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText167 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )

		self.m_staticText167.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText167, 0, wx.ALL, 5 )

		self.input_digb_luas_layang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_digb_luas_layang, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.hitung_luas_layang = wx.Button( self, wx.ID_ANY, u"Hitung Luas", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.hitung_luas_layang.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hitung_luas_layang.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.hitung_luas_layang.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.hitung_luas_layang, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.kem_layang_luas = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.kem_layang_luas.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.kem_layang_luas.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.kem_layang_luas.SetBackgroundColour( wx.Colour( 255, 128, 192 ) )

		bSizer4.Add( self.kem_layang_luas, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.hitung_luas_layang.Bind( wx.EVT_BUTTON, self.layang_luas_hitung )
		self.kem_layang_luas.Bind( wx.EVT_BUTTON, self.layang_luas_tom )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def layang_luas_hitung( self, event ):
		event.Skip()

	def layang_luas_tom( self, event ):
		event.Skip()


###########################################################################
## Class k_jajar
###########################################################################

class k_jajar ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Keliling Jajar Genjang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Sisi Alas", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 10), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_sisi_alasGJ = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_alasGJ, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_kel_Gj = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_kel_Gj.Wrap( -1 )

		self.hasil_kel_Gj.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_kel_Gj.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_kel_Gj, 0, wx.ALL, 5 )

		self.m_staticText166 = wx.StaticText( self, wx.ID_ANY, u"Sisi Miring", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText166.Wrap( -1 )

		self.m_staticText166.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText166.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText166, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText167 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )

		self.m_staticText167.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText167.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText167, 0, wx.ALL, 5 )

		self.input_sisi_miringGJ = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_sisi_miringGJ, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kel_GJ = wx.Button( self, wx.ID_ANY, u"Hitung Keliling", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.tombol_kel_GJ.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kel_GJ.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kel_GJ.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.tombol_kel_GJ, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.kembali_kel_gj = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.kembali_kel_gj.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.kembali_kel_gj.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.kembali_kel_gj.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer4.Add( self.kembali_kel_gj, 0, wx.ALIGN_CENTER, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.tombol_kel_GJ.Bind( wx.EVT_BUTTON, self.gj_keliling_hitung )
		self.kembali_kel_gj.Bind( wx.EVT_BUTTON, self.kembali_kel_gjOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def gj_keliling_hitung( self, event ):
		event.Skip()

	def kembali_kel_gjOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class l_jajar
###########################################################################

class l_jajar ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Luas Jajar Genjang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4.Add( self.m_staticText51, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Alas", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 50), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_p_jg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_p_jg, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_luas_jg = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_luas_jg.Wrap( -1 )

		self.hasil_luas_jg.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_luas_jg.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.hasil_luas_jg, 0, wx.ALL, 5 )

		self.m_staticText166 = wx.StaticText( self, wx.ID_ANY, u"Tinggi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText166.Wrap( -1 )

		self.m_staticText166.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText166.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText166, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText167 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )

		self.m_staticText167.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer2.Add( self.m_staticText167, 0, wx.ALL, 5 )

		self.input_t_jg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		fgSizer2.Add( self.input_t_jg, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.hitung_luas_jg = wx.Button( self, wx.ID_ANY, u"Hitung Luas", wx.DefaultPosition, wx.Size( 160,35 ), 0 )
		self.hitung_luas_jg.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hitung_luas_jg.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.hitung_luas_jg.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2.Add( self.hitung_luas_jg, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.luas_segitiga_kembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.luas_segitiga_kembali.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.luas_segitiga_kembali.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.luas_segitiga_kembali.SetBackgroundColour( wx.Colour( 255, 128, 192 ) )

		bSizer4.Add( self.luas_segitiga_kembali, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.hitung_luas_jg.Bind( wx.EVT_BUTTON, self.jg_luas_hitung )
		self.luas_segitiga_kembali.Bind( wx.EVT_BUTTON, self.kem_jg_luas )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def jg_luas_hitung( self, event ):
		event.Skip()

	def kem_jg_luas( self, event ):
		event.Skip()


###########################################################################
## Class LP_kubus
###########################################################################

class LP_kubus ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Luas Permukaan Kubus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Rusuk", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 50), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_rusuk = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_rusuk, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_luasPermukaanKubus = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_luasPermukaanKubus.Wrap( -1 )

		self.hasil_luasPermukaanKubus.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_luasPermukaanKubus.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_luasPermukaanKubus, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kubus_lpermukaan = wx.Button( self, wx.ID_ANY, u"Hitung \nLuas Permukaan", wx.DefaultPosition, wx.Size( 170,70 ), 0 )
		self.tombol_kubus_lpermukaan.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kubus_lpermukaan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kubus_lpermukaan.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_kubus_lpermukaan, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_kubus_luasPer = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_kubus_luasPer.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_kubus_luasPer.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_kubus_luasPer.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_kubus_luasPer, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_kubus_lpermukaan.Bind( wx.EVT_BUTTON, self.kubus_lPermukaan_hitung )
		self.tombol_kembali_kubus_luasPer.Bind( wx.EVT_BUTTON, self.kembali_luasPer_kubusOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def kubus_lPermukaan_hitung( self, event ):
		event.Skip()

	def kembali_luasPer_kubusOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class V_kubus
###########################################################################

class V_kubus ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Volume Kubus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"rusuk_volume", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 50), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_rusuk_volume = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_rusuk_volume, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_volumeKubus = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_volumeKubus.Wrap( -1 )

		self.hasil_volumeKubus.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_volumeKubus.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_volumeKubus, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kubus_volume = wx.Button( self, wx.ID_ANY, u"Hitung Volume", wx.DefaultPosition, wx.Size( 170,35 ), 0 )
		self.tombol_kubus_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kubus_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kubus_volume.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_kubus_volume, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_kubus_volume = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_kubus_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_kubus_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_kubus_volume.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_kubus_volume, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_kubus_volume.Bind( wx.EVT_BUTTON, self.kubus_volume_hitung )
		self.tombol_kembali_kubus_volume.Bind( wx.EVT_BUTTON, self.kembali_volume_kubusOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def kubus_volume_hitung( self, event ):
		event.Skip()

	def kembali_volume_kubusOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class LP_balok
###########################################################################

class LP_balok ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Luas Permukaan Balok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Panjang", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_panjang_balok = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_panjang_balok, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_luasPermukaanBalok = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_luasPermukaanBalok.Wrap( -1 )

		self.hasil_luasPermukaanBalok.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_luasPermukaanBalok.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_luasPermukaanBalok, 0, wx.ALL, 5 )

		self.m_staticText400 = wx.StaticText( self, wx.ID_ANY, u"Lebar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText400.Wrap( -1 )

		self.m_staticText400.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText400.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText400, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText402 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText402.Wrap( -1 )

		self.m_staticText402.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText402.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText402, 0, wx.ALL, 5 )

		self.input_lebar_balok = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_lebar_balok, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText403 = wx.StaticText( self, wx.ID_ANY, u"Tinggi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText403.Wrap( -1 )

		self.m_staticText403.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText403.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText403, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText404 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText404.Wrap( -1 )

		self.m_staticText404.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText404.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText404, 0, wx.ALL, 5 )

		self.input_tinggi_balok = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_tinggi_balok, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_balok_lpermukaan = wx.Button( self, wx.ID_ANY, u"Hitung \nLuas Permukaan", wx.DefaultPosition, wx.Size( 170,70 ), 0 )
		self.tombol_balok_lpermukaan.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_balok_lpermukaan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_balok_lpermukaan.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_balok_lpermukaan, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_balok_luasPer = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_balok_luasPer.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_balok_luasPer.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_balok_luasPer.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_balok_luasPer, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_balok_lpermukaan.Bind( wx.EVT_BUTTON, self.balok_lPermukaan_hitung )
		self.tombol_kembali_balok_luasPer.Bind( wx.EVT_BUTTON, self.kembali_luasPer_balokOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def balok_lPermukaan_hitung( self, event ):
		event.Skip()

	def kembali_luasPer_balokOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class V_balok
###########################################################################

class V_balok ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Volume Balok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Panjang", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_panjang_balok1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_panjang_balok1, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_volumeBalok = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_volumeBalok.Wrap( -1 )

		self.hasil_volumeBalok.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_volumeBalok.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_volumeBalok, 0, wx.ALL, 5 )

		self.m_staticText400 = wx.StaticText( self, wx.ID_ANY, u"Lebar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText400.Wrap( -1 )

		self.m_staticText400.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText400.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText400, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText402 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText402.Wrap( -1 )

		self.m_staticText402.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText402.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText402, 0, wx.ALL, 5 )

		self.input_lebar_balok1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_lebar_balok1, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText403 = wx.StaticText( self, wx.ID_ANY, u"Tinggi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText403.Wrap( -1 )

		self.m_staticText403.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText403.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText403, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText404 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText404.Wrap( -1 )

		self.m_staticText404.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText404.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText404, 0, wx.ALL, 5 )

		self.input_tinggi_balok1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_tinggi_balok1, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_balok_volume = wx.Button( self, wx.ID_ANY, u"Hitung Volume", wx.DefaultPosition, wx.Size( 170,35 ), 0 )
		self.tombol_balok_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_balok_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_balok_volume.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_balok_volume, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_balok_volume = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_balok_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_balok_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_balok_volume.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_balok_volume, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_balok_volume.Bind( wx.EVT_BUTTON, self.balok_volume_hitung )
		self.tombol_kembali_balok_volume.Bind( wx.EVT_BUTTON, self.kembali_volume_balokOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def balok_volume_hitung( self, event ):
		event.Skip()

	def kembali_volume_balokOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class LP_PSeg
###########################################################################

class LP_PSeg ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Luas Permukaan Prisma Segitiga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Alas (Sisi AB)", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_alas_prisma = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_alas_prisma, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_luasPermukaanPSegitiga = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_luasPermukaanPSegitiga.Wrap( -1 )

		self.hasil_luasPermukaanPSegitiga.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_luasPermukaanPSegitiga.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_luasPermukaanPSegitiga, 0, wx.ALL, 5 )

		self.m_staticText400 = wx.StaticText( self, wx.ID_ANY, u"Tinggi Alas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText400.Wrap( -1 )

		self.m_staticText400.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText400.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText400, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText402 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText402.Wrap( -1 )

		self.m_staticText402.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText402.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText402, 0, wx.ALL, 5 )

		self.input_tinggi_alas = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_tinggi_alas, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText403 = wx.StaticText( self, wx.ID_ANY, u"Tinggi Prisma", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText403.Wrap( -1 )

		self.m_staticText403.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText403.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText403, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText404 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText404.Wrap( -1 )

		self.m_staticText404.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText404.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText404, 0, wx.ALL, 5 )

		self.input_tinggi_prisma = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_tinggi_prisma, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText508 = wx.StaticText( self, wx.ID_ANY, u"Sisi BC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText508.Wrap( -1 )

		self.m_staticText508.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText508.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText508, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText509 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText509.Wrap( -1 )

		self.m_staticText509.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText509.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText509, 0, wx.ALL, 5 )

		self.input_sisiBC = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_sisiBC, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText5112 = wx.StaticText( self, wx.ID_ANY, u"Sisi AC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5112.Wrap( -1 )

		self.m_staticText5112.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText5112.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText5112, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText512 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText512.Wrap( -1 )

		self.m_staticText512.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText512.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText512, 0, wx.ALL, 5 )

		self.input_sisiAC = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_sisiAC, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_pSegitiga_lpermukaan = wx.Button( self, wx.ID_ANY, u"Hitung \nLuas Permukaan", wx.DefaultPosition, wx.Size( 170,70 ), 0 )
		self.tombol_pSegitiga_lpermukaan.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_pSegitiga_lpermukaan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_pSegitiga_lpermukaan.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_pSegitiga_lpermukaan, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_prismaSegitiga_luasPer = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_prismaSegitiga_luasPer.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_prismaSegitiga_luasPer.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_prismaSegitiga_luasPer.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_prismaSegitiga_luasPer, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_pSegitiga_lpermukaan.Bind( wx.EVT_BUTTON, self.pSegitiga_lPermukaan_hitung )
		self.tombol_kembali_prismaSegitiga_luasPer.Bind( wx.EVT_BUTTON, self.kembali_luasPer_balokOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def pSegitiga_lPermukaan_hitung( self, event ):
		event.Skip()

	def kembali_luasPer_balokOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class V_PSeg
###########################################################################

class V_PSeg ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Volume Prisma Segitiga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Alas", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_alas_pSegitiga = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_alas_pSegitiga, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_volumePSegitiga = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_volumePSegitiga.Wrap( -1 )

		self.hasil_volumePSegitiga.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_volumePSegitiga.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_volumePSegitiga, 0, wx.ALL, 5 )

		self.m_staticText400 = wx.StaticText( self, wx.ID_ANY, u"Tinggi Alas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText400.Wrap( -1 )

		self.m_staticText400.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText400.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText400, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText402 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText402.Wrap( -1 )

		self.m_staticText402.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText402.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText402, 0, wx.ALL, 5 )

		self.input_tinggi_alas_pSegitiga = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_tinggi_alas_pSegitiga, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText403 = wx.StaticText( self, wx.ID_ANY, u"Tinggi Prisma", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText403.Wrap( -1 )

		self.m_staticText403.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText403.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText403, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText404 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText404.Wrap( -1 )

		self.m_staticText404.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText404.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText404, 0, wx.ALL, 5 )

		self.input_tinggi_pSegitiga = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_tinggi_pSegitiga, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_pSegitiga_volume = wx.Button( self, wx.ID_ANY, u"Hitung Volume", wx.DefaultPosition, wx.Size( 170,35 ), 0 )
		self.tombol_pSegitiga_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_pSegitiga_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_pSegitiga_volume.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_pSegitiga_volume, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_pSegitiga_volume = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_pSegitiga_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_pSegitiga_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_pSegitiga_volume.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_pSegitiga_volume, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_pSegitiga_volume.Bind( wx.EVT_BUTTON, self.pSegitiga_volume_hitung )
		self.tombol_kembali_pSegitiga_volume.Bind( wx.EVT_BUTTON, self.kembali_volume_pSegitigaOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def pSegitiga_volume_hitung( self, event ):
		event.Skip()

	def kembali_volume_pSegitigaOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class LP_PEmpat
###########################################################################

class LP_PEmpat ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Luas Permukaan Prisma Segiempat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Panjang", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_panjang_pS = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_panjang_pS, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_LPSegiempat = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_LPSegiempat.Wrap( -1 )

		self.hasil_LPSegiempat.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_LPSegiempat.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_LPSegiempat, 0, wx.ALL, 5 )

		self.m_staticText400 = wx.StaticText( self, wx.ID_ANY, u"Lebar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText400.Wrap( -1 )

		self.m_staticText400.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText400.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText400, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText402 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText402.Wrap( -1 )

		self.m_staticText402.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText402.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText402, 0, wx.ALL, 5 )

		self.input_lebar_pS = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_lebar_pS, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText403 = wx.StaticText( self, wx.ID_ANY, u"Tinggi Prisma", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText403.Wrap( -1 )

		self.m_staticText403.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText403.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText403, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText404 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText404.Wrap( -1 )

		self.m_staticText404.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText404.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText404, 0, wx.ALL, 5 )

		self.input_tinggi_pS = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_tinggi_pS, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_pSegiempat_lpermukaan = wx.Button( self, wx.ID_ANY, u"Hitung \nLuas Permukaan", wx.DefaultPosition, wx.Size( 170,70 ), 0 )
		self.tombol_pSegiempat_lpermukaan.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_pSegiempat_lpermukaan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_pSegiempat_lpermukaan.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_pSegiempat_lpermukaan, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_pSegiempat_luasPer = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_pSegiempat_luasPer.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_pSegiempat_luasPer.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_pSegiempat_luasPer.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_pSegiempat_luasPer, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_pSegiempat_lpermukaan.Bind( wx.EVT_BUTTON, self.pSegiempat_lpermukaan )
		self.tombol_kembali_pSegiempat_luasPer.Bind( wx.EVT_BUTTON, self.kembali_luasPer_pSegiempatOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def pSegiempat_lpermukaan( self, event ):
		event.Skip()

	def kembali_luasPer_pSegiempatOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class V_PEmpat
###########################################################################

class V_PEmpat ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Volume Prisma Segiempat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Panjang", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_panjang4_pSegiempat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_panjang4_pSegiempat, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_volumepSegiempat = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_volumepSegiempat.Wrap( -1 )

		self.hasil_volumepSegiempat.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_volumepSegiempat.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_volumepSegiempat, 0, wx.ALL, 5 )

		self.m_staticText400 = wx.StaticText( self, wx.ID_ANY, u"Lebar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText400.Wrap( -1 )

		self.m_staticText400.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText400.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText400, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText402 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText402.Wrap( -1 )

		self.m_staticText402.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText402.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText402, 0, wx.ALL, 5 )

		self.input_lebar4_pSegiempat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_lebar4_pSegiempat, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText403 = wx.StaticText( self, wx.ID_ANY, u"Tinggi Prisma", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText403.Wrap( -1 )

		self.m_staticText403.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText403.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText403, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText404 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText404.Wrap( -1 )

		self.m_staticText404.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText404.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText404, 0, wx.ALL, 5 )

		self.input_tinggi4_pSegiempat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_tinggi4_pSegiempat, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_pSegiempat_volume = wx.Button( self, wx.ID_ANY, u"Hitung Volume", wx.DefaultPosition, wx.Size( 170,35 ), 0 )
		self.tombol_pSegiempat_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_pSegiempat_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_pSegiempat_volume.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_pSegiempat_volume, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_pSegiempat_volume = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_pSegiempat_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_pSegiempat_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_pSegiempat_volume.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_pSegiempat_volume, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_pSegiempat_volume.Bind( wx.EVT_BUTTON, self.pSegiempat_volume_hitung )
		self.tombol_kembali_pSegiempat_volume.Bind( wx.EVT_BUTTON, self.kembali_volume_pSegiempatOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def pSegiempat_volume_hitung( self, event ):
		event.Skip()

	def kembali_volume_pSegiempatOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class LP_Kerucut
###########################################################################

class LP_Kerucut ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Luas Permukaan Kerucut", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Jari-Jari", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_jari_kerucut = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_jari_kerucut, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_luasPermukaanKerucut = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_luasPermukaanKerucut.Wrap( -1 )

		self.hasil_luasPermukaanKerucut.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_luasPermukaanKerucut.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_luasPermukaanKerucut, 0, wx.ALL, 5 )

		self.m_staticText400 = wx.StaticText( self, wx.ID_ANY, u"Garis Pelukis (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText400.Wrap( -1 )

		self.m_staticText400.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText400.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText400, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText402 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText402.Wrap( -1 )

		self.m_staticText402.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText402.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText402, 0, wx.ALL, 5 )

		self.input_s_kerucut = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_s_kerucut, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kerucut_lpermukaan = wx.Button( self, wx.ID_ANY, u"Hitung \nLuas Permukaan", wx.DefaultPosition, wx.Size( 170,70 ), 0 )
		self.tombol_kerucut_lpermukaan.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kerucut_lpermukaan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kerucut_lpermukaan.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_kerucut_lpermukaan, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_kerucut_luasPer = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_kerucut_luasPer.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_kerucut_luasPer.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_kerucut_luasPer.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_kerucut_luasPer, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_kerucut_lpermukaan.Bind( wx.EVT_BUTTON, self.lpermukaan_kerucut_hitung )
		self.tombol_kembali_kerucut_luasPer.Bind( wx.EVT_BUTTON, self.kembali_luasPer_KerucutOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def lpermukaan_kerucut_hitung( self, event ):
		event.Skip()

	def kembali_luasPer_KerucutOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class V_Kerucut
###########################################################################

class V_Kerucut ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Volume Kerucut", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Jari-Jari", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_jari_kerucut = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_jari_kerucut, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_volumeKerucut = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_volumeKerucut.Wrap( -1 )

		self.hasil_volumeKerucut.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_volumeKerucut.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_volumeKerucut, 0, wx.ALL, 5 )

		self.m_staticText403 = wx.StaticText( self, wx.ID_ANY, u"Tinggi Kerucut", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText403.Wrap( -1 )

		self.m_staticText403.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText403.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText403, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText404 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText404.Wrap( -1 )

		self.m_staticText404.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText404.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText404, 0, wx.ALL, 5 )

		self.input_tinggi_kerucut = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_tinggi_kerucut, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kerucut_volume = wx.Button( self, wx.ID_ANY, u"Hitung Volume", wx.DefaultPosition, wx.Size( 170,35 ), 0 )
		self.tombol_kerucut_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kerucut_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kerucut_volume.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_kerucut_volume, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_kerucut_volume = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_kerucut_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_kerucut_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_kerucut_volume.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_kerucut_volume, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_kerucut_volume.Bind( wx.EVT_BUTTON, self.kerucut_volume_hitung )
		self.tombol_kembali_kerucut_volume.Bind( wx.EVT_BUTTON, self.kembali_volume_kerucutOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def kerucut_volume_hitung( self, event ):
		event.Skip()

	def kembali_volume_kerucutOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class LP_Bola
###########################################################################

class LP_Bola ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Luas Permukaan Bola", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Jari-Jari", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_jari_bola = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_jari_bola, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_luasPermukaanBola = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_luasPermukaanBola.Wrap( -1 )

		self.hasil_luasPermukaanBola.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_luasPermukaanBola.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_luasPermukaanBola, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_bola_lpermukaan = wx.Button( self, wx.ID_ANY, u"Hitung \nLuas Permukaan", wx.DefaultPosition, wx.Size( 170,70 ), 0 )
		self.tombol_bola_lpermukaan.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_bola_lpermukaan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_bola_lpermukaan.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_bola_lpermukaan, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_kerucut_luasPer = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_kerucut_luasPer.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_kerucut_luasPer.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_kerucut_luasPer.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_kerucut_luasPer, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_bola_lpermukaan.Bind( wx.EVT_BUTTON, self.lpermukaan_bola_hitung )
		self.tombol_kembali_kerucut_luasPer.Bind( wx.EVT_BUTTON, self.kembali_luasPer_BolaOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def lpermukaan_bola_hitung( self, event ):
		event.Skip()

	def kembali_luasPer_BolaOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class V_Bola
###########################################################################

class V_Bola ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Volume Bola", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Jari-Jari", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_jari_bola_2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_jari_bola_2, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_volumeBola = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_volumeBola.Wrap( -1 )

		self.hasil_volumeBola.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_volumeBola.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_volumeBola, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_bola_volume = wx.Button( self, wx.ID_ANY, u"Hitung Volume", wx.DefaultPosition, wx.Size( 170,35 ), 0 )
		self.tombol_bola_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_bola_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_bola_volume.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_bola_volume, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_bola_volume = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_bola_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_bola_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_bola_volume.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_bola_volume, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_bola_volume.Bind( wx.EVT_BUTTON, self.bola_volume_hitung )
		self.tombol_kembali_bola_volume.Bind( wx.EVT_BUTTON, self.kembali_volume_BolaOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def bola_volume_hitung( self, event ):
		event.Skip()

	def kembali_volume_BolaOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class LP_LEmpat
###########################################################################

class LP_LEmpat ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Luas Permukaan Limas Segiempat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Alas Segitiga", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_alas_lSegiempat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_alas_lSegiempat, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_LPSegiempat = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_LPSegiempat.Wrap( -1 )

		self.hasil_LPSegiempat.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_LPSegiempat.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_LPSegiempat, 0, wx.ALL, 5 )

		self.m_staticText400 = wx.StaticText( self, wx.ID_ANY, u"Tinggi Segitiga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText400.Wrap( -1 )

		self.m_staticText400.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText400.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText400, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText402 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText402.Wrap( -1 )

		self.m_staticText402.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText402.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText402, 0, wx.ALL, 5 )

		self.input_tinggi_lSegiempat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_tinggi_lSegiempat, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText403 = wx.StaticText( self, wx.ID_ANY, u"Sisi Segiempat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText403.Wrap( -1 )

		self.m_staticText403.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText403.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText403, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText404 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText404.Wrap( -1 )

		self.m_staticText404.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText404.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText404, 0, wx.ALL, 5 )

		self.input_sisi_lSegiempat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_sisi_lSegiempat, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_lSegiempat_lpermukaan = wx.Button( self, wx.ID_ANY, u"Hitung \nLuas Permukaan", wx.DefaultPosition, wx.Size( 170,70 ), 0 )
		self.tombol_lSegiempat_lpermukaan.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_lSegiempat_lpermukaan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_lSegiempat_lpermukaan.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_lSegiempat_lpermukaan, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_LSegiempat_luasPer = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_LSegiempat_luasPer.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_LSegiempat_luasPer.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_LSegiempat_luasPer.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_LSegiempat_luasPer, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_lSegiempat_lpermukaan.Bind( wx.EVT_BUTTON, self.lpermukaan_LSegiempat_hitung )
		self.tombol_kembali_LSegiempat_luasPer.Bind( wx.EVT_BUTTON, self.kembali_luasPer_LSegiempatOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def lpermukaan_LSegiempat_hitung( self, event ):
		event.Skip()

	def kembali_luasPer_LSegiempatOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class V_LEmpat
###########################################################################

class V_LEmpat ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Volume Limas Segiempat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Sisi Segiempat", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_sisi_LSegiempat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_sisi_LSegiempat, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_volumeLsegiempat = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_volumeLsegiempat.Wrap( -1 )

		self.hasil_volumeLsegiempat.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_volumeLsegiempat.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_volumeLsegiempat, 0, wx.ALL, 5 )

		self.m_staticText400 = wx.StaticText( self, wx.ID_ANY, u"Tinggi Limas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText400.Wrap( -1 )

		self.m_staticText400.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText400.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText400, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText402 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText402.Wrap( -1 )

		self.m_staticText402.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText402.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText402, 0, wx.ALL, 5 )

		self.input_tinggi_limas_lSegiempat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_tinggi_limas_lSegiempat, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_lSegiempat_volume = wx.Button( self, wx.ID_ANY, u"Hitung Volume", wx.DefaultPosition, wx.Size( 170,35 ), 0 )
		self.tombol_lSegiempat_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_lSegiempat_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_lSegiempat_volume.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_lSegiempat_volume, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_LSegiempat_volume = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_LSegiempat_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_LSegiempat_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_LSegiempat_volume.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_LSegiempat_volume, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_lSegiempat_volume.Bind( wx.EVT_BUTTON, self.lSegiempat_volume_hitung )
		self.tombol_kembali_LSegiempat_volume.Bind( wx.EVT_BUTTON, self.kembali_volume_LSegiempatOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def lSegiempat_volume_hitung( self, event ):
		event.Skip()

	def kembali_volume_LSegiempatOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class LP_Tabung
###########################################################################

class LP_Tabung ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Luas Permukaan Tabung", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Jari-Jari", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_jari_tabung = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_jari_tabung, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_luasPermukaanTabung = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_luasPermukaanTabung.Wrap( -1 )

		self.hasil_luasPermukaanTabung.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_luasPermukaanTabung.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_luasPermukaanTabung, 0, wx.ALL, 5 )

		self.m_staticText400 = wx.StaticText( self, wx.ID_ANY, u"Tinggi Tabung", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText400.Wrap( -1 )

		self.m_staticText400.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText400.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText400, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText402 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText402.Wrap( -1 )

		self.m_staticText402.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText402.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText402, 0, wx.ALL, 5 )

		self.input_tinggi_tabung = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_tinggi_tabung, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_tabung_lpermukaan = wx.Button( self, wx.ID_ANY, u"Hitung \nLuas Permukaan", wx.DefaultPosition, wx.Size( 170,70 ), 0 )
		self.tombol_tabung_lpermukaan.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_tabung_lpermukaan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_tabung_lpermukaan.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_tabung_lpermukaan, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_Tabung_luasPer = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_Tabung_luasPer.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_Tabung_luasPer.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_Tabung_luasPer.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_Tabung_luasPer, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_tabung_lpermukaan.Bind( wx.EVT_BUTTON, self.lpermukaan_tabung_hitung )
		self.tombol_kembali_Tabung_luasPer.Bind( wx.EVT_BUTTON, self.kembali_luasPer_TabungOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def lpermukaan_tabung_hitung( self, event ):
		event.Skip()

	def kembali_luasPer_TabungOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class V_Tabung
###########################################################################

class V_Tabung ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Volume Tabung", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer41.Add( self.m_staticText511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		fgSizer22 = wx.FlexGridSizer( 0, 9, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Jari-Jari", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_jari_tabung2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_jari_tabung2, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Hasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText33, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.hasil_volumeTabung = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.hasil_volumeTabung.Wrap( -1 )

		self.hasil_volumeTabung.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.hasil_volumeTabung.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.hasil_volumeTabung, 0, wx.ALL, 5 )

		self.m_staticText400 = wx.StaticText( self, wx.ID_ANY, u"Tinggi Tabung", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText400.Wrap( -1 )

		self.m_staticText400.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText400.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText400, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText402 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText402.Wrap( -1 )

		self.m_staticText402.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.m_staticText402.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer22.Add( self.m_staticText402, 0, wx.ALL, 5 )

		self.input_tinggi_tabung2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		fgSizer22.Add( self.input_tinggi_tabung2, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_tabung_volume = wx.Button( self, wx.ID_ANY, u"Hitung Volume", wx.DefaultPosition, wx.Size( 170,35 ), 0 )
		self.tombol_tabung_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_tabung_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_tabung_volume.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer22.Add( self.tombol_tabung_volume, 0, wx.ALL, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer52.Add( fgSizer22, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_kembali_Tabung_volume = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_kembali_Tabung_volume.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_kembali_Tabung_volume.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_kembali_Tabung_volume.SetBackgroundColour( wx.Colour( 253, 123, 221 ) )

		bSizer41.Add( self.tombol_kembali_Tabung_volume, 0, wx.ALIGN_CENTER, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		# Connect Events
		self.tombol_tabung_volume.Bind( wx.EVT_BUTTON, self.volume_tabung_hitung )
		self.tombol_kembali_Tabung_volume.Bind( wx.EVT_BUTTON, self.kembali_volume_TabungOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def volume_tabung_hitung( self, event ):
		event.Skip()

	def kembali_volume_TabungOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class panel_ru_bd
###########################################################################

class panel_ru_bd ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer80 = wx.BoxSizer( wx.VERTICAL )


		bSizer80.Add( ( 0, 25), 0, wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Rumus Bangun Datar", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 26, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer80.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.grid_datar = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_datar.CreateGrid( 8, 3 )
		self.grid_datar.EnableEditing( True )
		self.grid_datar.EnableGridLines( True )
		self.grid_datar.EnableDragGridSize( False )
		self.grid_datar.SetMargins( 0, 0 )

		# Columns
		self.grid_datar.SetColSize( 0, 200 )
		self.grid_datar.SetColSize( 1, 200 )
		self.grid_datar.SetColSize( 2, 200 )
		self.grid_datar.EnableDragColMove( False )
		self.grid_datar.EnableDragColSize( True )
		self.grid_datar.SetColLabelSize( 30 )
		self.grid_datar.SetColLabelValue( 0, u"Nama Bangun Datar" )
		self.grid_datar.SetColLabelValue( 1, u"Rumus Keliling" )
		self.grid_datar.SetColLabelValue( 2, u"Rumus Luas" )
		self.grid_datar.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_datar.SetRowSize( 0, 35 )
		self.grid_datar.SetRowSize( 1, 35 )
		self.grid_datar.SetRowSize( 2, 35 )
		self.grid_datar.SetRowSize( 3, 35 )
		self.grid_datar.SetRowSize( 4, 35 )
		self.grid_datar.SetRowSize( 5, 35 )
		self.grid_datar.SetRowSize( 6, 35 )
		self.grid_datar.SetRowSize( 7, 35 )
		self.grid_datar.EnableDragRowSize( True )
		self.grid_datar.SetRowLabelSize( 80 )
		self.grid_datar.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_datar.SetLabelBackgroundColour( wx.Colour( 128, 128, 192 ) )
		self.grid_datar.SetLabelFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.grid_datar.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_datar.SetDefaultCellBackgroundColour( wx.Colour( 221, 221, 255 ) )
		self.grid_datar.SetDefaultCellFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )
		self.grid_datar.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer80.Add( self.grid_datar, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_rum_ba_tar = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_rum_ba_tar.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_rum_ba_tar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_rum_ba_tar.SetBackgroundColour( wx.Colour( 255, 128, 192 ) )

		bSizer80.Add( self.tombol_rum_ba_tar, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer80 )
		self.Layout()

		# Connect Events
		self.tombol_rum_ba_tar.Bind( wx.EVT_BUTTON, self.klik_kembali_datar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def klik_kembali_datar( self, event ):
		event.Skip()


###########################################################################
## Class panel_ru_ruang
###########################################################################

class panel_ru_ruang ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer80 = wx.BoxSizer( wx.VERTICAL )


		bSizer80.Add( ( 0, 25), 0, wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Rumus Bangun Ruang", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 26, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer80.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.grid_ruang = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_ruang.CreateGrid( 8, 3 )
		self.grid_ruang.EnableEditing( True )
		self.grid_ruang.EnableGridLines( True )
		self.grid_ruang.EnableDragGridSize( False )
		self.grid_ruang.SetMargins( 0, 0 )

		# Columns
		self.grid_ruang.SetColSize( 0, 200 )
		self.grid_ruang.SetColSize( 1, 280 )
		self.grid_ruang.SetColSize( 2, 200 )
		self.grid_ruang.EnableDragColMove( False )
		self.grid_ruang.EnableDragColSize( True )
		self.grid_ruang.SetColLabelSize( 30 )
		self.grid_ruang.SetColLabelValue( 0, u"Nama Bangun Ruang" )
		self.grid_ruang.SetColLabelValue( 1, u"Rumus Luas Permukaan" )
		self.grid_ruang.SetColLabelValue( 2, u"Rumus Volume" )
		self.grid_ruang.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_ruang.SetRowSize( 0, 35 )
		self.grid_ruang.SetRowSize( 1, 35 )
		self.grid_ruang.SetRowSize( 2, 35 )
		self.grid_ruang.SetRowSize( 3, 35 )
		self.grid_ruang.SetRowSize( 4, 35 )
		self.grid_ruang.SetRowSize( 5, 35 )
		self.grid_ruang.SetRowSize( 6, 35 )
		self.grid_ruang.SetRowSize( 7, 35 )
		self.grid_ruang.EnableDragRowSize( True )
		self.grid_ruang.SetRowLabelSize( 80 )
		self.grid_ruang.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_ruang.SetLabelBackgroundColour( wx.Colour( 128, 128, 192 ) )
		self.grid_ruang.SetLabelFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.grid_ruang.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_ruang.SetDefaultCellBackgroundColour( wx.Colour( 221, 221, 255 ) )
		self.grid_ruang.SetDefaultCellFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )
		self.grid_ruang.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer80.Add( self.grid_ruang, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_rum_ba_ang = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_rum_ba_ang.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_rum_ba_ang.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_rum_ba_ang.SetBackgroundColour( wx.Colour( 255, 128, 192 ) )

		bSizer80.Add( self.tombol_rum_ba_ang, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer80 )
		self.Layout()

		# Connect Events
		self.tombol_rum_ba_ang.Bind( wx.EVT_BUTTON, self.klik_kembali_ruang )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def klik_kembali_ruang( self, event ):
		event.Skip()


###########################################################################
## Class panel_spe_bd
###########################################################################

class panel_spe_bd ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer80 = wx.BoxSizer( wx.VERTICAL )


		bSizer80.Add( ( 0, 25), 0, wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Spesifikasi Bangun Datar", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 26, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer80.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.grid_spe_datar = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_spe_datar.CreateGrid( 8, 5 )
		self.grid_spe_datar.EnableEditing( True )
		self.grid_spe_datar.EnableGridLines( True )
		self.grid_spe_datar.EnableDragGridSize( False )
		self.grid_spe_datar.SetMargins( 0, 0 )

		# Columns
		self.grid_spe_datar.SetColSize( 0, 200 )
		self.grid_spe_datar.SetColSize( 1, 100 )
		self.grid_spe_datar.SetColSize( 2, 100 )
		self.grid_spe_datar.SetColSize( 3, 200 )
		self.grid_spe_datar.SetColSize( 4, 100 )
		self.grid_spe_datar.EnableDragColMove( False )
		self.grid_spe_datar.EnableDragColSize( True )
		self.grid_spe_datar.SetColLabelSize( 30 )
		self.grid_spe_datar.SetColLabelValue( 0, u"Nama Bangun Datar" )
		self.grid_spe_datar.SetColLabelValue( 1, u"Sisi" )
		self.grid_spe_datar.SetColLabelValue( 2, u"Sudut" )
		self.grid_spe_datar.SetColLabelValue( 3, u"Simetri Putar" )
		self.grid_spe_datar.SetColLabelValue( 4, u"Diagonal" )
		self.grid_spe_datar.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_spe_datar.SetRowSize( 0, 35 )
		self.grid_spe_datar.SetRowSize( 1, 35 )
		self.grid_spe_datar.SetRowSize( 2, 35 )
		self.grid_spe_datar.SetRowSize( 3, 35 )
		self.grid_spe_datar.SetRowSize( 4, 35 )
		self.grid_spe_datar.SetRowSize( 5, 35 )
		self.grid_spe_datar.SetRowSize( 6, 35 )
		self.grid_spe_datar.SetRowSize( 7, 35 )
		self.grid_spe_datar.EnableDragRowSize( True )
		self.grid_spe_datar.SetRowLabelSize( 80 )
		self.grid_spe_datar.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_spe_datar.SetLabelBackgroundColour( wx.Colour( 128, 128, 192 ) )
		self.grid_spe_datar.SetLabelFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.grid_spe_datar.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_spe_datar.SetDefaultCellBackgroundColour( wx.Colour( 221, 221, 255 ) )
		self.grid_spe_datar.SetDefaultCellFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )
		self.grid_spe_datar.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer80.Add( self.grid_spe_datar, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_spe_ba_tar = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_spe_ba_tar.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_spe_ba_tar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_spe_ba_tar.SetBackgroundColour( wx.Colour( 255, 128, 192 ) )

		bSizer80.Add( self.tombol_spe_ba_tar, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer80 )
		self.Layout()

		# Connect Events
		self.tombol_spe_ba_tar.Bind( wx.EVT_BUTTON, self.klik_kembali_datar_spek )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def klik_kembali_datar_spek( self, event ):
		event.Skip()


###########################################################################
## Class panel_spe_bruang
###########################################################################

class panel_spe_bruang ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1300,800 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 72, 164, 255 ) )

		bSizer80 = wx.BoxSizer( wx.VERTICAL )


		bSizer80.Add( ( 0, 25), 0, wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Spesifikasi Bangun Ruang", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 26, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Bauhaus 93" ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer80.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.grid_spe_ruang = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_spe_ruang.CreateGrid( 8, 7 )
		self.grid_spe_ruang.EnableEditing( True )
		self.grid_spe_ruang.EnableGridLines( True )
		self.grid_spe_ruang.EnableDragGridSize( False )
		self.grid_spe_ruang.SetMargins( 0, 0 )

		# Columns
		self.grid_spe_ruang.SetColSize( 0, 200 )
		self.grid_spe_ruang.SetColSize( 1, 100 )
		self.grid_spe_ruang.SetColSize( 2, 100 )
		self.grid_spe_ruang.SetColSize( 3, 100 )
		self.grid_spe_ruang.SetColSize( 4, 200 )
		self.grid_spe_ruang.SetColSize( 5, 200 )
		self.grid_spe_ruang.SetColSize( 6, 200 )
		self.grid_spe_ruang.EnableDragColMove( False )
		self.grid_spe_ruang.EnableDragColSize( True )
		self.grid_spe_ruang.SetColLabelSize( 30 )
		self.grid_spe_ruang.SetColLabelValue( 0, u"Nama Bangun Datar" )
		self.grid_spe_ruang.SetColLabelValue( 1, u"Sisi" )
		self.grid_spe_ruang.SetColLabelValue( 2, u"Rusuk" )
		self.grid_spe_ruang.SetColLabelValue( 3, u"Sudut" )
		self.grid_spe_ruang.SetColLabelValue( 4, u"Diagonal Sisi" )
		self.grid_spe_ruang.SetColLabelValue( 5, u"Diagonal Ruang" )
		self.grid_spe_ruang.SetColLabelValue( 6, u"Bidang Diagonal" )
		self.grid_spe_ruang.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_spe_ruang.SetRowSize( 0, 35 )
		self.grid_spe_ruang.SetRowSize( 1, 35 )
		self.grid_spe_ruang.SetRowSize( 2, 35 )
		self.grid_spe_ruang.SetRowSize( 3, 35 )
		self.grid_spe_ruang.SetRowSize( 4, 35 )
		self.grid_spe_ruang.SetRowSize( 5, 35 )
		self.grid_spe_ruang.SetRowSize( 6, 35 )
		self.grid_spe_ruang.SetRowSize( 7, 35 )
		self.grid_spe_ruang.EnableDragRowSize( True )
		self.grid_spe_ruang.SetRowLabelSize( 80 )
		self.grid_spe_ruang.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_spe_ruang.SetLabelBackgroundColour( wx.Colour( 128, 128, 192 ) )
		self.grid_spe_ruang.SetLabelFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.grid_spe_ruang.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_spe_ruang.SetDefaultCellBackgroundColour( wx.Colour( 221, 221, 255 ) )
		self.grid_spe_ruang.SetDefaultCellFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )
		self.grid_spe_ruang.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer80.Add( self.grid_spe_ruang, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tombol_spe_ba_ruang = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.tombol_spe_ba_ruang.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.tombol_spe_ba_ruang.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.tombol_spe_ba_ruang.SetBackgroundColour( wx.Colour( 255, 128, 192 ) )

		bSizer80.Add( self.tombol_spe_ba_ruang, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer80.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer80 )
		self.Layout()

		# Connect Events
		self.tombol_spe_ba_ruang.Bind( wx.EVT_BUTTON, self.klik_kembali_ruang_spek )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def klik_kembali_ruang_spek( self, event ):
		event.Skip()


