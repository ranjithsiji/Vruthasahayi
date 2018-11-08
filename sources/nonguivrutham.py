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
from interface import *
from utils import *

def findResult(padyam, vrutham):
	if padyam == '':
		return 'No Padyam Given', []
	uniPadyam = unicode(padyam,'utf-8')
	uniVrutham = unicode(vrutham,'utf-8')
	uniVrutham = uniVrutham.replace('\n', '')
	return getVrutham(uniPadyam, uniVrutham)

if __name__ == '__main__':
	inpPadyam = openPadyamFile()
	padyam = inpPadyam.read()

	inpVrutham = openVruthamFile()
	vrutham = inpVrutham.read()

	vrutham, errLocs = findResult(padyam, vrutham)
	print vrutham, errLocs
