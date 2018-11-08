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
from matra import *
from checkvrutham import *
from findvrutham import *
from utils import *

def markCorrectSyls(errlocs, sylArray):
	modArray = []
	for i in range(0,len(errlocs)):
		if errlocs[i] == 'x':					# Guru in place of laghu or vice versa
			modArray.append((sylArray[i], 'n'))
		elif errlocs[i] == 't':					# Marking yathi
			modArray.append((sylArray[i], 't'))
		elif errlocs[i] == 'g':					# For anushtup non-matching ganams
			modArray.append((sylArray[i], 'g'))
		else:
			modArray.append((sylArray[i], 'y'))
	return modArray

def getVrutham(padyam, vrutham):
	errlocs = []
	modArray = []
	if padyam == '':
		return 'No Padyam Given', errlocs
	glArray, sylArray = getMatraArray(padyam)

	if vrutham != '':
		errlocs = checkVrutham(vrutham, glArray)
		modArray = markCorrectSyls(errlocs, sylArray)
	else:
		vrutham = findVrutham(glArray)
		prevPos = -1
		newLinePos = 0
		multipleVruthams = 0
		prevSlokamNumber = -2
		prevLineVruthamId = -2
		for i in range(0,len(vrutham)):
			curPos = sylArray.index((-1,-1),newLinePos)
			while curPos - prevPos < 2:
				prevPos = curPos
				newLinePos += 1
				curPos = sylArray.index((-1, -1),newLinePos)
			sylLine = sylArray[prevPos + 1:curPos]
			yathiBool = 'y'
			if vrutham[i][2] != -1:
				if data.similarVruthamDict.has_key(vrutham[i][2]):	# Check if vrutham is diff from another only by yathi
					similarVruthamList = data.similarVruthamDict[vrutham[i][2]]
					for vruthamId in similarVruthamList:
						if data.yathiDict.has_key(vruthamId):
							yathiPos = data.yathiDict[vruthamId]
							yathiBool = 'y'
							for j in yathiPos:
								if j == -1:
									continue
								if ' ' not in padyam[sylLine[j-1][1]:sylLine[j][0]] and \
									'/' not in padyam[sylLine[j-1][1]:sylLine[j][0]]:
									yathiBool = 'n'
									break
							if yathiBool == 'y':
								lineVruthamId = vruthamId
								break
							else:
								lineVruthamId = vrutham[i][2]
						else:
							yathiBool = 'y'
							continue
					newSlokaVruthamId = lineVruthamId
					if prevSlokamNumber != -2 and vrutham[i][0] != prevSlokamNumber:
						multipleVruthams = 0
					else:
						if prevLineVruthamId != -2 and lineVruthamId != prevLineVruthamId:
							multipleVruthams = 1
					if vrutham[i][3] != -2 and vrutham[i][3] != -1:	# Safe since only samavruthams come here
						if multipleVruthams == 1:
							slokaVruthamId = -1
						else:
							slokaVruthamId = newSlokaVruthamId
					else:
						slokaVruthamId = vrutham[i][3]					# For lines 1,2 and 3 of the slokam
					prevSlokamNumber = vrutham[i][0]
					prevLineVruthamId = lineVruthamId
				else:
					lineVruthamId = vrutham[i][2]
					slokaVruthamId = vrutham[i][3]
					for j in vrutham[i][4]:
						if j == -1:
							continue
						if ' ' not in padyam[sylLine[j-1][1]:sylLine[j][0]] and \
							'/' not in padyam[sylLine[j-1][1]:sylLine[j][0]]:
							yathiBool = 'n'
							break
			else:
				lineVruthamId = vrutham[i][2]
				slokaVruthamId = vrutham[i][3]
			vrutham[i] = vrutham[i][0], vrutham[i][1], lineVruthamId, slokaVruthamId, yathiBool
			prevPos = curPos
			newLinePos += 1
	return vrutham, modArray
