#!/usr/bin/python
################################################################################
# Vrutha Sahayi - An application that helps one to find/check the "vrutham"
# (metrics) of a given Malayalam poem.
#
# Authors:	Sanjeev Kozhisseri <sanjvkoz@yahoo.com>
#			Sushen V Kumar <sushku@yahoo.com>
#
# Vrutha Sahayi is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# Vrutha Sahayi is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Vrutha Sahayi; if not, write to the
#				 Free Software Foundation, Inc.,
#				 51 Franklin St, Fifth Floor,
#				 Boston, MA  02110-1301 USA
################################################################################
import wx, data
from wx.grid import Grid
from wx.html import HtmlHelpController
from wx.lib.wordwrap import wordwrap
from interface import *

class myPanel(wx.Panel):
	def __init__(self, parent, id):
		wx.Panel.__init__(self, parent, id)

		# Top Sizer
		topSizer = wx.BoxSizer(wx.VERTICAL)

		# Input Label
		labelSizer = wx.BoxSizer(wx.HORIZONTAL)
		self.inputLabel = wx.StaticText(self, -1, data.enterPadyamLabel, wx.Point(40, 20), wx.Size(720,20))
		self.increaseFontSize(self.inputLabel, 1.5)
		labelSizer.Add(self.inputLabel, 1, wx.EXPAND | wx.ALL, 5)
		topSizer.Add(labelSizer, 0, wx.ALIGN_LEFT)

		# Input Multiline TextCtrl 
		self.input = wx.TextCtrl(self,5, '',wx.Point(40,50), wx.Size(720,140),wx.TE_MULTILINE|wx.TE_DONTWRAP)
		self.increaseFontSize(self.input, 1.5)
		topSizer.Add(self.input, 1, wx.EXPAND | wx.ALL, 5)

		# Output Label
		labelSizer1 = wx.BoxSizer(wx.HORIZONTAL)
		self.outputLabel = wx.StaticText(self, -1, data.seeResultsHereLabel, wx.Point(40, 20), wx.Size(720,20))
		self.increaseFontSize(self.outputLabel, 1.5)
		labelSizer1.Add(self.outputLabel, 1, wx.EXPAND | wx.ALL, 5)
		topSizer.Add(labelSizer1, 0, wx.ALIGN_LEFT)

		# Output Multiline Grid
		self.output = Grid(self,6, wx.Point(40,210), wx.Size(790,140),wx.TE_MULTILINE|wx.TE_READONLY)
		self.output.SetDefaultRowSize(25)
		self.output.SetDefaultColSize(50)
		self.output.SetRowLabelSize(0)
		self.output.SetColLabelSize(0)
		self.output.CreateGrid(10,30)
		self.output.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.evtOnCellSelected)
		topSizer.Add(self.output, 1, wx.EXPAND | wx.ALL, 5)

		# Control Sizer
		controlSizer = wx.BoxSizer(wx.HORIZONTAL)

		# Radio Box
		self.radioList = [	data.findVruthamLabel,
							data.checkVruthamLabel] 
		self.rb = wx.RadioBox(self, 50, data.whatToDoLabel, wx.Point(40, 375), wx.Size(250,90),
							self.radioList, 3, wx.RA_SPECIFY_ROWS)
		self.increaseFontSize(self.rb, 1.5)
		controlSizer.Add(self.rb, 0, wx.ALL, 10)
		wx.EVT_RADIOBOX(self, 50, self.evtRadioBox)

		# Combobox
		self.vruthamList = data.vruthamNameList()
		self.vruthamCombo = wx.ComboBox(self, 30, data.selectVruthamLabel, wx.Point(420,390), wx.Size(250, -1),
										self.vruthamList, wx.CB_DROPDOWN|wx.CB_READONLY)
		self.increaseFontSize(self.vruthamCombo, 1.5)
		controlSizer.Add(self.vruthamCombo, 0, wx.ALIGN_CENTER)
		wx.EVT_COMBOBOX(self, 30, self.evtComboBox)
		self.vruthamCombo.Enable(0)

		# Status TextCtrl
		self.status = wx.TextCtrl(self,5, '',wx.DefaultPosition, wx.Size(250,80),wx.TE_MULTILINE|wx.TE_READONLY)
		self.increaseFontSize(self.status, 1.5)
		self.status.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))
		controlSizer.Add(self.status, 0, wx.EXPAND | wx.ALL, 15)

		topSizer.Add(controlSizer, 0, wx.ALIGN_CENTER)

		# Button Sizer
		buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

		# Buttons
		self.goButton = wx.Button(self, 10, data.findLabel, wx.Point(379, 470), wx.Size(117,35))
		self.increaseFontSize(self.goButton, 1.5)
		self.increaseFontWeight(self.goButton)
		wx.EVT_BUTTON(self, 10, self.goClick)
		buttonSizer.Add(self.goButton, 0, wx.ALL, 10)

		self.clearButton = wx.Button(self, 11, data.clearLabel, wx.Point(506, 470), wx.Size(117,35))
		self.increaseFontSize(self.clearButton, 1.5)
		self.increaseFontWeight(self.clearButton)
		wx.EVT_BUTTON(self, 11, self.clearClick)
		buttonSizer.Add(self.clearButton, 0, wx.ALL, 10)

		self.closeButton = wx.Button(self, 12, data.closeLabel, wx.Point(633, 470), wx.Size(117,35))
		self.increaseFontSize(self.closeButton, 1.5)
		self.increaseFontWeight(self.closeButton)
		wx.EVT_BUTTON(self, 12, self.closeClick)
		buttonSizer.Add(self.closeButton, 0, wx.ALL, 10)

		topSizer.Add(buttonSizer, 0, wx.ALIGN_CENTER)
		self.SetSizer(topSizer)
		topSizer.SetSizeHints(self)

		# Initialize Variables
		self.inVruthamName = ''
		self.checkVruthamFlg = 0
		self.checkFlgSet = 0
		self.dictErrors = {}

	def displayStatus(self, row, col):
		self.status.Clear()
		if self.output.GetNumberRows() <= 0:
			return
		if self.output.GetNumberCols() <= 0:
			return
		if self.output.GetCellValue(row, col) == '':
			return
		if self.checkFlgSet == 1:
			if self.dictErrors.has_key((row,col)):
				self.status.AppendText(self.dictErrors[(row,col)])
			elif self.output.GetCellValue(row, col) == data.rightLabel:
				self.status.AppendText(data.thisLineIsCorrectLabel)
			elif self.output.GetCellValue(row, col) == data.wrongLabel:
				self.status.AppendText(data.thisLineIsWrongLabel)
			else:
				if row == 0:
					self.status.AppendText(data.syllableCountLabel + ' ' + self.output.GetCellValue(row, col))
				else:
					self.status.AppendText(data.thisIsCorrectLabel)
		else:
			if row == 0:
				self.status.AppendText(self.output.GetCellValue(row, col))
			else:
				if col == 0:
					self.status.AppendText(data.slokamLabel + ' ' + self.output.GetCellValue(row, col))
				elif col == 1:
					self.status.AppendText(data.lineLabel + ' ' + self.output.GetCellValue(row, col))
				elif col == 2:
					if self.output.GetCellValue(row, col) != data.iDontKnowLabel:
						if self.dictErrors.has_key((row,col)):
							self.status.AppendText(data.lineVruthamGanangalLabel + ' ' +
										self.output.GetCellValue(row, col) + ', ' + data.yathiBhangamLabel)
						else:
							self.status.AppendText(data.lineVruthamGanangalLabel + ' ' + self.output.GetCellValue(row, col))
					else:
						self.status.AppendText(data.dontKnowVruthamLabel)
				else:
					if self.output.GetCellValue(row, col) != data.iDontKnowLabel:
						if self.dictErrors.has_key((row,col)):
							self.status.AppendText(data.slokamsVruthamLabel + ' ' +
									self.output.GetCellValue(row, col) + ', ' + data.yathiBhangamLabel)
						else:
							self.status.AppendText(data.slokamsVruthamLabel + ' ' + self.output.GetCellValue(row, col))
					else:
						self.status.AppendText(data.dontKnowVruthamLabel)

	def evtOnCellSelected(self, event):
		eventObject = event.GetEventObject()
		row = event.GetRow()
		col = event.GetCol()
		self.displayStatus(row, col)
		event.Skip()

	def evtRadioBox(self, event):
		if (event.GetInt() == 1):
			self.vruthamCombo.Enable(1)
			self.goButton.SetLabel(data.checkLabel)
			self.checkVruthamFlg = 1
		else:
			self.vruthamCombo.Enable(0)
			self.goButton.SetLabel(data.findLabel)
			self.checkVruthamFlg = 0

	def giveCell(self, row = 0, col = 0):
		if self.output.GetNumberCols() < col + 1:
			self.output.AppendCols(col + 1 - self.output.GetNumberCols())
		if self.output.GetNumberRows() < row + 1:
			self.output.AppendRows(row + 1 - self.output.GetNumberRows())

	def increaseFontSize(self, text, size):
		Font = text.GetFont()
		Font.SetPointSize(Font.GetPointSize() * size)
		text.SetFont(Font)

	def increaseFontWeight(self, text):
		Font = text.GetFont()
		Font.SetWeight(wx.FONTWEIGHT_BOLD)
		text.SetFont(Font)

	def increaseCellFontSize(self, row, col):
		Font = self.output.GetDefaultCellFont()
		Font.SetPointSize(Font.GetPointSize() * 1.5)
		self.output.SetCellFont(row, col, Font)

	def increaseCellFontWeight(self, row, col):
		Font = self.output.GetCellFont(row, col)
		Font.SetWeight(wx.FONTWEIGHT_BOLD)
		self.output.SetCellFont(row, col, Font)

	def evtComboBox(self, event):
		self.inVruthamName = event.GetString()

	def splitIntoLines(self, errLocs):
		errLocLines = []
		lineList = []
		for i in errLocs:
			if i[0] == (-1,-1):
				lineList.append(i)
				errLocLines.append(lineList)
				lineList = []
			else:
				lineList.append(i)
		errLocLines.append([((-1,-1), 'y')])
		return errLocLines

	def highLightErrors(self):
		# Print Syllable numbers and Lakshanam
		lakshanamStr = data.getVruthamLakshanam(self.inVruthamName)
		incrRow = 0
		incrCol = 1
		self.ardhaVishamaVrutham = 'n'
		lakshanamLines = lakshanamStr.split('|')
		if lakshanamLines[0] == 'ANUSHTUP':
			lakshanamLines = '        '
			anushtupVrutham = 'y'
			for i in lakshanamLines:
				self.giveCell(incrRow, incrCol)
				self.output.SetCellValue(0, incrCol, str(incrCol))
				self.increaseCellFontWeight(0, incrCol)
				self.output.SetCellAlignment(0, incrCol, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
				self.output.SetCellBackgroundColour(0, incrCol, wx.TheColourDatabase.Find('LIGHT BLUE'))
				incrCol = incrCol + 1
			# Display Ganam Grouping
			incrRow += 1
			incrCol = 1
			self.giveCell(incrRow, incrCol)
			ganamColour1 = wx.Colour(166, 166, 166)
			ganamColour2 = wx.Colour(200, 200, 200)
			self.output.SetCellBackgroundColour(incrRow, incrCol, ganamColour1)
			self.output.SetCellBackgroundColour(incrRow, incrCol + 1, ganamColour2)
			self.output.SetCellBackgroundColour(incrRow, incrCol + 2, ganamColour2)
			self.output.SetCellBackgroundColour(incrRow, incrCol + 3, ganamColour2)
			self.output.SetCellBackgroundColour(incrRow, incrCol + 4, ganamColour1)
			self.output.SetCellBackgroundColour(incrRow, incrCol + 5, ganamColour1)
			self.output.SetCellBackgroundColour(incrRow, incrCol + 6, ganamColour1)
			self.output.SetCellBackgroundColour(incrRow, incrCol + 7, ganamColour2)
		else:
			if lakshanamLines[0] == 'AV':
				self.ardhaVishamaVrutham = 'y'
				lakshanamLines = lakshanamLines[1:len(lakshanamLines)]
			for lakshanam in lakshanamLines:
				incrRow = incrRow + 1
				ganamCount = 1
				ganamStr = ''
				ganam = ''
				ganamColour1 = wx.Colour(166, 166, 166)
				ganamColour2 = wx.Colour(200, 200, 200)
				curGanamColour = ganamColour1
				for i in lakshanam:
					self.giveCell(incrRow, incrCol)
					self.output.SetCellValue(0, incrCol, str(incrCol))
					self.increaseCellFontWeight(0, incrCol)
					self.output.SetCellAlignment(0, incrCol, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
					self.output.SetCellBackgroundColour(0, incrCol, wx.TheColourDatabase.Find('LIGHT BLUE'))
					self.output.SetCellValue(incrRow, incrCol, i)
					self.increaseCellFontWeight(incrRow, incrCol)
					self.output.SetCellAlignment(incrRow, incrCol, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
					self.output.SetCellBackgroundColour(incrRow, incrCol, wx.TheColourDatabase.Find('LIGHT BLUE'))
					# Display Ganam Grouping
					ganamStr += i
					if incrCol % 3 == 0:
						if data.ganamDict.has_key(ganamStr):
							ganam = data.ganamDict[ganamStr]
							self.dictErrors[(incrRow, incrCol - 2)] = ganam + ' ' + data.ganamLabel
							self.dictErrors[(incrRow, incrCol - 1)] = ganam + ' ' + data.ganamLabel
							self.dictErrors[(incrRow, incrCol)] = ganam + ' ' + data.ganamLabel
							ganamStr = ''
							self.output.SetCellBackgroundColour(incrRow, incrCol - 2, curGanamColour)
							self.output.SetCellBackgroundColour(incrRow, incrCol - 1, curGanamColour)
							self.output.SetCellBackgroundColour(incrRow, incrCol, curGanamColour)
							if curGanamColour == ganamColour1:
								curGanamColour = ganamColour2
							else:
								curGanamColour = ganamColour1
						ganamCount += 1
					elif ganamCount > len(lakshanam) / 3:
						if ganamStr == '-':
							self.dictErrors[(incrRow, incrCol)] = data.guruLabel
						else:
							self.dictErrors[(incrRow, incrCol)] = data.laghuLabel
						ganamStr = ''
						self.output.SetCellBackgroundColour(incrRow, incrCol, curGanamColour)
						if curGanamColour == ganamColour1:
							curGanamColour = ganamColour2
						else:
							curGanamColour = ganamColour1
						ganamCount += 1
					incrCol = incrCol + 1
				incrCol = 1
		gridRow = incrRow + 1
		gridCol = 1

		# Print Padyam
		lineNum = 0
		lakshanam = ''
		bgColour = wx.Colour(255, 212, 160)
		errLocLines = self.splitIntoLines(self.errLocs)
		for oneErrLocLine in errLocLines:
			if oneErrLocLine == [((-1,-1),'y')]:
				if self.ardhaVishamaVrutham == 'y':
					if lineNum != 0:
						for i in range(0,4 - lineNum):
							gridCol = 1
							self.giveCell(gridRow, gridCol)
							self.output.SetCellValue(gridRow, 0, data.wrongLabel)
							self.increaseCellFontSize(gridRow, 0)
							self.increaseCellFontWeight(gridRow, 0)
							self.output.SetCellBackgroundColour(gridRow, 0, wx.RED)
							lakshanam = lakshanamLines[lineNum + i]
							while gridCol <= len(lakshanam):
								self.output.SetCellBackgroundColour(gridRow, gridCol, wx.RED)
								self.dictErrors[(gridRow, gridCol)] = data.emptySylLabel
								gridCol = gridCol + 1
							gridRow = gridRow + 1
				lineNum = 0
				gridCol = 1
				if self.output.GetCellValue(gridRow - 1, 0) != '':
					gridRow = gridRow + 1
					self.giveCell(gridRow, gridCol)
				continue
			if self.ardhaVishamaVrutham == 'y':
				lakshanam = lakshanamLines[lineNum % 4]
			else:
				lakshanam = lakshanamStr
			if lineNum == 4:
				lineNum = 1
				gridRow = gridRow + 1
				self.giveCell(gridRow, gridCol)
			else:
				lineNum = lineNum + 1
			if lineNum == 1:
				if bgColour.Green() == 212:
					bgColour = wx.Colour(255, 255, 160)
				else:
					bgColour = wx.Colour(255, 212, 160)
			yathiInPrevChar = 0
			for i in oneErrLocLine:
				if i[0] == (-1, -1):
					yathiInPrevChar = 0
					while gridCol > 1 and gridCol <= len(lakshanam):
						self.output.SetCellValue(gridRow, 0, data.wrongLabel)
						self.increaseCellFontSize(gridRow, 0)
						self.increaseCellFontWeight(gridRow, 0)
						self.output.SetCellBackgroundColour(gridRow, 0, wx.RED)
						self.output.SetCellBackgroundColour(gridRow, gridCol, wx.RED)
						self.dictErrors[(gridRow, gridCol)] = data.emptySylLabel
						gridCol = gridCol + 1
					if gridCol == 1:
						self.giveCell(gridRow, gridCol)
						self.output.SetCellValue(gridRow, 0, '')
						self.output.SetCellBackgroundColour(gridRow, 0, wx.WHITE)
					gridRow = gridRow + 1
					gridCol = 1
					continue
				if gridCol == 1:
					self.giveCell(gridRow, gridCol)
					self.output.SetCellValue(gridRow, 0, data.rightLabel)
					self.increaseCellFontSize(gridRow, 0)
					self.increaseCellFontWeight(gridRow, 0)
					self.output.SetCellBackgroundColour(gridRow, 0, wx.GREEN)
				self.giveCell(gridRow, gridCol)
				if i[1] == 'n':
					yathiInPrevChar = 0
					self.output.SetCellValue(gridRow, gridCol, self.input.GetValue()[i[0][0]:i[0][1] + 1])
					self.output.SetCellBackgroundColour(gridRow, gridCol, wx.RED)
					if gridCol - 1 < len(lakshanam):
						if lakshanam[gridCol - 1] == '-' :
							self.dictErrors[(gridRow, gridCol)] = data.wronglyPlacedLaghuLabel
						else:
							self.dictErrors[(gridRow, gridCol)] = data.wronglyPlacedGuruLabel
					else:
						self.dictErrors[(gridRow, gridCol)] = data.extraSylLabel
					self.output.SetCellValue(gridRow, 0, data.wrongLabel)
					self.increaseCellFontSize(gridRow, 0)
					self.increaseCellFontWeight(gridRow, 0)
					self.output.SetCellBackgroundColour(gridRow, 0, wx.RED)
				elif i[1] == 'g':
					self.output.SetCellValue(gridRow, gridCol, self.input.GetValue()[i[0][0]:i[0][1] + 1])
					self.output.SetCellBackgroundColour(gridRow, gridCol, wx.RED)
					self.dictErrors[(gridRow, gridCol)] = data.wrongGanamLabel
					self.output.SetCellValue(gridRow, 0, data.wrongLabel)
					self.increaseCellFontSize(gridRow, 0)
					self.increaseCellFontWeight(gridRow, 0)
					self.output.SetCellBackgroundColour(gridRow, 0, wx.RED)
				else:
					self.output.SetCellValue(gridRow, gridCol, self.input.GetValue()[i[0][0]:i[0][1] + 1])
					self.output.SetCellBackgroundColour(gridRow, gridCol, bgColour)
					if yathiInPrevChar == 1:
						yathiInPrevChar = 0
						if ' ' not in self.input.GetValue()[yathiStartPos:i[0][0]] and \
							'/' not in self.input.GetValue()[yathiStartPos:i[0][0]]:
							self.output.SetCellValue(gridRow, 0, data.wrongLabel)
							self.increaseCellFontSize(gridRow, 0)
							self.increaseCellFontWeight(gridRow, 0)
							self.output.SetCellBackgroundColour(gridRow, 0, wx.RED)
							self.output.SetCellBackgroundColour(gridRow, gridCol, wx.RED)
							self.dictErrors[(gridRow, gridCol)] = data.yathiRequiredLabel
					if i[1] == 't':
						yathiInPrevChar = 1
						yathiStartPos = i[0][1] + 1
				self.increaseCellFontSize(gridRow, gridCol)
				gridCol = gridCol + 1
		while self.output.GetCellValue(gridRow, 0) == '':
			self.output.DeleteRows(gridRow, 1)
			gridRow -= 1
		self.output.SetGridCursor(0, 0)

	def printVruthamNames(self, vruthamNames):
		gRows, gCols = 0, 0
		# Print Header
		self.giveCell(gRows, 3)
		self.output.SetCellValue(0, 0, data.slokamLabel)
		self.increaseCellFontSize(0, 0)
		self.increaseCellFontWeight(0, 0)
		self.output.SetCellAlignment(0, 0, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
		self.output.SetCellBackgroundColour(0, 0, wx.TheColourDatabase.Find('LIGHT BLUE'))
		self.output.SetCellValue(0, 1, data.lineLabel)
		self.increaseCellFontSize(0, 1)
		self.increaseCellFontWeight(0, 1)
		self.output.SetCellAlignment(0, 1, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
		self.output.SetCellBackgroundColour(0, 1, wx.TheColourDatabase.Find('LIGHT BLUE'))
		self.output.SetCellValue(0, 2, data.lineVruthamGanangalLabel)
		self.increaseCellFontSize(0, 2)
		self.increaseCellFontWeight(0, 2)
		self.output.SetCellAlignment(0, 2, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
		self.output.SetCellBackgroundColour(0, 2, wx.TheColourDatabase.Find('LIGHT BLUE'))
		self.output.SetCellValue(0, 3, data.slokaVruthamLabel)
		self.increaseCellFontSize(0, 3)
		self.increaseCellFontWeight(0, 3)
		self.output.SetCellAlignment(0, 3, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
		self.output.SetCellBackgroundColour(0, 3, wx.TheColourDatabase.Find('LIGHT BLUE'))
		gRows = gRows + 1
		yathiBhangamSlokam = -1
		for i in vruthamNames:
			yathiBhangam = 'n'
			self.giveCell(gRows, 1)	
			self.output.SetDefaultColSize(190, 1)
			self.output.SetCellValue(gRows, 0, i[0])
			self.increaseCellFontWeight(gRows, 0)
			self.output.SetCellAlignment(gRows, 0, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
			self.output.SetCellValue(gRows, 1, i[1])
			self.increaseCellFontWeight(gRows, 1)
			self.output.SetCellAlignment(gRows, 1, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
			if i[2] != -1:
				self.output.SetCellValue(gRows, 2, data.vruthamTable[i[2]][1])
			else:
				self.output.SetCellValue(gRows, 2, data.iDontKnowLabel)
			self.increaseCellFontSize(gRows, 2)
			self.increaseCellFontWeight(gRows, 2)
			self.output.SetCellAlignment(gRows, 2, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
			if i[3] == -1:
				self.output.SetCellValue(gRows, 3, data.iDontKnowLabel)
			elif i[3] == -2:
				self.output.SetCellValue(gRows, 3, '')
			else:
				self.output.SetCellValue(gRows, 3, data.vruthamTable[i[3]][1])
			self.increaseCellFontSize(gRows, 3)
			self.increaseCellFontWeight(gRows, 3)
			self.output.SetCellAlignment(gRows, 3, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
			if int(i[0]) % 2 != 0:
				bgColour = wx.Colour(255, 255, 160)		# HTML value ffffa0
			else:
				bgColour = wx.Colour(255, 212, 160)		# HTML value ffd4a0
			self.output.SetCellBackgroundColour(gRows, 0, bgColour)
			self.output.SetCellBackgroundColour(gRows, 1, bgColour)
			if i[2] != -1:
				self.output.SetCellBackgroundColour(gRows, 2, bgColour)
				if i[4] == 'n':
					self.output.SetCellBackgroundColour(gRows, 2, wx.RED)
					self.dictErrors[(gRows, 2)] = data.yathiBhangamLabel
					yathiBhangamSlokam = i[0]
				if i[0] == yathiBhangamSlokam:
					yathiBhangam = 'y'
			else:
				self.output.SetCellBackgroundColour(gRows, 2, wx.RED)
			if i[3] != -1:
				self.output.SetCellBackgroundColour(gRows, 3, bgColour)
				if yathiBhangam == 'y':
					curSlokam = self.output.GetCellValue(gRows, 0)
					for i in range(0,4):
						if self.output.GetCellValue(gRows - i, 0) != curSlokam:
							break
						self.output.SetCellBackgroundColour(gRows - i, 3, wx.RED)
						self.dictErrors[(gRows - i, 3)] = data.yathiBhangamLabel
			else:
				curSlokam = self.output.GetCellValue(gRows, 0)
				for i in range(0,4):
					if self.output.GetCellValue(gRows - i, 0) != curSlokam:
						break
					self.output.SetCellBackgroundColour(gRows - i, 3, wx.RED)
			gRows = gRows + 1
		self.output.AutoSizeColumns()

	def goClick(self,event):
		self.checkFlgSet = 0
		if self.output.GetNumberRows() != 0:
			self.dictErrors = {}
			self.output.DeleteRows(0, self.output.GetNumberRows())
			self.output.DeleteCols(0, self.output.GetNumberCols())
		self.output.SetDefaultRowSize(25, 1)
		self.output.SetDefaultColSize(50, 1)
		if self.input.GetValue() == '':
			self.output.SetDefaultColSize(790, 1)
			self.giveCell()
			self.output.SetCellValue(0, 0, data.noPadyamGivenLabel)
			self.increaseCellFontSize(0, 0)
			return
		if filter(lambda x: x > u'\u0d00' and x < u'\u0d65', self.input.GetValue()) == '':
			self.output.SetDefaultColSize(790, 1)
			self.giveCell()
			self.output.SetCellValue(0, 0, data.givePadyamInMalLabel)
			self.increaseCellFontSize(0, 0)
			return
		if self.checkVruthamFlg == 1:
			if self.inVruthamName == '':
				self.output.SetDefaultColSize(790, 1)
				self.giveCell()
				self.output.SetCellValue(0, 0, data.noVruthamGivenLabel)
				self.increaseCellFontSize(0, 0)
				return
			self.checkFlgSet = 1
			self.outVruthamName, self.errLocs = getVrutham(self.input.GetValue(), self.inVruthamName)
			self.highLightErrors()
		else:
			self.checkFlgSet = 0
			self.outVruthamName, self.errLocs = getVrutham(self.input.GetValue(), '')
			self.printVruthamNames(self.outVruthamName)

	def clearClick(self, event):
		self.status.Clear()
		if self.output.GetNumberRows() != 0:
			self.dictErrors = {}
			self.output.DeleteRows(0, self.output.GetNumberRows())
			self.output.DeleteCols(0, self.output.GetNumberCols())
		self.output.SetDefaultRowSize(25, 1)
		self.output.SetDefaultColSize(50, 1)
		if self.input.GetValue() != '':
			diag = wx.MessageDialog(self, data.clearAreYouSureLabel,
							data.pleaseConfirmLabel, wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
			if diag.ShowModal() == wx.ID_YES:
				self.input.Clear()

	def closeClick(self, event):
		dlg = wx.MessageDialog(self, data.quitAreYouSureLabel,
							data.pleaseConfirmLabel, wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		if dlg.ShowModal() == wx.ID_YES:
			self.GetParent().Close(True)

class myMenu(wx.MenuBar):
	def __init__(self):
		wx.MenuBar.__init__(self)
		file = wx.Menu()
		edit = wx.Menu()
		tools = wx.Menu()
		help = wx.Menu()

		file.Append(101, '&Open...\tCtrl+O', 'Open a new utf-8 text file')
		file.Append(102, '&Save Input\tCtrl+S', 'Save the opened text file')
		file.Append(103, 'S&ave Input As...', 'Save input as a utf-8 text file')
		file.AppendSeparator()
		file.Append(105, 'E&xport Output to HTML', 'Save the result as HTML')
		file.Enable(105, 0)
		file.AppendSeparator()
		quit = wx.MenuItem(file, 104, '&Quit\tCtrl+Q', 'Quit the application')
		file.AppendItem(quit)

# TODO	edit.Append(201, '&Undo\tCtrl+Z', 'Undo last action')
# TODO	edit.Append(202, '&Redo\tCtrl+Y', 'Redo last action')
# TODO	edit.AppendSeparator()
# TODO	edit.Append(203, 'Cu&t\tCtrl+X', 'Cut and copy to clipboard')
# TODO	edit.Append(204, '&Copy\tCtrl+C', 'Copy to clipboard')
# TODO	edit.Append(205, '&Paste\tCtrl+V', 'Paste from clipboard')
# TODO	edit.Append(206, '&Delete\tDel', 'Delete')
# TODO	edit.AppendSeparator()
# TODO	edit.Append(207, '&Find...\tCtrl+F', 'Find item')
# TODO	edit.Append(208, 'F&ind Next\tF3', 'Find next')
# TODO	edit.Append(209, 'R&eplace...\tCtrl+H', 'Replace')
# TODO	edit.AppendSeparator()
		edit.Append(210, '&Select All\tCtrl+A', 'Select entire text')
		edit.Enable(210, 0)

		edit.Append(211, 'C&lear All\tCtrl+U', 'Clear entire text')

		tools.Append(301, 'Op&tions...\tCtrl+T', 'Open the options window')
		tools.Enable(301, 0)

		help.Append(401, '&Help Topics\tF1', 'Help Topics')
		help.Append(402, '&About...', 'About')

		self.Append(file, '&File')
		self.Append(edit, '&Edit')
		self.Append(tools, '&Tools')
		self.Append(help, '&Help')

class myFrame(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title,wx.Point(100,50), wx.Size(800,580))
		self.SetMenuBar(myMenu())
		self.Centre()
		self.Bind(wx.EVT_MENU, self.onOpen, id=101)
		self.Bind(wx.EVT_MENU, self.onSave, id=102)
		self.Bind(wx.EVT_MENU, self.onSaveAs, id=103)
		self.Bind(wx.EVT_MENU, self.onQuit, id=104)
		self.Bind(wx.EVT_MENU, self.onClearAll, id=211)
		self.Bind(wx.EVT_MENU, self.onHelpTopics, id=401)
		self.Bind(wx.EVT_MENU, self.onAbout, id=402)
# TODO	self.Bind(wx.EVT_CLOSE, self.onQuit)
		self.panel = myPanel(self, -1)
		sb = self.CreateStatusBar()
		sb.PushStatusText('Ready')
		self.path = -1
		self.SetSizeHints(800, 580)
		self.myHelpCtrl = HtmlHelpController()
		self.myHelpCtrl.AddBook("help/vshelp/vshelp.hhp", 0)
# TODO	self.myHelpCtrl.AddBook("help/vruthams/vruthams.hhp", 0)
		myIcon = wx.Icon(name = "iconvs.ico", type = wx.BITMAP_TYPE_ICO)
		self.SetIcon(myIcon)

	def onOpen(self, event):
		dlg = wx.FileDialog(self, message = "Choose a file",
				wildcard = "Text files (*.txt)|*.txt",
				style = wx.OPEN | wx.CHANGE_DIR)
		self.path = -1
		try:
			if dlg.ShowModal() == wx.ID_OK:
				self.path = dlg.GetFilename()
				f = open(self.path, "rb")
				uniPadyam = unicode(f.read(),'utf-8')
				self.panel.input.SetValue(uniPadyam)
		except:
			openErrDiag = wx.MessageDialog(self, 'File Opening Error: Maybe not a utf-8 encoded text?', 'File Error',
										wx.OK | wx.ICON_ERROR)
			openErrDiag.ShowModal()

	def onSave(self, event):
		if self.panel.input.GetValue() == '':
			statDiag = wx.MessageDialog(self, 'Nothing to save', 'Save Error',
										wx.OK | wx.ICON_ERROR)
			statDiag.ShowModal()
			self.path = -1
			return
		if self.path == -1:
			return self.onSaveAs(event)
		try:
			f = open(self.path, 'wb')
			outText = self.panel.input.GetValue().encode('utf-8')
			f.write(outText)
		except:
			saveErrDiag = wx.MessageDialog(self, 'File Write Error: Check permissions', 'Save Error',
										wx.OK | wx.ICON_ERROR)
			saveErrDiag.ShowModal()

	def onSaveAs(self, event):
		if self.panel.input.GetValue() == '':
			statDiag = wx.MessageDialog(self, 'Nothing to save', 'Save Error',
										wx.OK | wx.ICON_ERROR)
			statDiag.ShowModal()
			self.path = -1
			return
		dlg = wx.FileDialog(self, message = 'Save Input As...',
				wildcard = "Text files (*.txt)|*.txt",
				style = wx.SAVE | wx.CHANGE_DIR | wx.OVERWRITE_PROMPT)
		try:
			if dlg.ShowModal() == wx.ID_OK:
				self.path = dlg.GetFilename()
				f = open(self.path, "wb")
				outText = self.panel.input.GetValue().encode('utf-8')
				f.write(outText)
		except:
			saveAsErrDiag = wx.MessageDialog(self, 'File Write Error: Check permissions', 'Save Error',
										wx.OK | wx.ICON_ERROR)
			saveAsErrDiag.ShowModal()

	def onQuit(self, event):
		self.panel.closeClick(event)

	def onClearAll(self, event):
		self.panel.clearClick(event)

	def onHelpTopics(self, event):
		self.myHelpCtrl.DisplayContents()

	def onAbout(self, event):
		self.myAboutInfo = wx.AboutDialogInfo()
		self.myAboutInfo.SetName(data.aboutName)
		self.myAboutInfo.SetDescription(data.aboutDescription)
		self.myAboutInfo.SetDevelopers(data.aboutDevelopers)
		self.myAboutInfo.SetCopyright(data.aboutCopyright)
		self.myAboutInfo.SetWebSite(data.aboutWebSite)
		self.myAboutInfo.SetLicense(wordwrap(data.aboutLicense, 400, wx.ClientDC(self), 1))
		self.myAboutInfo.SetVersion(data.aboutVersion)
		wx.AboutBox(self.myAboutInfo)

class myApp(wx.App):
	def OnInit(self):
		self.frame = myFrame(None, -1, data.vruthaSahayiLabel)
		self.frame.Show(True)
		self.SetTopWindow(self.frame)
		return True

if __name__ == '__main__':
	app = myApp(0)
	app.MainLoop()
