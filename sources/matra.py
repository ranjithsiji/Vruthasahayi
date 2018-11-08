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
from syllable import *
from utils import *

def findCharType(sylChars):
	sylCharCount = len(sylChars)
	if (sylCharCount == 1):
		if sylChars[0] in [u'\u0d06', u'\u0d08', u'\u0d0a', u'\u0d0f', u'\u0d10', u'\u0d13', u'\u0d14']:
			return 'sg'	# Independent vowels (AA, II, UU, EE, AI, AU)
		else:
			return 'sl'
	elif (sylCharCount == 2):
		if u'\u0d4d' in sylChars:
			# special case for chillu
			for oneChar in sylChars:
				if oneChar in [u'\u0d23', u'\u0d28']:
					return 'nch'
				if oneChar in [u'\u0d30', u'\u0d31', u'\u0d32', u'\u0d33']:
					return 'rlch'
				if (oneChar >= u'\u0d15' and oneChar <= u'\u0d39'):
					return 'hc'			# Half consonant
			return 'sl'					# Will not come here
		for oneChar in sylChars:
			if oneChar in [u'\u0d3e', u'\u0d40', u'\u0d42', u'\u0d47', u'\u0d48', u'\u0d4b', u'\u0d4c', u'\u0d57', u'\u0d02', u'\u0d03']:
				return 'sg' # Dependent vowels (AA, II, UU, EE, AI, OO, AU), ANUSVARA, VISARGA
		return 'sl'
	elif (sylCharCount == 3):
		if u'\u0d4d' in sylChars:
			if u'\u0d41' in sylChars:
				return 'sl'
			elif u'\u200d' in sylChars:
				for oneChar in sylChars:
					if oneChar in [u'\u0d23', u'\u0d28']:
						return 'nch'
					if oneChar in [u'\u0d30', u'\u0d31', u'\u0d32', u'\u0d33']:
						return 'rlch'
			elif u'\u200c' in sylChars:
				for oneChar in sylChars:
					if (oneChar >= u'\u0d15' and oneChar <= u'\u0d39'):
						return 'hc'			# Half consonant
				return 'sl'
			else:
				return 'kl'
		for oneChar in sylChars:
			if oneChar == u'\u0d46':
				for anotherChar in sylChars:
					if anotherChar in [u'\u0d3e']:
						return 'sl'
					else:
						return 'sg'
			elif oneChar == u'\u0d47':
				return 'sg'
		return 'sg'
	else:											# If sylCharCount is 4 or more
		if sylChars[0] in [u'\u0d23', u'\u0d28', u'\u0d30',  u'\u0d31', u'\u0d32', u'\u0d33'] and sylChars[1] == u'\u0d4d' and sylChars[2] == u'\u200d':
			return 'ccc'							# Chillu before consonant combo. Extra special case
		if u'\u0d46' in sylChars:					# Dependent vowel sign E
			if u'\u0d3e' in sylChars:				# Dependent vowel sign AA
				return 'kl'							# Case: KO
			elif u'\u0d57' in sylChars:				# Dependent vowel sign AU
				return 'kg'							# Case: KAU
		for oneChar in sylChars:
			if oneChar in [u'\u0d3e', u'\u0d40', u'\u0d42', u'\u0d47', u'\u0d48', u'\u0d4b', u'\u0d4c', u'\u0d02', u'\u0d03']:
				return 'kg'
		return 'kl'

def getMatraArray(uniPadyam):
	strippedPadyam = changeNewLineToPipe(uniPadyam)
	charCount = len(strippedPadyam)
	prev = 0
	sylCount = 0
	lineSylCount = 0
	prevType = ' '
	glArray = []
	sylArray = []
	while (prev < charCount):
		if not isMal(strippedPadyam[prev]):
			prev = prev + 1
			continue
		if (strippedPadyam[prev] == '|'):							# If end of a line
			lineSylCount = 0
			glArray.append('|')										# Append '|' in glArray to mark end of line
			sylArray.append((-1,-1))								# Append (-1,-1) in sylArray to mark end of line
			prevPrevType = prevType
			prevType = '|'
			prev = prev + 1
			sylCount = sylCount + 1
			continue
		syllable = findSyllable(strippedPadyam, prev, charCount)
		sylList = strippedPadyam[prev:syllable]
		charType = findCharType(sylList)
		if (charType == 'sl'):
			glArray.append('v')
			sylArray.append((prev,syllable-1))
		elif (charType == 'sg'):
			glArray.append('-')
			sylArray.append((prev,syllable-1))
		elif (charType == 'kl'):
			if (sylCount > 0):
				if (lineSylCount > 0):
					glArray[sylCount - 1] = '-'
			glArray.append('v')
			sylArray.append((prev,syllable-1))
		elif (charType == 'kg'):
			if (sylCount > 0):
				if (lineSylCount > 0):
					glArray[sylCount - 1] = '-'
			glArray.append('-')
			sylArray.append((prev,syllable-1))
		elif (charType == 'nch'):						# Type nch (Chillu n, N)
			if (sylCount > 0) and (lineSylCount > 0):
				glArray[sylCount - 1] = '-'
				sylArray[sylCount -1] = sylArray[sylCount -1][0], syllable - 1
				sylCount = sylCount - 1
		elif (charType == 'rlch'):						# Type rlch (Chillu r, R, l, L)
			if (sylCount > 0) and (lineSylCount > 0):
				if glArray[sylCount - 1] != '-':
					glArray[sylCount - 1] = 'c'
				sylArray[sylCount -1] = sylArray[sylCount -1][0], syllable - 1
				sylCount = sylCount - 1
		elif (charType == 'hc'):						# Half consonant
			if (sylCount > 0) and (lineSylCount > 0):
				glArray[sylCount - 1] = '-'
				sylArray[sylCount -1] = sylArray[sylCount -1][0], syllable - 1
				sylCount = sylCount - 1
		else:											# Chillu before consonant combo. Extra special case
			if (sylCount > 0) and (lineSylCount > 0):
				if glArray[sylCount - 1] != '-':
					glArray[sylCount - 1] = 'c'
				sylArray[sylCount -1] = sylArray[sylCount -1][0], sylArray[sylCount -1][1] + 3
				sylCount = sylCount - 1
				syllable = prev + 3
		prev = syllable
		prevPrevType = prevType
		prevType = charType
		lineSylCount = lineSylCount + 1
		sylCount = sylCount + 1
	return glArray, sylArray
