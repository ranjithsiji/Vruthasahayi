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

def getGlSeq(vruthamId):
	return data.vruthamTable[vruthamId][4]

def checkVrutham(uniVrutham, glArray):
	glString  = ''.join(glArray)
	glLines = glString.split('|')
	glLines = glLines[:len(glLines) - 1]

	vruthamId = data.getVruthamId(uniVrutham)
	ardhaVishamaVrutham = 'n'
	upajathiVrutham = 'n'
	if vruthamId == -1:							# For non-gui
		return [((-1, -1), 'n')] 
	glSeq = getGlSeq(vruthamId)
	if data.yathiDict.has_key(vruthamId):		# Returns true only for Samavruthams
		yathiPos = data.yathiDict[vruthamId]
	else:
		yathiPos = (-1,-1)
	if glSeq == 'ANUSHTUP':
		errLocs = checkVruthamForAnushtupFamily(vruthamId, glLines)
		return errLocs
	elif glSeq[0:2] == 'AV':
		ardhaVishamaVrutham = 'y'
		glSeq = glSeq[3:len(glSeq)]
		glSeqLines = glSeq.split('|')
		if vruthamId in [49, 50]:
			upajathiVrutham = 'y'
	posCount = 0
	errLocs = []
	lineNum = 0

	for oneLine in glLines:
		if oneLine == '':
			errLocs.append('|')
			lineNum = 0
			continue
		if ardhaVishamaVrutham == 'y':
			glSeqLine = glSeqLines[lineNum % 4]
		else:
			glSeqLine = glSeq
		lineNum = lineNum + 1
		posCount = 0
		for i in oneLine:
			if posCount > len(glSeqLine) - 1:
				errLocs.append('x')
			elif upajathiVrutham == 'y' and posCount == 0:
				errLocs.append(i)					# First syl in a line correct in case of upajathi
			elif posCount == len(glSeqLine) - 1 and vruthamId not in [100, 337]:	# Last syl in a line can be considered
				errLocs.append(i)													# correct except for Sree and khaga
			elif i == glSeqLine[posCount] or i == 'c':
				if posCount + 1 in yathiPos[1:]:
					errLocs.append('t')				# Marking yathi position
				else:
					errLocs.append(i)
			else:
				errLocs.append('x')
			posCount = posCount + 1
		errLocs.append('|')
	return errLocs

def checkVruthamForAnushtupFamily(vruthamId, glLines):
	errLocs = []
	lineNum = 0

	for oneLine in glLines:
		if oneLine == '':
			errLocs.append('|')
			lineNum = 0
			continue
		lineNum = lineNum + 1
		curErrLocs = []
		curErrLocs.append('a')
		if vruthamId == 10:						# anushTuP
			if lineNum % 2 == 1:
				ganam1 = re.compile(r'^.(?=(([vc][vc][vc])|([vc][vc][\-c])))')
			else:
				ganam1 = re.compile(r'^.(?=(([\-c][vc][\-c])|([vc][vc][vc])|([vc][vc][\-c])))')
		else:									# All others
			ganam1 = re.compile(r'^.(?=(([vc][vc][vc])|([vc][vc][\-c])))')

		if ganam1.search(oneLine):
			curErrLocs.extend(['g', 'g', 'g'])
		else:
			curErrLocs.extend(['a', 'a', 'a'])

		if vruthamId == 286:					# vakthram
			ganam2 = re.compile(r'^....(?![vc][\-c][\-c])')
		elif vruthamId == 171:					# paththhyAvakthram
			if lineNum % 2 == 1:
				ganam2 = re.compile(r'^....(?![vc][\-c][\-c])')
			else:
				ganam2 = re.compile(r'^....(?![vc][\-c][vc])')
		elif vruthamId == 302:					# vipareethapaththhyAvakthram
			if lineNum % 2 == 1:
				ganam2 = re.compile(r'^....(?![vc][\-c][vc])')
			else:
				ganam2 = re.compile(r'^....(?![vc][\-c][\-c])')
		elif vruthamId == 118:					# chapalAvakthram
			if lineNum % 2 == 1:
				ganam2 = re.compile(r'^....(?![vc][vc][vc])')
			else:
				ganam2 = re.compile(r'^....(?![vc][\-c][\-c])')
		elif vruthamId == 207:					# bhavipula
			if lineNum % 2 == 1:
				ganam2 = re.compile(r'^....(?![\-c][vc][vc])')
			else:
				ganam2 = re.compile(r'^....(?!(([\-c][vc][vc])|([vc][\-c][\-c])))')
		elif vruthamId == 161:					# navipula
			if lineNum % 2 == 1:
				ganam2 = re.compile(r'^....(?![vc][vc][vc])')
			else:
				ganam2 = re.compile(r'^....(?!(([vc][vc][vc])|([vc][\-c][\-c])))')
		elif vruthamId == 269:					# ravipula
			if lineNum % 2 == 1:
				ganam2 = re.compile(r'^....(?![\-c][vc][\-c])')
			else:
				ganam2 = re.compile(r'^....(?!(([\-c][vc][\-c])|([vc][\-c][\-c])))')
		elif vruthamId == 245:					# mavipula
			if lineNum % 2 == 1:
				ganam2 = re.compile(r'^....(?![\-c][\-c][\-c])')
			else:
				ganam2 = re.compile(r'^....(?!(([\-c][\-c][\-c])|([vc][\-c][\-c])))')
		elif vruthamId == 139:					# thavipula
			if lineNum % 2 == 1:
				ganam2 = re.compile(r'^....(?![\-c][\-c][vc])')
			else:
				ganam2 = re.compile(r'^....(?!(([\-c][\-c][vc])|([vc][\-c][\-c])))')
		else:									# anushTuP
			if lineNum % 2 == 1:
				ganam2 = re.compile(r'^.(?=(([vc][\-c][vc])|([vc][vc][\-c])))')
			else:
				ganam2 = re.compile(r'^....(?![vc][\-c][vc])')

		if ganam2.search(oneLine):
			curErrLocs.extend(['g', 'g', 'g'])
		else:
			curErrLocs.extend(['a', 'a', 'a'])
		curErrLocs.append('a')
		if len(oneLine) > 8:
			for i in range(0,len(oneLine) - 8):
				curErrLocs.append('x')
		curErrLocs = curErrLocs[0:len(oneLine)]
		errLocs.extend(curErrLocs)
		errLocs.append('|')
	return errLocs
