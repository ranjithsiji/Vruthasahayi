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
import re, data

def findVrutham(glArray):
	glString  = ''.join(glArray)
	glString += '|'
	glLines = glString.split('|')
	glLines = glLines[:len(glLines) - 1]
	vruthamList = []
	lineCount = 1
	slokamCount = 1
	printSummary = 0
	slokaLakshanamList = []
	slokamLinesList = []
	anushtupSlokam = []
	for i in glLines:
		yathiPos = ()
		if i  == '':												# Print summary when slokam breaks
			if printSummary == 1:
				lineVruthamIds, slokaVruthamId = findSlokaVrutham(slokaLakshanamList, slokamLinesList)
				for num in range(1,len(lineVruthamIds) + 1):
					if num == 1:
						if slokaVruthamId != -1:
							sV = slokaVruthamId
						else:
							sV = -1
					else:
						sV = -2										# For printing null
					if data.vruthamTable[lineVruthamIds[len(lineVruthamIds) - num]][2] > 277:
						yathiPositions = (-1,-1)		# Clear yathi positions if sloka vrutham is an ardha/vishama vrutham
					else:
						yathiPositions = vruthamList[len(vruthamList) - num][4]
					vruthamList[len(vruthamList) - num] = vruthamList[len(vruthamList) - num][0], vruthamList[len(vruthamList) - num][1], lineVruthamIds[len(lineVruthamIds) - num], sV, yathiPositions
				slokamCount += 1
				printSummary = 0
			slokaLakshanamList = []
			slokamLinesList = []
			anushtupSlokam = []
			lineCount = 1
			continue
		printSummary = 1
		if len(i) == 8:
			anushtupSlokam.append(i)								# For checking anushtup if everything else fails
		if data.vruthamDict.has_key(i):
			vruthamId = data.vruthamDict[i]
			if data.yathiDict.has_key(vruthamId):
				yathiPos = data.yathiDict[vruthamId]
			vruthamList.append((str(slokamCount), str(lineCount), vruthamId, -2, yathiPos))
		else:
			if 'c' in i:
				vruthamId = convolutedFindVrutham(i, data.vruthamDict)
				if vruthamId >= 0:
					if data.yathiDict.has_key(vruthamId):
						yathiPos = data.yathiDict[vruthamId]
					vruthamList.append((str(slokamCount), str(lineCount), vruthamId, -2, yathiPos))
				else:
					vruthamList.append((str(slokamCount), str(lineCount), -1, -2, (-1,-1)))
			else:
				vruthamId = -1
				vruthamList.append((str(slokamCount), str(lineCount), -1, -2, (-1,-1)))
		slokaLakshanamList.append(vruthamId)
		slokamLinesList.append(i)
		if lineCount == 4:											# Print summary assuming slokam break after 4 lines
			lineVruthamIds, slokaVruthamId = findSlokaVrutham(slokaLakshanamList, slokamLinesList)
			if slokaVruthamId == -1 and len(anushtupSlokam) == 4:
				lineVruthamIds, slokaVruthamId = checkIfAnushtupFamily(anushtupSlokam)
			for num in range(1,len(lineVruthamIds) + 1):
				if num == 1:
					if slokaVruthamId != -1:
						sV = slokaVruthamId
					else:
						sV = -1
				else:
					sV = -2											# For printing null
				if data.vruthamTable[lineVruthamIds[4 - num]][2] > 277:		# Clear yathi positions if sloka vrutham
					yathiPositions = (-1,-1)								#    is an ardha/vishama vrutham
				else:
					yathiPositions = vruthamList[len(vruthamList) - num][4]
				vruthamList[len(vruthamList) - num] = vruthamList[len(vruthamList) - num][0], vruthamList[len(vruthamList) - num][1], lineVruthamIds[4 - num], sV, yathiPositions
			printSummary = 0					# Slokam end reached. Dont print again at the next blank line
			lineCount = 0						# Slokam end reached. Initialize line count
			slokamCount += 1					# Slokam end reached. Increase slokam count by 1
			slokaLakshanamList = []
			slokamLinesList = []
			anushtupSlokam = []
		lineCount += 1					# Increase line count normally
	return vruthamList

def convolutedFindVrutham(i, dict):
	if 'c' in i:
		il = i.replace('c','v', 1)		# Replace first prev char + chillu with laghu
		id = convolutedFindVrutham(il, dict)
		if id >= 0:
			return id
		ig = i.replace('c','-', 1) 		# Replace first prev char + chillu with guru
		id = convolutedFindVrutham(ig, dict)
		return id
	else:
		if dict.has_key(i):
			id = dict[i]
		else:
			id = -1
		return id

