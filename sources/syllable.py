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
import string

def isMal(x):
	if ((x > u'\u0d00') and (x < u'\u0d65')):
		return 1
	elif (x == '|'):
		return 1
#	elif (x == ' '):
#		return 1
	return 0

def atoh(s, hexdigits = string.hexdigits):
	value = 0
	for char in s:
		index = string.find(string.hexdigits, char)
		if index >= 16:
			index = index - 6
		value = value*16 + index
	return value

def getCharClass(char):
	_xx = 0						# CC_RESERVED
	_mp = 2						# CC_MODIFYING_MARK_POST
	_iv = 3						# CC_INDEPENDENT_VOWEL
	_ct = (4 | 0x80000000)		# (CC_CONSONANT | CF_CONSONANT)
	_pb = (_ct | 0x08000000)	# (_ct | CF_POST_BASE)
	_cn = (5 | 0x80000000)		# CC_CONSONANT_WITH_NUKTA | CF_CONSONANT
	_dv = 7						# CC_DEPENDENT_VOWEL
	_dr = (_dv | 0x00800000)	# _dv | CF_MATRA_POST
	_dl = (_dv | 0x04000000)	# _dv | CF_MATRA_PRE
	_x1 = (1 << 16)				# (1 << CF_INDEX_SHIFT)
	_x2 = (1 << 16)				# (2 << CF_INDEX_SHIFT)
	_x3 = (1 << 16)				# (3 << CF_INDEX_SHIFT)
	_s1 = (_dv | _x1)			# (_dv | _x1)
	_s2 = (_dv | _x2)			# (_dv | _x2)
	_s3 = (_dv | _x3)			# (_dv | _x3)
	_vr = 8						# CC_VIRAMA
	mlymCharClasses = [ _xx, _xx, _mp, _mp, _xx, _iv, _iv, _iv, _iv, _iv, _iv, _iv, _iv, _xx, _iv, _iv,	# 0D00 - 0D0F
						_iv, _xx, _iv, _iv, _iv, _ct, _ct, _ct, _ct, _ct, _ct, _ct, _ct, _ct, _ct, _ct,	# 0D10 - 0D1F
						_ct, _ct, _ct, _ct, _ct, _ct, _ct, _ct, _ct, _xx, _ct, _ct, _ct, _ct, _ct, _pb,	# 0D20 - 0D2F
						_cn, _cn, _ct, _ct, _ct, _pb, _ct, _ct, _ct, _ct, _xx, _xx, _xx, _xx, _dr, _dr,	# 0D30 - 0D3F
						_dr, _dr, _dr, _dr, _xx, _xx, _dl, _dl, _dl, _xx, _s1, _s2, _s3, _vr, _xx, _xx,	# 0D40 - 0D4F
						_xx, _xx, _xx, _xx, _xx, _xx, _xx, _dr, _xx, _xx, _xx, _xx, _xx, _xx, _xx, _xx,	# 0D50 - 0D5F
						_iv, _iv, _xx, _xx, _xx, _xx, _xx, _xx, _xx, _xx, _xx, _xx, _xx, _xx, _xx, _xx]	# 0D60 - 0D6F
	if (char == u'\u200d'):								# C_SIGN_ZWJ
		return 0x80000000 | 9								# CF_CONSONANT | CC_ZERO_WIDTH_MARK
	if (char == u'\u200c'):								# C_SIGN_ZWNJ
		return 9											# CC_ZERO_WIDTH_MARK
	if ((char < u'\u0d00') or (char > u'\u0d65')):
		return 0											# CC_RESERVED
	uniChar = repr(char)
	hexString = uniChar.replace('u\'\\u','')
	hexString = hexString.replace('\'','')
	ch = atoh(hexString)
	return mlymCharClasses[ch - 0x0d00]

def findSyllable(chars, prev, charCount):
	stateTable =   [[ 1,  1,  1,  5,  3,  2,  1,  1,  1,  1,  1],
					[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
					[-1,  6,  1, -1, -1, -1, -1,  5,  4, -1, -1],
					[-1,  6,  1, -1, -1, -1,  2,  5,  4, 10,  9],
					[-1, -1, -1, -1,  3,  2, -1, -1, -1,  8, -1],
					[-1,  6,  1, -1, -1, -1, -1, -1, -1, -1, -1],
					[-1,  7,  1, -1, -1, -1, -1, -1, -1, -1, -1],
					[-1, -1,  1, -1, -1, -1, -1, -1, -1, -1, -1],
					[-1, -1, -1, -1,  3,  2, -1, -1, -1, -1, -1],
					[-1, -1, -1, -1, -1, -1, -1, -1, -1,  8, -1],
					[-1, -1, -1, -1, -1, -1, -1, -1,  8, -1,  8]]
	cursor = prev
	state = 0
	while (cursor < charCount):
		charClass = getCharClass(chars[cursor])
		state = stateTable[state][charClass & 0x0000FFFF] # Masking with CF_CLASS_MASK
		if (state < 0):
			return cursor
		cursor = cursor + 1
	return cursor