def findSlokaVrutham(slokaLakshanamList, slokamLinesList):
	prevVruthamId = -2
	for i in slokaLakshanamList:
		if prevVruthamId != -2 and i != prevVruthamId:
			break
		else:
			vruthamId = i
		if i == -1:
			break
		prevVruthamId = i
	else:
		return slokaLakshanamList, vruthamId

	return findArdhaVishamaVrutham(slokamLinesList, slokaLakshanamList)

def findArdhaVishamaVrutham(slokamLinesList, slokaLakshanamList):
	newLineVruthamIdsString = ''
	newLineVruthamIds = []
	for oneLine in slokamLinesList:
		newLineVruthamIds.append(convolutedFindVrutham(oneLine, data.avGanamDict))
	for i in newLineVruthamIds:
		newLineVruthamIdsString += str(i)
		newLineVruthamIdsString += '-'
	if data.ardhaVishamaVruthamDict.has_key(newLineVruthamIdsString):
		slokaVruthamId = data.ardhaVishamaVruthamDict[newLineVruthamIdsString]
		return newLineVruthamIds, slokaVruthamId
	else:
		return slokaLakshanamList, -1

def checkIfAnushtupFamily(anushtupSlokam):
	slokaVruthamId = -1
	lineVruthamIds = []
	for j in range(0,4):
		lineVruthamIds.append(-1)

	anushtupSlokamString = ''
	for line in anushtupSlokam:
		anushtupSlokamString += line
		anushtupSlokamString += '|'

	vakthram = re.compile(r'(?P<l1char1>.)'
		r'(?P<l1gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l1gan2>[vc][\-c][\-c])'
		r'(?P<l1char2>.)'
		r'(?P<sep1>[|])'
		r'(?P<l2char1>.)'
		r'(?P<l2gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l2gan2>[vc][\-c][\-c])'
		r'(?P<l2char2>.)'
		r'(?P<sep2>[|])'
		r'(?P<l3char1>.)'
		r'(?P<l3gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l3gan2>[vc][\-c][\-c])'
		r'(?P<l3char2>.)'
		r'(?P<sep3>[|])'
		r'(?P<l4char1>.)'
		r'(?P<l4gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l4gan2>[vc][\-c][\-c])'
		r'(?P<l4char2>.)'
		r'(?P<sep4>[|])')

	if vakthram.match(anushtupSlokamString):
		slokaVruthamId = 286									# vakthram
		lineVruthamIds = []
		for j in range(0,4):
			lineVruthamIds.append(slokaVruthamId)
		return lineVruthamIds, slokaVruthamId

	pathyaVakthram = re.compile(r'(?P<l1char1>.)'
		r'(?P<l1gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l1gan2>[vc][\-c][\-c])'
		r'(?P<l1char2>.)'
		r'(?P<sep1>[|])'
		r'(?P<l2char1>.)'
		r'(?P<l2gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l2gan2>[vc][\-c][vc])'
		r'(?P<l2char2>.)'
		r'(?P<sep2>[|])'
		r'(?P<l3char1>.)'
		r'(?P<l3gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l3gan2>[vc][\-c][\-c])'
		r'(?P<l3char2>.)'
		r'(?P<sep3>[|])'
		r'(?P<l4char1>.)'
		r'(?P<l4gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l4gan2>[vc][\-c][vc])'
		r'(?P<l4char2>.)'
		r'(?P<sep4>[|])')

	if pathyaVakthram.match(anushtupSlokamString):
		slokaVruthamId = 171									# paththhyAvakthram
		lineVruthamIds = []
		for j in range(0,4):
			lineVruthamIds.append(slokaVruthamId)
		return lineVruthamIds, slokaVruthamId

	vipareethaPathyaVakthram = re.compile(r'(?P<l1char1>.)'
		r'(?P<l1gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l1gan2>[vc][\-c][vc])'
		r'(?P<l1char2>.)'
		r'(?P<sep1>[|])'
		r'(?P<l2char1>.)'
		r'(?P<l2gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l2gan2>[vc][\-c][\-c])'
		r'(?P<l2char2>.)'
		r'(?P<sep2>[|])'
		r'(?P<l3char1>.)'
		r'(?P<l3gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l3gan2>[vc][\-c][vc])'
		r'(?P<l3char2>.)'
		r'(?P<sep3>[|])'
		r'(?P<l4char1>.)'
		r'(?P<l4gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l4gan2>[vc][\-c][\-c])'
		r'(?P<l4char2>.)'
		r'(?P<sep4>[|])')

	if vipareethaPathyaVakthram.match(anushtupSlokamString):
		slokaVruthamId = 302									# vipareethapaththhyAvakthram
		lineVruthamIds = []
		for j in range(0,4):
			lineVruthamIds.append(slokaVruthamId)
		return lineVruthamIds, slokaVruthamId

	chapalaVakthram = re.compile(r'(?P<l1char1>.)'
		r'(?P<l1gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l1gan2>[vc][vc][vc])'
		r'(?P<l1char2>.)'
		r'(?P<sep1>[|])'
		r'(?P<l2char1>.)'
		r'(?P<l2gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l2gan2>[vc][\-c][\-c])'
		r'(?P<l2char2>.)'
		r'(?P<sep2>[|])'
		r'(?P<l3char1>.)'
		r'(?P<l3gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l3gan2>[vc][vc][vc])'
		r'(?P<l3char2>.)'
		r'(?P<sep3>[|])'
		r'(?P<l4char1>.)'
		r'(?P<l4gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l4gan2>[vc][\-c][\-c])'
		r'(?P<l4char2>.)'
		r'(?P<sep4>[|])')

	if chapalaVakthram.match(anushtupSlokamString):
		slokaVruthamId = 118									# chapalAvakthram
		lineVruthamIds = []
		for j in range(0,4):
			lineVruthamIds.append(slokaVruthamId)
		return lineVruthamIds, slokaVruthamId

	bhaVipula = re.compile(r'(?P<l1char1>.)'
		r'(?P<l1gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l1gan2>[\-c][vc][vc])'
		r'(?P<l1char2>.)'
		r'(?P<sep1>[|])'
		r'(?P<l2char1>.)'
		r'(?P<l2gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l2gan2>(([\-c][vc][vc])|([vc][\-c][\-c])))'
		r'(?P<l2char2>.)'
		r'(?P<sep2>[|])'
		r'(?P<l3char1>.)'
		r'(?P<l3gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l3gan2>[\-c][vc][vc])'
		r'(?P<l3char2>.)'
		r'(?P<sep3>[|])'
		r'(?P<l4char1>.)'
		r'(?P<l4gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l4gan2>(([\-c][vc][vc])|([vc][\-c][\-c])))'
		r'(?P<l4char2>.)'
		r'(?P<sep4>[|])')

	if bhaVipula.match(anushtupSlokamString):
		slokaVruthamId = 207									# bhavipula
		lineVruthamIds = []
		for j in range(0,4):
			lineVruthamIds.append(slokaVruthamId)
		return lineVruthamIds, slokaVruthamId

	naVipula = re.compile(r'(?P<l1char1>.)'
		r'(?P<l1gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l1gan2>[vc][vc][vc])'
		r'(?P<l1char2>.)'
		r'(?P<sep1>[|])'
		r'(?P<l2char1>.)'
		r'(?P<l2gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l2gan2>(([vc][vc][vc])|([vc][\-c][\-c])))'
		r'(?P<l2char2>.)'
		r'(?P<sep2>[|])'
		r'(?P<l3char1>.)'
		r'(?P<l3gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l3gan2>[vc][vc][vc])'
		r'(?P<l3char2>.)'
		r'(?P<sep3>[|])'
		r'(?P<l4char1>.)'
		r'(?P<l4gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l4gan2>(([vc][vc][vc])|([vc][\-c][\-c])))'
		r'(?P<l4char2>.)'
		r'(?P<sep4>[|])')

	if naVipula.match(anushtupSlokamString):
		slokaVruthamId = 161									# navipula
		lineVruthamIds = []
		for j in range(0,4):
			lineVruthamIds.append(slokaVruthamId)
		return lineVruthamIds, slokaVruthamId

	raVipula = re.compile(r'(?P<l1char1>.)'
		r'(?P<l1gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l1gan2>[\-c][vc][\-c])'
		r'(?P<l1char2>.)'
		r'(?P<sep1>[|])'
		r'(?P<l2char1>.)'
		r'(?P<l2gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l2gan2>(([\-c][vc][\-c])|([vc][\-c][\-c])))'
		r'(?P<l2char2>.)'
		r'(?P<sep2>[|])'
		r'(?P<l3char1>.)'
		r'(?P<l3gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l3gan2>[\-c][vc][\-c])'
		r'(?P<l3char2>.)'
		r'(?P<sep3>[|])'
		r'(?P<l4char1>.)'
		r'(?P<l4gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l4gan2>(([\-c][vc][\-c])|([vc][\-c][\-c])))'
		r'(?P<l4char2>.)'
		r'(?P<sep4>[|])')

	if raVipula.match(anushtupSlokamString):
		slokaVruthamId = 269									# ravipula
		lineVruthamIds = []
		for j in range(0,4):
			lineVruthamIds.append(slokaVruthamId)
		return lineVruthamIds, slokaVruthamId

	maVipula = re.compile(r'(?P<l1char1>.)'
		r'(?P<l1gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l1gan2>[\-c][\-c][\-c])'
		r'(?P<l1char2>.)'
		r'(?P<sep1>[|])'
		r'(?P<l2char1>.)'
		r'(?P<l2gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l2gan2>(([\-c][\-c][\-c])|([vc][\-c][\-c])))'
		r'(?P<l2char2>.)'
		r'(?P<sep2>[|])'
		r'(?P<l3char1>.)'
		r'(?P<l3gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l3gan2>[\-c][\-c][\-c])'
		r'(?P<l3char2>.)'
		r'(?P<sep3>[|])'
		r'(?P<l4char1>.)'
		r'(?P<l4gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l4gan2>(([\-c][\-c][\-c])|([vc][\-c][\-c])))'
		r'(?P<l4char2>.)'
		r'(?P<sep4>[|])')

	if maVipula.match(anushtupSlokamString):
		slokaVruthamId = 245									# mavipula
		lineVruthamIds = []
		for j in range(0,4):
			lineVruthamIds.append(slokaVruthamId)
		return lineVruthamIds, slokaVruthamId

	thaVipula = re.compile(r'(?P<l1char1>.)'
		r'(?P<l1gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l1gan2>[\-c][\-c][vc])'
		r'(?P<l1char2>.)'
		r'(?P<sep1>[|])'
		r'(?P<l2char1>.)'
		r'(?P<l2gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l2gan2>(([\-c][\-c][vc])|([vc][\-c][\-c])))'
		r'(?P<l2char2>.)'
		r'(?P<sep2>[|])'
		r'(?P<l3char1>.)'
		r'(?P<l3gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l3gan2>[\-c][\-c][vc])'
		r'(?P<l3char2>.)'
		r'(?P<sep3>[|])'
		r'(?P<l4char1>.)'
		r'(?P<l4gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l4gan2>(([\-c][\-c][vc])|([vc][\-c][\-c])))'
		r'(?P<l4char2>.)'
		r'(?P<sep4>[|])')

	if thaVipula.match(anushtupSlokamString):
		slokaVruthamId = 139									# thavipula
		lineVruthamIds = []
		for j in range(0,4):
			lineVruthamIds.append(slokaVruthamId)
		return lineVruthamIds, slokaVruthamId

	anushtup = re.compile(r'(?P<l1char1>.)'
		r'(?P<l1gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l1gan2>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][vc][vc])|([\-c][\-c][\-c])))'
		r'(?P<l1char2>.)'
		r'(?P<sep1>[|])'
		r'(?P<l2char1>.)'
		r'(?P<l2gan1>(([vc][\-c][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l2gan2>[vc][\-c][vc])'
		r'(?P<l2char2>.)'
		r'(?P<sep2>[|])'
		r'(?P<l3char1>.)'
		r'(?P<l3gan1>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l3gan2>(([vc][\-c][\-c])|([\-c][vc][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][vc][vc])|([\-c][\-c][\-c])))'
		r'(?P<l3char2>.)'
		r'(?P<sep3>[|])'
		r'(?P<l4char1>.)'
		r'(?P<l4gan1>(([vc][\-c][\-c])|([\-c][\-c][vc])|([\-c][vc][vc])|([vc][\-c][vc])|([\-c][\-c][\-c])))'
		r'(?P<l4gan2>[vc][\-c][vc])'
		r'(?P<l4char2>.)'
		r'(?P<sep4>[|])')

	if anushtup.match(anushtupSlokamString):
		slokaVruthamId = 10										# anushTupp
		lineVruthamIds = []
		for j in range(0,4):
			lineVruthamIds.append(slokaVruthamId)
		return lineVruthamIds, slokaVruthamId

	return lineVruthamIds, slokaVruthamId
