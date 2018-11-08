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

ganamDict = {	'v--':u'\u0d2f',					# ya gaNam
				'-v-':u'\u0d30',					# ra gaNam
				'--v':u'\u0d24',					# tha gaNam
				'-vv':u'\u0d2d',					# bha gaNam
				'v-v':u'\u0d1c',					# ja gaNam
				'vv-':u'\u0d38',					# sa gaNam
				'---':u'\u0d2e',					# ma gaNam
				'vvv':u'\u0d28',					# na gaNam
				'-':u'\u0d17',						# guru
				'v':u'\u0d32'						# laghu
				}

vruthamDict = {	'-':337,							# Sree
				'v':100,							# khaga
				'--':377,							# sthree
				'-v':377,							# sthree
				'vv':325,							# Sivam
				'v-':325,							# Sivam
				'---':164,							# naari
				'--v':164,							# naari
				'-v-':254,							# mr^gi
				'-vv':254,							# mr^gi
				'----':63,							# kanya
				'---v':63,							# kanya
				'--v-':311,							# vENi
				'--vv':311,							# vENi
				'-----':109,						# gauri
				'----v':109,						# gauri
				'v-v--':250,						# mAla
				'v-v-v':250,						# mAla
				'--vv--':135,						# thanumaddhya
				'--vv-v':135,						# thanumaddhya
				'--vvv-':294,						# vasumathi
				'--vvvv':294,						# vasumathi
				'-v--v-':261,						# rathnAvali
				'-v--vv':261,						# rathnAvali
				'---vv--':235,						# madalEkha
				'---vv-v':235,						# madalEkha
				'vvv-vv-':238,						# madhumathi
				'vvv-vvv':238,						# madhumathi
				'vv--v--':384,						# hamsamAla
				'vv--v-v':384,						# hamsamAla
				'--------':301,						# vidyunmAla
				'-------v':301,						# vidyunmAla
				'-vv-vv--':123,						# chithrapada
				'-vv-vv-v':123,						# chithrapada
				'-vv--vv-':248,						# mANavakam
				'-vv--vvv':248,						# mANavakam
				'-v-v-v-v':342,						# samAnika
				'-v-v-v--':342,						# samAnika
				'v-v-v-v-':192,						# pramANika
				'v-v-v-vv':192,						# pramANika
				'--v-v-v-':163,						# nArAchika
				'--v-v-vv':163,						# nArAchika
				'--vv-vv-':66,						# kabari
				'--vv-vvv':66,						# kabari
				'---vvv--':385,						# hamsarutha
				'---vvv-v':385,						# hamsarutha
				'v-v--v--':299,						# vithAnam
				'v-v--v-v':299,						# vithAnam
				'-vv-v-v-':162,						# nAgarikam
				'-vv-v-vv':162,						# nAgarikam
				'---vvvv--':268,					# ramaNeeyam
				'---vvvv-v':268,					# ramaNeeyam
				'-vv---vv-':224,					# maNimaddhyam
				'-vv---vvv':224,					# maNimaddhyam
				'-v-vvvvv-':200,					# phalamukhi
				'-v-vvvvvv':200,					# phalamukhi
				'vvvvvv---':328,					# SiSubhr^tha
				'vvvvvv--v':328,					# SiSubhr^tha
				'-v-vvv-v-':204,					# bhadrika
				'-v-vvv-vv':204,					# bhadrika
				'vv-vv-v-v-':366,					# sumukhi
				'vv-vv-v-vv':366,					# sumukhi
				'-vv---vv--':120,					# champakamAla
				'-vv---vv-v':120,					# champakamAla
				'----vvvv--':226,					# maththa
				'----vvvv-v':226,					# maththa
				'---vv-v-v-':327,					# SuddhavirAL
				'---vv-v-vv':327,					# SuddhavirAL
				'-v-v-v-v--':242,					# mayoorasAriNi
				'-v-v-v-v-v':242,					# mayoorasAriNi
				'vvv-v-v-v-':240,					# manOrama
				'vvv-v-v-vv':240,					# manOrama
				'-vv-vv-vv-':352,					# sAravathi
				'-vv-vv-vvv':352,					# sAravathi
				'--vv---vv-':371,					# sushama
				'--vv---vvv':371,					# sushama
				'--v--vv-v--':37,					# indravajra
				'--v--vv-v-v':37,					# indravajra
				'v-v--vv-v--':57,					# upEndravajra
				'v-v--vv-v-v':57,					# upEndravajra
				'-v-vvv-v-v-':262,					# rathhOddhatha
				'-v-vvv-v-vv':262,					# rathhOddhatha
				'-v-vvv-vv--':376,					# svAgatha
				'-v-vvv-vv-v':376,					# svAgatha
				'-----v--v--':323,					# SAlini
				'-----v--v-v':323,					# SAlini
				'----vv--v--':297,					# vAthOrMi
				'----vv--v-v':297,					# vAthOrMi
				'-vv-vv-vv--':147,					# dOdhakam
				'-vv-vv-vv-v':147,					# dOdhakam
				'----vvvvvv-':211,					# bhramaravilasitham
				'----vvvvvvv':211,					# bhramaravilasitham
				'-vv--vvvv--':258,					# maukthikamAla
				'-vv--vvvv-v':258,					# maukthikamAla
				'vv-vv-vv-v-':48,					# upachithram
				'vv-vv-vv-vv':48,					# upachithram
				'v-v--v--v--':95,					# kEraLi
				'v-v--v--v-v':95,					# kEraLi
				'vvvv-vv-vv-':367,					# sumukhi
				'vvvv-vv-vvv':367,					# sumukhi
				'vvvv---vv--':257,					# maukthikapamkthi
				'vvvv---vv-v':257,					# maukthikapamkthi
				'-v-v-v-v-v-':335,					# SyEnika
				'-v-v-v-v-vv':335,					# SyEnika
				'vvv-v--v-v-':344,					# sammatha
				'vvv-v--v-vv':344,					# sammatha
				'v--v--v--v-':83,					# kumAri
				'v--v--v--vv':83,					# kumAri
				'--vv-vv-v--':54,					# upasthhitha
				'--vv-vv-v-v':54,					# upasthhitha
				'vvvvvv-vv--':184,					# pr^ththhvi
				'vvvvvv-vv-v':184,					# pr^ththhvi
				'vvvvvv--v--':125,					# chithravr^ththa
				'vvvvvv--v-v':125,					# chithravr^ththa
				'vvvvvvvv---':308,					# vr^ththa
				'vvvvvvvv--v':308,					# vr^ththa
				'vvvvvv-v-v-':201,					# bhadraka
				'vvvvvv-v-vv':201,					# bhadraka
				'v-vvv---v--':55,					# upasthhitham
				'v-vvv---v-v':55,					# upasthhitham
				'-vv-vv-vv--':121,					# chAraNageetham
				'-vv-vv-vv-v':121,					# chAraNageetham
				'vvvvvvvvvv-':264,					# ramaNam
				'vvvvvvvvvvv':264,					# ramaNam
				'vvvvvv-vv--':332,					# SubhajAtham
				'vvvvvv-vv-v':332,					# SubhajAtham
				'-vvvv-vvvv-':108,					# guru
				'-vvvv-vvvvv':108,					# guru
				'vv-vv-vvvv-':153,					# dharaNi
				'vv-vv-vvvvv':153,					# dharaNi
				'vvvv-vvvv--':129,					# jaladharaneelam
				'vvvv-vvvv-v':129,					# jaladharaneelam
				'vv-v-vvvvv-':331,					# Subhacharitham
				'vv-v-vvvvvv':331,					# Subhacharitham
				'v-v--vv-v-v-':316,					# vamSasthham
				'v-v--vv-v-vv':316,					# vamSasthham
				'--v--vv-v-v-':38,					# indravamSa
				'--v--vv-v-vv':38,					# indravamSa
				'vvv-vv-vv-v-':152,					# druthaviLambitham
				'vvv-vv-vv-vv':152,					# druthaviLambitham
				'vv-v-vvv-vv-':193,					# pramithAkshara
				'vv-v-vvv-vvv':193,					# pramithAkshara
				'vv-vv-vv-vv-':141,					# thOTakam
				'vv-vv-vv-vvv':141,					# thOTakam
				'v--v--v--v--':209,					# bhujamgaprayAtham
				'v--v--v--v-v':209,					# bhujamgaprayAtham
				'v-vv-vv-vv-v':256,					# maukthikadAma
				'v-vv-vv-vv--':256,					# maukthikadAma
				'-v--v--v--v-':375,					# sragviNi
				'-v--v--v--vv':375,					# sragviNi
				'------v--v--':313,					# vaiSvadEvi
				'------v--v-v':313,					# vaiSvadEvi
				'--vv----vv--':225,					# maNimAla
				'--vv----vv-v':225,					# maNimAla
				'vvvvvv-v--v-':188,					# prabha
				'vvvvvv-v--vv':188,					# prabha
				'vvvv--vvvv--':91,					# kusumavichithra
				'vvvv--vvvv-v':91,					# kusumavichithra
				'v-vvv-v-vvv-':131,					# jalOddhathagathi
				'v-vvv-v-vvvv':131,					# jalOddhathagathi
				'vvvvvv---v--':181,					# puTam
				'vvvvvv---v-v':181,					# puTam
				'vvv-vvv-v-v-':199,					# priyamvada
				'vvv-vvv-v-vv':199,					# priyamvada
				'--v-vvv-v-v-':280,					# laLitha
				'--v-vvv-v-vv':280,					# laLitha
				'----vvvv----':130,					# jaladharamAla
				'----vvvv---v':130,					# jaladharamAla
				'vvvv-v-vvv--':160,					# navamAlika
				'vvvv-v-vvv-v':160,					# navamAlika
				'vvvv-vv-v-v-':249,					# mAnini
				'vvvv-vv-v-vv':249,					# mAnini
				'v-v-vvv-v-v-':365,					# sumamgala
				'v-v-vvv-v-vv':365,					# sumamgala
				'vvvv-vv-vv--':282,					# laLithapadam
				'vvvv-vv-vv-v':282,					# laLithapadam
				'-v-vvv-vvvv-':117,					# chandravar_thma
				'-v-vvv-vvvvv':117,					# chandravar_thma
				'vvvvvv-vv-v-':39,					# ujjvala
				'vvvvvv-vv-vv':39,					# ujjvala
				'-vv---vv-vv-':276,					# lalana
				'-vv---vv-vvv':276,					# lalana
				'vvv-vvvvvv--':150,					# druthapadam
				'vvv-vvvvvv-v':150,					# druthapadam
				'vvv-vvv-vv--':149,					# druthagathi
				'vvv-vvv-vv-v':149,					# druthagathi
				'-vvvv-vvvv--':64,					# kanya
				'-vvvv-vvvv-v':64,					# kanya
				'vv-v--vv-v--':96,					# kOkaratham
				'vv-v--vv-v-v':96,					# kOkaratham
				'-vv--vvvvvv-':364,					# subhaga
				'-vv--vvvvvvv':364,					# subhaga
				'vvvvvv----v-':281,					# laLitham
				'vvvvvv----vv':281,					# laLitham
				'vvvvvv-vv---':133,					# jvAla
				'vvvvvv-vv--v':133,					# jvAla
				'-vv-vvvvvv--':40,					# ujjvalam
				'-vv-vvvvvv-v':40,					# ujjvalam
				'-vvvv-v-vvv-':363,					# sudathi
				'-vvvv-v-vvvv':363,					# sudathi
				'vvvv-vvvvvv-':4,					# athiruchiram
				'vvvv-vvvvvvv':4,					# athiruchiram
				'vvv-v-vvv-v-':362,					# sukhAvaham
				'vvv-v-vvv-vv':362,					# sukhAvaham
				'---vvvv-v-v--':197,				# prahar_shiNi
				'---vvvv-v-v-v':197,				# prahar_shiNi
				'vv-v-vvv-v-v-':217,				# manjubhAshiNi
				'vv-v-vvv-v-vv':217,				# manjubhAshiNi
				'v-v-vvvv-v-v-':3,					# athiruchira
				'v-v-vvvv-v-vv':3,					# athiruchira
				'vvvvvv--v--v-':99,					# kshama
				'vvvvvv--v--vv':99,					# kshama
				'-----vv--vv--':228,				# maththamayooram
				'-----vv--vv-v':228,				# maththamayooram
				'v------v--v--':111,				# chanchareekAvali
				'v------v--v-v':111,				# chanchareekAvali
				'vvvvv--v--v--':115,				# chandralEkha
				'vvvvv--v--v-v':115,				# chandralEkha
				'vvvvvv--v--v-':300,				# vidyuthth
				'vvvvvv--v--vv':300,				# vidyuthth
				'vvv--v--v--v-':58,					# ur_vaSi
				'vvv--v--v--vv':58,					# ur_vaSi
				'vv-v-vvv-vv--':346,				# sarasa
				'vv-v-vvv-vv-v':346,				# sarasa
				'v-v--vvv-v-v-':227,				# maththakASini
				'v-v--vvv-v-vv':227,				# maththakASini
				'vvvv-vvv-v-v-':189,				# prabhadrakam
				'vvvv-vvv-v-vv':189,				# prabhadrakam
				'v--v-vvv-vv--':154,				# dharAnandini
				'v--v-vvv-vv-v':154,				# dharAnandini
				'vvvvvvvvvvvv-':0,					# aghaharaNam
				'vvvvvvvvvvvvv':0,					# aghaharaNam
				'vvvvvvvvvv---':159,				# navathAruNyam
				'vvvvvvvvvv--v':159,				# navathAruNyam
				'vvvv-vvvvvv--':284,				# laLithaSareeram
				'vvvv-vvvvvv-v':284,				# laLithaSareeram
				'vvvvvv-vv-vv-':265,				# ramaNam
				'vvvvvv-vv-vvv':265,				# ramaNam
				'-vvvv-vvvvvv-':263,				# rajani
				'-vvvv-vvvvvvv':263,				# rajani
				'vv-vvvv-vvvv-':146,				# dooshaNaharaNam
				'vv-vvvv-vvvvv':146,				# dooshaNaharaNam
				'vv--vvvvvv-vv':293,				# vasudha
				'vv--vvvvvv-v-':293,				# vasudha
				'vv-vv-vvvv-vv':21,					# avani
				'vv-vv-vvvv-v-':21,					# avani
				'vvvvvv--vvvv-':259,				# mamgaLaphalakam
				'vvvvvv--vvvvv':259,				# mamgaLaphalakam
				'--v-vvv-vv-v--':292,				# vasanthathilakam
				'--v-vvv-vv-v-v':292,				# vasanthathilakam
				'-vvv-vvv-vvv--':36,				# induvadana
				'-vvv-vvv-vvv-v':36,				# induvadana
				'vvvv-v-vvv-vv-':191,				# pramada
				'vvvv-v-vvv-vvv':191,				# pramada
				'vvv-v-vvv-v-v-':360,				# sukEsaram
				'vvv-v-vvv-v-vv':360,				# sukEsaram
				'-----vvvvvv---':28,				# asambAdha
				'-----vvvvvv--v':28,				# asambAdha
				'vvvvvv-v-vv-v-':14,				# aparAjitha
				'vvvvvv-v-vv-vv':14,				# aparAjitha
				'---vv-----vv--':20,				# alOla
				'---vv-----vv-v':20,				# alOla
				'vvvvvv-vvvvvv-':196,				# praharaNathilakam
				'vvvvvv-vvvvvvv':196,				# praharaNathilakam
				'vvvv-v-vvv-v--':84,				# kumAri
				'vvvv-v-vvv-v-v':84,				# kumAri
				'vv-v-vvv-v--v-':169,				# paththhya
				'vv-v-vvv-v--vv':169,				# paththhya
				'--vv--vv--vv--':232,				# madanArththa
				'--vv--vv--vv-v':232,				# madanArththa
				'-vvvvvvvvvvvv-':103,				# giriSikharam
				'-vvvvvvvvvvvvv':103,				# giriSikharam
				'vvvv-vvvvvv-vv':347,				# sarOruham
				'vvvv-vvvvvv-v-':347,				# sarOruham
				'vvvvvv-vvvv-vv':69,				# kamalAkaram
				'vvvvvv-vvvv-v-':69,				# kamalAkaram
				'vv-vvvvvvvvvv-':72,				# karuNAkaram
				'vv-vvvvvvvvvvv':72,				# karuNAkaram
				'vvvv-vvvvvvvv-':289,				# valajam
				'vvvv-vvvvvvvvv':289,				# valajam
				'vv-vvvv-vvvvvv':330,				# Subhagathi
				'vv-vvvv-vvvvv-':330,				# Subhagathi
				'vvvvvv---v--v--':251,				# mAlini
				'vvvvvv---v--v-v':251,				# mAlini
				'vvvvvv--v-vv-v-':52,				# upamAlini
				'vvvvvv--v-vv-vv':52,				# upamAlini
				'vvvvvvvvvvvvvv-':320,				# SaSikala
				'vvvvvvvvvvvvvvv':320,				# SaSikala
				'---------------':81,				# kAmakreeDa
				'--------------v':81,				# kAmakreeDa
				'vvvv-v-vvv-v-v-':190,				# prabhadrakam
				'vvvv-v-vvv-v-vv':190,				# prabhadrakam
				'vv-v-vvvvvvvv--':61,				# Ela
				'vv-v-vvvvvvvv-v':61,				# Ela
				'----v----v--v--':116,				# chandralEkha
				'----v----v--v-v':116,				# chandralEkha
				'-v--v--v--v--v-':114,				# chandrarEkha
				'-v--v--v--v--vv':114,				# chandrarEkha
				'vv-v-vvvvvvvvv-':144,				# daLam
				'vv-v-vvvvvvvvvv':144,				# daLam
				'vvvv--vvvv-----':351,				# samsAram
				'vvvv--vvvv----v':351,				# samsAram
				'----vvvv--vvvv-':341,				# sakalakalam
				'----vvvv--vvvvv':341,				# sakalakalam
				'-----vvvv-vvvv-':353,				# sArasakalika
				'-----vvvv-vvvvv':353,				# sArasakalika
				'vv---vvvv--vv--':243,				# marathakaneelam
				'vv---vvvv--vv-v':243,				# marathakaneelam
				'v-v-v-v-v-v-v-v-':168,				# panchachAmaram
				'v-v-v-v-v-v-v-vv':168,				# panchachAmaram
				'-vv-vv-vv-vv-vv-':25,				# aSvagathi
				'-vv-vv-vv-vv-vvv':25,				# aSvagathi
				'-vv-v-vvv-vv-vv-':333,				# SailaSikha
				'-vv-v-vvv-vv-vvv':333,				# SailaSikha
				'-v--v--v--v--v--':126,				# chhAndasi
				'-v--v--v--v--v-v':126,				# chhAndasi
				'-vv-v-vvv-v-vvv-':155,				# dheeralaLitha
				'-vv-v-vvv-v-vvvv':155,				# dheeralaLitha
				'vvvv-v-vvv-v-v--':296,				# vANini
				'vvvv-v-vvv-v-v-v':296,				# vANini
				'vvvvvvvvvvvvvvv-':177,				# parimaLam
				'vvvvvvvvvvvvvvvv':177,				# parimaLam
				'----vvvvvv-vvvv-':274,				# ruchiratharam
				'----vvvvvv-vvvvv':274,				# ruchiratharam
				'vvvvvv--vvvv----':354,				# sArasanayana
				'vvvvvv--vvvv---v':354,				# sArasanayana
				'vvvv--vvvv--vv--':272,				# rasaramgam
				'vvvv--vvvv--vv-v':272,				# rasaramgam
				'-vvvv-vv-vv--vv-':172,				# pathralatha
				'-vvvv-vv-vv--vvv':172,				# pathralatha
				'vv-vv-vv-vv-vv--':67,	 			# kamaneeyam
				'vv-vv-vv-vv-vv-v':67,		 		# kamaneeyam
				'vv--vvvv--vvvv--':16,		 		# amala
				'vv--vvvv--vvvv-v':16,		 		# amala
				'vvvv-vv---vvvv--':104,				# girisAram
				'vvvv-vv---vvvv-v':104,				# girisAram
				'--v--v--vvv---v-':6,				# athimuditham
				'--v--v--vvv---vv':6,				# athimuditham
				'v-----vvvvv--vvv-':324,			# SikhariNi
				'v-----vvvvv--vvvv':324,			# SikhariNi
				'v-vvv-v-vvv-v--v-':185,			# pr^ththhvi
				'v-vvv-v-vvv-v--vv':185,			# pr^ththhvi
				'----vvvvv--v--v--':241,			# mandAkrAntha
				'----vvvvv--v--v-v':241,			# mandAkrAntha
				'vvvvv-----v-vv-v-':382,			# hariNi
				'vvvvv-----v-vv-vv':382,			# hariNi
				'-vv-v-vvv-vvvvvv-':314,			# vamSapathrapathitham
				'-vv-v-vvv-vvvvvvv':314,			# vamSapathrapathitham
				'vvvv-v-vvv-vv-vv-':158,			# nar_kkuTakam
				'vvvv-v-vvv-vv-vvv':158,			# nar_kkuTakam
				'vvvvvv----v-vv-v-':379,			# hari
				'vvvvvv----v-vv-vv':379,			# hari
				'v---vvvvv-v-vv-v-':80,				# kAntha
				'v---vvvvv-v-vv-vv':80,				# kAntha
				'vvvv-vvv--vvv-v--':124,			# chithralEkha
				'vvvv-vvv--vvv-v-v':124,			# chithralEkha
				'vvvvvvvvvvvvvvv--':221,			# maNideepam
				'vvvvvvvvvvvvvvv-v':221,			# maNideepam
				'-vvvv-vvvvvv-vv--':176,			# pariNAmam
				'-vvvv-vvvvvv-vv-v':176,			# pariNAmam
				'vvvvvv-vvvvvv----':267,			# ramaNi
				'vvvvvv-vvvvvv---v':267,			# ramaNi
				'vvvvvv--vvvv-vv--':368,			# sulalAmam
				'vvvvvv--vvvv-vv-v':368,			# sulalAmam
				'vv-vv-vvvv-vvvv--':127,			# jagatheethilakam
				'vv-vv-vvvv-vvvv-v':127,			# jagatheethilakam
				'vvvv-vvvv-vv-vv--':370,			# suSareeram
				'vvvv-vvvv-vv-vv-v':370,			# suSareeram
				'vvvv-vvvvvv--vv--':106,			# guNajAlam
				'vvvv-vvvvvv--vv-v':106,			# guNajAlam
				'vv-vv-vvvv--vvvv-':182,			# puLakam
				'vv-vv-vvvv--vvvvv':182,			# puLakam
				'vvvvvv-vvvv--vv--':233,			# madaneeyam
				'vvvvvv-vvvv--vv-v':233,			# madaneeyam
				'vv--vv--vv--vvvv-':336,			# SravaNeeyam
				'vv--vv--vv--vvvvv':336,			# SravaNeeyam
				'-v-vv-v-vv-v-vv-v-':244,			# mallika
				'-v-vv-v-vv-v-vv-vv':244,			# mallika
				'-vvvv-vvvv-vvvvvv-':266,			# ramaNam
				'-vvvv-vvvv-vvvvvvv':266,			# ramaNam
				'-v-vvvv-vv---vv-v-':378,			# haranar_ththanam
				'-v-vvvv-vv---vv-vv':378,			# haranar_ththanam
				'-vv-vvvvvvvv-vvvv-':205,			# bhavatharaNam
				'-vv-vvvvvvvv-vvvvv':205,			# bhavatharaNam
				'-vv-vvvvvv-vvvvvv-':71,			# karakamalam
				'-vv-vvvvvv-vvvvvvv':71,			# karakamalam
				'-vvvv-vvvvvv-vvvv-':359,			# sukr^tham
				'-vvvv-vvvvvv-vvvvv':359,			# sukr^tham
				'vv-vvvv-vvvv-vvvv-':318,			# Sankaracharitham
				'vv-vvvv-vvvv-vvvvv':318,			# Sankaracharitham
				'vv-vvvvvvvvvv--vv-':339,			# Sreesadanam
				'vv-vvvvvvvvvv--vvv':339,			# Sreesadanam
				'-----vvvvv--v--v--':90,			# kusumithalathAvEllitha
				'-----vvvvv--v--v-v':90,			# kusumithalathAvEllitha
				'vvvvvv-v--v--v--v-':19,			# alasa
				'vvvvvv-v--v--v--vv':19,			# alasa
				'-------vv---v--v--':356,			# simhavishphoor_jjitham
				'-------vv---v--v-v':356,			# simhavishphoor_jjitham
				'---vv-v-vvvv-vv-v-':381,			# hariNaplutham
				'---vv-v-vvvv-vv-vv':381,			# hariNaplutham
				'vvvvvv-v--v--v--v-':246,			# mahAmAlika
				'vvvvvv-v--v--v--vv':246,			# mahAmAlika
				'-vv-vv-vv-vv-vvvv-':26,			# aSvagathi
				'-vv-vv-vv-vv-vvvvv':26,			# aSvagathi
				'---vv-v-vvv---v--v-':322,			# SArddoolavikreeDitham
				'---vv-v-vvv---v--vv':322,			# SArddoolavikreeDitham
				'v-----vvvvv--v--v--':255,			# mEghavishphoor_jjitham
				'v-----vvvvv--v--v-v':255,			# mEghavishphoor_jjitham
				'v-----vvvvv-v-vv-v-':213,			# makarandika
				'v-----vvvvv-v-vv-vv':213,			# makarandika
				'vvv-vv-v-vv-v-vv-v-':212,			# bhramarAvali
				'vvv-vv-v-vv-v-vv-vv':212,			# bhramarAvali
				'---vv-vv---vv-vv---':222,			# maNideepthi
				'---vv-vv---vv-vv--v':222,			# maNideepthi
				'----vvvv-vvvv--vv--':295,			# vANi
				'----vvvv-vvvv--vv-v':295,			# vANi
				'vvvvvv-vvvvvv-vvvv-':187,			# prathhamapadam
				'vvvvvv-vvvvvv-vvvvv':187,			# prathhamapadam
				'-vv--vv---vvvv-vv--':70,			# kamalAksham
				'-vv--vv---vvvv-vv-v':70,			# kamalAksham
				'vvvv-vvvvvv-vvvvvv-':17,			# amalatharam
				'vvvv-vvvvvv-vvvvvvv':17,			# amalatharam
				'vvvv-vvvvvvvv-vvvv-':88,			# kuvalini
				'vvvv-vvvvvvvv-vvvvv':88,			# kuvalini
				'vv-vvvvvvvvvvvvvv--':87,			# kulapAlam
				'vv-vvvvvvvvvvvvvv-v':87,			# kulapAlam
				'vvvvvvvvvv-vvvvvv--':361,			# sukhakaram
				'vvvvvvvvvv-vvvvvv-v':361,			# sukhakaram
				'vvvvvv-vv-vvvvvvvv-':156,			# dhr^thakuthukam
				'vvvvvv-vv-vvvvvvvvv':156,			# dhr^thakuthukam
				'-v-v-v-v-v-v-v-v-v--':309,			# vr^ththam
				'-v-v-v-v-v-v-v-v-v-v':309,			# vr^ththam
				'----v--vvvvvv---vvv-':369,			# suvadana
				'----v--vvvvvv---vvvv':369,			# suvadana
				'-vv-v-vvv-vv-vv-v-v-':41,			# uthpalamAlika
				'-vv-v-vvv-vv-vv-v-vv':41,			# uthpalamAlika
				'----vv-v-vvv---v--v-':231,			# maththEbhavikreeDitham
				'----vv-v-vvv---v--vv':231,			# maththEbhavikreeDitham
				'vvvv-vv-vvvvvvvvvv--':180,			# pAthram
				'vvvv-vv-vvvvvvvvvv-v':180,			# pAthram
				'vvvv--vv---vvvv-vv--':82,			# kAreeram
				'vvvv--vv---vvvv-vv-v':82,			# kAreeram
				'vvvvvvvvvvvvvv-vvvv-':239,			# madhuratharam
				'vvvvvvvvvvvvvv-vvvvv':239,			# madhuratharam
				'vv--vvvv--vvvv--vv--':287,			# vanamAlam
				'vv--vvvv--vvvv--vv-v':287,			# vanamAlam
				'vvvv-vv-vvvvvvvvvv--':206,			# bhavasAram
				'vvvv-vv-vvvvvvvvvv-v':206,			# bhavasAram
				'vvvv-----vvvvvv-vv--':101,			# gamga
				'vvvv-----vvvvvv-vv-v':101,			# gamga
				'vvvv---vv--vvvv-vv--':271,			# rasapAthram
				'vvvv---vv--vvvv-vv-v':271,			# rasapAthram
				'----v--vvvvvv--v--v--':374,		# sragddhara
				'----v--vvvvvv--v--v-v':374,		# sragddhara
				'-v-vvv-v-vvv-v-vvv-v-':89,			# kusumamanjjari
				'-v-vvv-v-vvv-v-vvv-vv':89,			# kusumamanjjari
				'vvvv-v-vvv-vv-vv-v-v-':350,		# salilanidhi
				'vvvv-v-vvv-vv-vv-v-vv':350,		# salilanidhi
				'vv-v-vvv-v-vvv-v-vvv-':134,		# thaTini
				'vv-v-vvv-v-vvv-v-vvvv':134,		# thaTini
				'vvvvvvvvvvvvvvvvvvvv-':5,			# athiruchiram
				'vvvvvvvvvvvvvvvvvvvvv':5,			# athiruchiram
				'vvv-vvvvv-vvvvv-vv-v-':85,			# kumudini
				'vvv-vvvvv-vvvvv-vv-vv':85,			# kumudini
				'--vvvvvvvv--vvvv-vv--':321,		# SaSikala
				'--vvvvvvvv--vvvv-vv-v':321,		# SaSikala
				'vvvv--vvvv--vvvv-vv--':78,			# kaLathram
				'vvvv--vvvv--vvvv-vv-v':78,			# kaLathram
				'vv--vv-vvvv-vv-vvvv--':9,			# anapAyam
				'vv--vv-vvvv-vv-vvvv-v':9,			# anapAyam
				'vv-vvvvv-vvvv-vvvvvv-':270,		# raviradanam
				'vv-vvvvv-vvvv-vvvvvvv':270,		# raviradanam
				'vvvv-vv--vvvv--vvvv--':277,		# lalAmam
				'vvvv-vv--vvvv--vvvv-v':277,		# lalAmam
				'--v-vvv--v-vvv--v-vvv-':230,		# maththEbham
				'--v-vvv--v-vvv--v-vvvv':230,		# maththEbham
				'-vv-v-vvv-v-vvv-v-vvv-':202,		# bhadrakam
				'-vv-v-vvv-v-vvv-v-vvvv':202,		# bhadrakam
				'-vv-vv-vv-vv-vv-vv-vv-':236,		# madira
				'-vv-vv-vv-vv-vv-vv-vvv':236,		# madira
				'vvv-v-vvv-v-vvv-v-vvv-':138,		# tharamgiNi
				'vvv-v-vvv-v-vvv-v-vvvv':138,		# tharamgiNi
				'vvvv--vv--vvvvvvvvvv--':275,		# lakshmi
				'vvvv--vv--vvvvvvvvvv-v':275,		# lakshmi
				'vvvv-vvvvvv-vvvvvv----':68,		# kamaladivAkaram
				'vvvv-vvvvvv-vvvvvv---v':68,		# kamaladivAkaram
				'vvvv-v-vvv-v-vvv-v-vvv-':27,		# aSvalaLitham
				'vvvv-v-vvv-v-vvv-v-vvvv':27,		# aSvalaLitham
				'--------vvvvvvvvvvvvvv-':229,		# maththAkreeDa
				'--------vvvvvvvvvvvvvvv':229,		# maththAkreeDa
				'vvvv-v-vvv-v-vvv-v-vvv-':218,		# manjjuLa
				'vvvv-v-vvv-v-vvv-v-vvvv':218,		# manjjuLa
				'-vv-vv-vv-vv-vv-vv-vv--':348,		# sarOjasamam
				'-vv-vv-vv-vv-vv-vv-vv-v':348,		# sarOjasamam
				'vvvv-vvvvvv-vvvvvv-vv--':220,		# maNighr^Ni
				'vvvv-vvvvvv-vvvvvv-vv-v':220,		# maNighr^Ni
				'-vv--vvvvvv--vv-vvvvvv--':136,		# thanvi
				'-vv--vvvvvv--vv-vvvvvv-v':136,		# thanvi
				'vvvvvvvvvvvv-v--v--v--v-':306,		# vilAsini
				'vvvvvvvvvvvv-v--v--v--vv':306,		# vilAsini
				'vvvv-v-vvvv-v-vvv-v-vvv-':283,		# laLitham
				'vvvv-v-vvvv-v-vvv-v-vvvv':283,		# laLitham
				'-vv---vv--vvvvvvvvvvvv--':98,		# kraunchapadam
				'-vv---vv--vvvvvvvvvvvv-v':98,		# kraunchapadam
				'vvvvvv-vv---vv-vvvvvvvv-':237,		# madhukarakaLabham
				'vvvvvv-vv---vv-vvvvvvvvv':237,		# madhukarakaLabham
				'vv--vv-vvvv-vvvv-vvvvvv-':107,		# guNasadanam
				'vv--vv-vvvv-vvvv-vvvvvvv':107,		# guNasadanam
				'-vv---vv--vvvvvvvvvvvvvv-':97,		# kraunchapada
				'-vv---vv--vvvvvvvvvvvvvvv':97,		# kraunchapada
				'-v-vv-v-vv-vv-vv-vv-vv-v-':86,		# kumudvathi
				'-v-vv-v-vv-vv-vv-vv-vv-vv':86,		# kumudvathi
				'vvvvvv-vvvv-vv-vvvv-vvvv-':223,	# maNimakuTam
				'vvvvvv-vvvv-vv-vvvv-vvvvv':223,	# maNimakuTam
				'-vvvvvv-vv-vvvvvv--vvvv--':319,	# SaSadharabimbam
				'-vvvvvv-vv-vvvvvv--vvvv-v':319,	# SaSadharabimbam
				'--------vvvvvvvvvv-v-vv-v-':210,	# bhujamgavijr^mbhitham
				'--------vvvvvvvvvv-v-vv-vv':210,	# bhujamgavijr^mbhitham
				'v-vvv-vvv-vvv-vvv-vvv-vvv-':334,	# SambhunaTanam
				'v-vvv-vvv-vvv-vvv-vvv-vvvv':334,	# SambhunaTanam
				'vvvv-vvvvvvvv--vv-vvvvvv--':73,	# karambham
				'vvvv-vvvvvvvv--vv-vvvvvv-v':73,	# karambham
				'-vv-vv-vv-vv-vv-vv-vv-vv--':113,	# chandanasAram
				'-vv-vv-vv-vv-vv-vv-vv-vv-v':113,	# chandanasAram
				'-v-v-v-v-v-v-v-v-v-v-v-vv-':65,	# kanyakAmaNi
				'-v-v-v-v-v-v-v-v-v-v-v-vvv':65		# kanyakAmaNi
				}

avGanamDict = {	'vv-vv-v-v-':386,					# sasajaga
				'vv-vv-v-vv':386,					# sasajaga
				'vv--vv-v-v-':387,					# sabharalaga
				'vv--vv-v-vv':387,					# sabharalaga
				'vv-vv-v-v--':388,					# sasajagaga
				'vv-vv-v-v-v':388,					# sasajagaga
				'vv--vv-v-v--':389,					# sabharaya
				'vv--vv-v-v-v':389,					# sabharaya
				'vvvvvv-v-v--':390,					# nanaraya
				'vvvvvv-v-v-v':390,					# nanaraya
				'vvvv-vv-v-v--':391,				# najajaraga
				'vvvv-vv-v-v-v':391,				# najajaraga
				'vv-vv-vv-v-':392,					# sasasalaga
				'vv-vv-vv-vv':392,					# sasasalaga
				'vvv-vv-vv-v-':393,					# nabhabhara
				'vvv-vv-vv-vv':393,					# nabhabhara
				'vvvvvv-v-v-':394,					# nanaralaga
				'vvvvvv-v-vv':394,					# nanaralaga
				'vvvv-vv-v-v-':395,					# najajara
				'vvvv-vv-v-vv':395,					# najajara
				'-v-v-v-v-v-v':396,					# rajaraja
				'-v-v-v-v-v--':396,					# rajaraja
				'v-v-v-v-v-v--':397,				# jarajaraga
				'v-v-v-v-v-v-v':397,				# jarajaraga
				'-vv-vv-vv--':398,					# bhabhabhagaga
				'-vv-vv-vv-v':398,					# bhabhabhagaga
				'vvvv-vv-vv--':399,					# najajaya
				'vvvv-vv-vv-v':399,					# najajaya
				'vv-vv-vv--':400,					# sasasaga
				'vv-vv-vv-v':400,					# sasasaga
				'--vv-v-v--':401,					# thajaraga
				'--vv-v-v-v':401,					# thajaraga
				'---vv-v-v--':402,					# masajagaga
				'---vv-v-v-v':402,					# masajagaga
				'vv-v-vvv--':403,					# sajasaga
				'vv-v-vvv-v':403,					# sajasaga
				'-vv-v-vvv--':404,					# bharanagaga
				'-vv-v-vvv-v':404,					# bharanagaga
				'vv-v-vvv-v':405,					# sajasala
				'vv-v-vvv--':405,					# sajasala
				'vvvvv-v-v-':406,					# nasajaga
				'vvvvv-v-vv':406,					# nasajaga
				'-vvvvvv-vv-':407,					# bhanajalaga
				'-vvvvvv-vvv':407,					# bhanajalaga
				'vv-v-vvv-v-v-':408,				# sajasajaga
				'vv-v-vvv-v-vv':408,				# sajasajaga
				'-v-vvv-vv-':409,					# ranabhaga
				'-v-vvv-vvv':409,					# ranabhaga
				'vvvvvvvv-vv-':410,					# nanasasa
				'vvvvvvvv-vvv':410,					# nanasasa
				'--v--vv-v--':37,					# indravajra
				'--v--vv-v-v':37,					# indravajra
				'v-v--vv-v--':57,					# upEndravajra
				'v-v--vv-v-v':57,					# upEndravajra
				'v-v--vv-v-v-':316,					# vamSasthham
				'v-v--vv-v-vv':316,					# vamSasthham
				'--v--vv-v-v-':38,					# indravamSa
				'--v--vv-v-vv':38					# indravamSa
				}

ardhaVishamaVruthamDict = { '37-57-':49,			# upajAthi
							'57-37-':49,			# upajAthi
							'37-37-37-57-':49,		# upajAthi
							'37-37-57-37-':49,		# upajAthi
							'37-37-57-57-':49,		# upajAthi
							'37-57-37-37-':49,		# upajAthi
							'37-57-37-57-':29,		# AkhyAnaki
							'37-57-57-37-':49,		# upajAthi
							'37-57-57-57-':49,		# upajAthi
							'57-37-37-37-':49,		# upajAthi
							'57-37-37-57-':49,		# upajAthi
							'57-37-57-37-':303,		# vipareethAkhyAnaki
							'57-37-57-57-':49,		# upajAthi
							'57-57-37-37-':49,		# upajAthi
							'57-57-37-57-':49,		# upajAthi
							'57-57-57-37-':49,		# upajAthi
							'38-316-':50,			# upajAthi
							'316-38-':50,			# upajAthi
							'38-38-38-316-':50,		# upajAthi
							'38-38-316-38-':50,		# upajAthi
							'38-38-316-316-':50,	# upajAthi
							'38-316-38-38-':50,		# upajAthi
							'38-316-38-316-':50,	# upajAthi
							'38-316-316-38-':50,	# upajAthi
							'38-316-316-316-':50,	# upajAthi
							'316-38-38-38-':50,		# upajAthi
							'316-38-38-316-':50,	# upajAthi
							'316-38-316-38-':50,	# upajAthi
							'316-38-316-316-':50,	# upajAthi
							'316-316-38-38-':50,	# upajAthi
							'316-316-38-316-':50,	# upajAthi
							'316-316-316-38-':50,	# upajAthi
							'386-387-':305,			# viyOgini
							'386-387-386-387-':305,	# viyOgini
							'388-389-':290,			# vasanthamAlika
							'388-389-388-389-':290,	# vasanthamAlika
							'390-391-':183,			# pushpithAgra
							'390-391-390-391-':183,	# pushpithAgra
							'392-393-':380,			# hariNaplutha
							'392-393-392-393-':380,	# hariNaplutha
							'394-395-':13,			# aparavakthram
							'394-395-394-395-':13,	# aparavakthram
							'396-397-':175,			# parAvathi
							'396-397-396-397-':175,	# parAvathi
							'392-398-':47,			# upachithram
							'392-398-392-398-':47,	# upachithram
							'398-399-':151,			# druthamaddhya
							'398-399-398-399-':151,	# druthamaddhya
							'400-398-':310,			# vEgavathi
							'400-398-400-398-':310,	# vEgavathi
							'401-402-':203,			# bhadravirAL
							'401-402-401-402-':203,	# bhadravirAL
							'403-404-':94,			# kEthumathi
							'403-404-403-404-':94,	# kEthumathi
							'405-404-':94,			# kEthumathi
							'405-404-405-404-':94,	# kEthumathi
							'405-406-407-408-':43,	# udgatha
							'403-406-407-408-':43,	# udgatha
							'405-406-409-408-':372,	# saurabham
							'403-406-409-408-':372,	# saurabham
							'405-406-410-408-':279,	# laLitha
							'403-406-410-408-':279	# laLitha
							}

yathiDict = {	301:(-1, 4),						# vidyunmAla
				323:(-1, 4),						# SAlini
				297:(-1, 4),						# vAthOrmi
				313:(-1, 5),						# vaiSvadEvi
				225:(-1, 6),						# manimAla
				188:(-1, 7),						# prabha
				194:(-1, 7),						# pramudithavadana (prabha)
				110:(-1, 7),						# gauri (prabha)
				181:(-1, 7),						# puTam
				130:(-1, 4),						# jaladharamAla
				249:(-1, 5),						# mAnini
				117:(-1, 4),						# chandravar_thma
				276:(-1, 5),						# lalana
				364:(-1, 5),						# subhaga
				197:(-1, 3),						# prahar_shiNi
				3:(-1, 4),							# athiruchira
				99:(-1, 7),							# kshama
				228:(-1, 4),						# maththamayooram
				115:(-1, 6),						# chandralEkha
				300:(-1, 6),						# vidyuthth
				28:(-1, 5),							# asambAdha
				14:(-1, 7),							# aparAjitha
				20:(-1, 7),							# alOla
				84:(-1, 8),							# kumAri
				169:(-1, 5),						# paththhya
				214:(-1, 5),						# manjjari (paththhya)
				251:(-1, 8),						# mAlini
				52:(-1, 8),							# upamAlini
				61:(-1, 5),							# Ela
				116:(-1, 7),						# chandralEkha
				144:(-1, 5),						# daLam
				324:(-1, 6),						# SikhariNi
				185:(-1, 8),						# pr^ththhvi
				241:(-1, 4, 10),					# mandAkrAntha
				382:(-1, 6, 10),					# hariNi
				314:(-1, 10),						# vamSapathrapathitham
				158:(-1, 7),						# nar_kkuTakam
				379:(-1, 6, 10),					# hari
				80:(-1, 4, 10),						# kAntha
				124:(-1, 10),						# chithralEkha
				368:(-1, 7),						# sulalAmam
				378:(-1, 8, 13),					# haranar_ththanam
				90:(-1, 5, 11),						# kusumithalathAvEllitha
				19:(-1, 10),						# alasa
				145:(-1, 10),						# diSa (alasa)
				165:(-1, 10),						# niSa (alasa)
				356:(-1, 5, 11),					# simhavishphoor_jjitham
				381:(-1, 8, 13),					# hariNaplutham
				322:(-1, 12),						# SArddoolavikreeDitham
				255:(-1, 6, 12),					# mEghavishphoor_jjitham
				213:(-1, 6, 12),					# makarandika
				369:(-1, 7, 14),					# suvadana
				374:(-1, 7, 14),					# sragddhara
				202:(-1, 10),						# bhadrakam
				27:(-1, 11),						# aSvalaLitham
				229:(-1, 8, 15),					# maththAkreeDa
				136:(-1, 5, 17),					# thanvi
				283:(-1, 7, 18),					# laLitham
				98:(-1, 10, 18),					# kraunchapadam
				210:(-1, 8, 14, 20),				# bhujamgavijr^mbhitham
				}

similarVruthamDict = {	99:[99, 300],				# kshama
						300:[99, 300],				# vidyuthth
						19:[19, 246],				# alasa
						246:[19, 246],				# mahAmAlika
						27:[27, 218],				# aSvalaLitham
						218:[27, 218]				# manjjuLa
						}

vruthamTable = [[0, u'\u0d05\u0d18\u0d39\u0d30\u0d23\u0d02', 130, 'aghaharaNam', 'vvvvvvvvvvvv-', 13],
[1, u'\u0d05\u0d1a\u0d32\u0d27\u0d43\u0d24\u0d3f', 312, 'achaladhr^thi', '', 0],
[2, u'\u0d05\u0d1c\u0d17\u0d30\u0d17\u0d2e\u0d28\u0d02', 335, 'ajagaragamanam', '', 0],
[3, u'\u0d05\u0d24\u0d3f\u0d30\u0d41\u0d1a\u0d3f\u0d30', 119, 'athiruchira', 'v-v-vvvv-v-v-', 13],
[4, u'\u0d05\u0d24\u0d3f\u0d30\u0d41\u0d1a\u0d3f\u0d30\u0d02', 115, 'athiruchiram', 'vvvv-vvvvvv-', 12],
[5, u'\u0d05\u0d24\u0d3f\u0d30\u0d41\u0d1a\u0d3f\u0d30\u0d02', 245, 'athiruchiram', 'vvvvvvvvvvvvvvvvvvvv-', 21],
[6, u'\u0d05\u0d24\u0d3f\u0d2e\u0d41\u0d26\u0d3f\u0d24\u0d02', 183, 'athimuditham', '--v--v--vvv---v-', 16],
[7, u'\u0d05\u0d24\u0d3f\u0d38\u0d2e\u0d4d\u0d2e\u0d24', 344, '', '', 0],
[8, u'\u0d05\u0d24\u0d3f\u0d38\u0d4d\u0d24\u0d3f\u0d2e\u0d3f\u0d24', 346, '', '', 0],
[9, u'\u0d05\u0d28\u0d2a\u0d3e\u0d2f\u0d02', 249, 'anapAyam', 'vv--vv-vvvv-vv-vvvv--', 21],
[10, u'\u0d05\u0d28\u0d41\u0d37\u0d4d\u0d1f\u0d41\u0d2a\u0d4d\u0d2a\u0d4d', 37, 'anushTupp', 'ANUSHTUP', 8],
[11, u'\u0d05\u0d28\u0d02\u0d17\u0d36\u0d47\u0d16\u0d30\u0d02', 301, '', '', 0],
[12, u'\u0d05\u0d28\u0d4d\u0d28\u0d28\u0d1f', 329, '', '', 0],
[13, u'\u0d05\u0d2a\u0d30\u0d35\u0d15\u0d4d\u0d24\u0d4d\u0d30\u0d02', 284, 'aparavakthram', 'AV|vvvvvv-v-v-|vvvv-vv-v-v-|vvvvvv-v-v-|vvvv-vv-v-v-', (11, 12)],
[14, u'\u0d05\u0d2a\u0d30\u0d3e\u0d1c\u0d3f\u0d24', 144, 'aparAjitha', 'vvvvvv-v-vv-v-', 14],
[15, u'\u0d05\u0d2a\u0d30\u0d3e\u0d28\u0d4d\u0d24\u0d3f\u0d15', 320, '', '', 0],
[16, u'\u0d05\u0d2e\u0d32', 181, 'amala', 'vv--vvvv--vvvv--', 16],
[17, u'\u0d05\u0d2e\u0d32\u0d24\u0d30\u0d02', 225, 'amalatharam', 'vvvv-vvvvvv-vvvvvv-', 19],
[18, u'\u0d05\u0d2e\u0d43\u0d24\u0d27\u0d3e\u0d30', 295, '', '', 0],
[19, u'\u0d05\u0d32\u0d38', 212, 'alasa', 'vvvvvv-v--v--v--v-', 18],
[20, u'\u0d05\u0d32\u0d4b\u0d32', 145, 'alOla', '---vv-----vv--', 14],
[21, u'\u0d05\u0d35\u0d28\u0d3f', 137, 'avani', 'vv-vv-vvvv-vv', 13],
[22, u'\u0d05\u0d30\u0d4d\u200d\u0d23\u0d02', 299, '', '', 0],
[23, u'\u0d05\u0d30\u0d4d\u200d\u0d23\u0d35\u0d02', 299, '', '', 0],
[24, u'\u0d05\u0d30\u0d4d\u200d\u0d26\u0d4d\u0d27\u0d15\u0d47\u0d15', 332, '', '', 0],
[25, u'\u0d05\u0d36\u0d4d\u0d35\u0d17\u0d24\u0d3f', 170, 'aSvagathi', '-vv-vv-vv-vv-vv-', 16],
[26, u'\u0d05\u0d36\u0d4d\u0d35\u0d17\u0d24\u0d3f', 216, 'aSvagathi', '-vv-vv-vv-vv-vvvv-', 18],
[27, u'\u0d05\u0d36\u0d4d\u0d35\u0d32\u0d33\u0d3f\u0d24\u0d02', 258, 'aSvalaLitham', 'vvvv-v-vvv-v-vvv-v-vvv-', 23],
[28, u'\u0d05\u0d38\u0d02\u0d2c\u0d3e\u0d27', 143, 'asambAdha', '-----vvvvvv---', 14],
[29, u'\u0d06\u0d16\u0d4d\u0d2f\u0d3e\u0d28\u0d15\u0d3f', 281, 'AkhyAnaki', 'AV|--v--vv-v--|v-v--vv-v--|--v--vv-v--|v-v--vv-v--', (11, 11)],
[30, u'\u0d06\u0d28\u0d41\u0d37\u0d4d\u0d1f\u0d41\u0d2d\u0d02', 36, '', '', 8],
[31, u'\u0d06\u0d2a\u0d3e\u0d24\u0d3e\u0d33\u0d3f\u0d15', 315, '', '', 0],
[32, u'\u0d06\u0d2a\u0d40\u0d21\u0d02', 295, '', '', 0],
[33, u'\u0d06\u0d30\u0d4d\u0d2f', 306, '', '', 0],
[34, u'\u0d06\u0d30\u0d4d\u0d2f\u0d3e\u0d17\u0d40\u0d24\u0d3f', 311, '', '', 0],
[35, u'\u0d07\u0d15\u0d4d\u0d37\u0d41\u0d26\u0d23\u0d4d\u0d21\u0d3f\u0d15', 303, '', '', 0],
[36, u'\u0d07\u0d28\u0d4d\u0d26\u0d41\u0d35\u0d26\u0d28', 140, 'induvadana', '-vvv-vvv-vvv--', 14],
[37, u'\u0d07\u0d28\u0d4d\u0d26\u0d4d\u0d30\u0d35\u0d1c\u0d4d\u0d30', 51, 'indravajra', '--v--vv-v--', 11],
[38, u'\u0d07\u0d28\u0d4d\u0d26\u0d4d\u0d30\u0d35\u0d02\u0d36', 83, 'indravamSa', '--v--vv-v-v-', 12],
[39, u'\u0d09\u0d1c\u0d4d\u0d1c\u0d4d\u0d35\u0d32', 104, 'ujjvala', 'vvvvvv-vv-v-', 12],
[40, u'\u0d09\u0d1c\u0d4d\u0d1c\u0d4d\u0d35\u0d32\u0d02', 113, 'ujjvalam', '-vv-vvvvvv--', 12],
[41, u'\u0d09\u0d24\u0d4d\u0d2a\u0d32\u0d2e\u0d3e\u0d32\u0d3f\u0d15', 232, 'uthpalamAlika', '-vv-v-vvv-vv-vv-v-v-', 20],
[42, u'\u0d09\u0d26\u0d40\u0d1a\u0d4d\u0d2f\u0d35\u0d43\u0d24\u0d4d\u0d24\u0d3f', 317, '', '', 0],
[43, u'\u0d09\u0d26\u0d4d\u0d17\u0d24', 291, 'udgatha', 'AV|vv-v-vvv-v|vvvvv-v-v-|-vvvvvv-vv-|vv-v-vvv-v-v-', (10, 10, 11, 13)],
[44, u'\u0d09\u0d26\u0d4d\u0d17\u0d40\u0d24\u0d3f', 310, '', '', 0],
[45, u'\u0d09\u0d26\u0d4d\u0d27\u0d30\u0d4d\u200d\u0d37\u0d3f\u0d23\u0d3f (\u0d35\u0d38\u0d28\u0d4d\u0d24\u0d24\u0d3f\u0d32\u0d15\u0d02)', 139, 'uddhar_shiNi (vasanthathilakam)', '--v-vvv-vv-v--', 14],
[46, u'\u0d09\u0d2a\u0d17\u0d40\u0d24\u0d3f', 310, '', '', 0],
[47, u'\u0d09\u0d2a\u0d1a\u0d3f\u0d24\u0d4d\u0d30\u0d02', 286, 'upachithram', 'AV|vv-vv-vv-v-|-vv-vv-vv--|vv-vv-vv-v-|-vv-vv-vv--', (11, 11)],
[48, u'\u0d09\u0d2a\u0d1a\u0d3f\u0d24\u0d4d\u0d30\u0d02', 62, 'upachithram', 'vv-vv-vv-v-', 11],
[49, u'\u0d09\u0d2a\u0d1c\u0d3e\u0d24\u0d3f (\u0d07\u0d28\u0d4d\u0d26\u0d4d\u0d30\u0d35\u0d1c\u0d4d\u0d30/\u0d09\u0d2a\u0d47\u0d28\u0d4d\u0d26\u0d4d\u0d30\u0d35\u0d1c\u0d4d\u0d30)', 53, 'upajAthi (indravajra/upEndravajra)', 'AV|--v--vv-v--|--v--vv-v--|--v--vv-v--|--v--vv-v--', (11, 11)],
[50, u'\u0d09\u0d2a\u0d1c\u0d3e\u0d24\u0d3f (\u0d07\u0d28\u0d4d\u0d26\u0d4d\u0d30\u0d35\u0d02\u0d36/\u0d35\u0d02\u0d36\u0d38\u0d4d\u0d25\u0d02)', 54, 'upajAthi (indravamSa/vamSasthham)', 'AV|--v--vv-v-v-|--v--vv-v-v-|--v--vv-v-v-|--v--vv-v-v-', (12, 12)],
[51, u'\u0d09\u0d2a\u0d1c\u0d3e\u0d24\u0d3f', 83, 'upajAthi', 'AV', 12],		# Same as 50. Not being displayed
[52, u'\u0d09\u0d2a\u0d2e\u0d3e\u0d32\u0d3f\u0d28\u0d3f', 157, 'upamAlini', 'vvvvvv--v-vv-v-', 15],
[53, u'\u0d09\u0d2a\u0d38\u0d30\u0d4d\u200d\u0d2a\u0d4d\u0d2a\u0d3f\u0d23\u0d3f', 347, '', '', 0],
[54, u'\u0d09\u0d2a\u0d38\u0d4d\u0d25\u0d3f\u0d24', 69, 'upasthhitha', '--vv-vv-v--', 11],
[55, u'\u0d09\u0d2a\u0d38\u0d4d\u0d25\u0d3f\u0d24\u0d02', 74, 'upasthhitham', 'v-vvv---v--', 11],
[56, u'\u0d09\u0d2a\u0d38\u0d4d\u0d25\u0d3f\u0d24\u0d2a\u0d4d\u0d30\u0d1a\u0d41\u0d2a\u0d3f\u0d24', 296, '', '', 0],
[57, u'\u0d09\u0d2a\u0d47\u0d28\u0d4d\u0d26\u0d4d\u0d30\u0d35\u0d1c\u0d4d\u0d30', 52, 'upEndravajra', 'v-v--vv-v--', 11],
[58, u'\u0d09\u0d30\u0d4d\u200d\u0d35\u0d36\u0d3f', 125, 'ur_vaSi', 'vvv--v--v--v-', 13],
[59, u'\u0d0a\u0d28\u0d15\u0d3e\u0d15\u0d33\u0d3f', 326, '', '', 0],
[60, u'\u0d0a\u0d28\u0d24\u0d30\u0d02\u0d17\u0d3f\u0d23\u0d3f', 331, '', '', 0],
[61, u'\u0d0f\u0d32', 161, 'Ela', 'vv-v-vvvvvvvv--', 15],
[62, u'\u0d14\u0d2a\u0d1a\u0d4d\u0d1b\u0d28\u0d4d\u0d26\u0d38\u0d3f\u0d15\u0d02', 314, '', '', 0],
[63, u'\u0d15\u0d28\u0d4d\u0d2f', 7, 'kanya', '----', 4],
[64, u'\u0d15\u0d28\u0d4d\u0d2f', 108, 'kanya', '-vvvv-vvvv--', 12],
[65, u'\u0d15\u0d28\u0d4d\u0d2f\u0d15\u0d3e\u0d2e\u0d23\u0d3f', 277, 'kanyakAmaNi', '-v-v-v-v-v-v-v-v-v-v-v-vv-', 26],
[66, u'\u0d15\u0d2c\u0d30\u0d3f', 23, 'kabari', '--vv-vv-', 8],
[67, u'\u0d15\u0d2e\u0d28\u0d40\u0d2f\u0d02', 180, 'kamaneeyam', 'vv-vv-vv-vv-vv--', 16],
[68, u'\u0d15\u0d2e\u0d32\u0d26\u0d3f\u0d35\u0d3e\u0d15\u0d30\u0d02', 257, 'kamaladivAkaram', 'vvvv-vvvvvv-vvvvvv----', 22],
[69, u'\u0d15\u0d2e\u0d32\u0d3e\u0d15\u0d30\u0d02', 152, 'kamalAkaram', 'vvvvvv-vvvv-vv', 14],
[70, u'\u0d15\u0d2e\u0d32\u0d3e\u0d15\u0d4d\u0d37\u0d02', 224, 'kamalAksham', '-vv--vv---vvvv-vv--', 19],
[71, u'\u0d15\u0d30\u0d15\u0d2e\u0d32\u0d02', 207, 'karakamalam', '-vv-vvvvvv-vvvvvv-', 18],
[72, u'\u0d15\u0d30\u0d41\u0d23\u0d3e\u0d15\u0d30\u0d02', 153, 'karuNAkaram', 'vv-vvvvvvvvvv-', 14],
[73, u'\u0d15\u0d30\u0d02\u0d2d\u0d02', 275, 'karambham', 'vvvv-vvvvvvvv--vv-vvvvvv--', 26],
[74, u'\u0d15\u0d32\u0d3f\u0d15', 295, '', '', 0],
[75, u'\u0d15\u0d32\u0d47\u0d28\u0d4d\u0d26\u0d41\u0d35\u0d26\u0d28', 339, '', '', 0],
[76, u'\u0d15\u0d32\u0d4d\u0d2f\u0d3e\u0d23\u0d3f', 342, '', '', 0],
[77, u'\u0d15\u0d33\u0d15\u0d3e\u0d1e\u0d4d\u0d1a\u0d3f', 323, '', '', 0],
[78, u'\u0d15\u0d33\u0d24\u0d4d\u0d30\u0d02', 248, 'kaLathram', 'vvvv--vvvv--vvvv-vv--', 21],
[79, u'\u0d15\u0d3e\u0d15\u0d33\u0d3f', 322, '', '', 0],
[80, u'\u0d15\u0d3e\u0d28\u0d4d\u0d24', 191, 'kAntha', 'v---vvvvv-v-vv-v-', 17],
[81, u'\u0d15\u0d3e\u0d2e\u0d15\u0d4d\u0d30\u0d40\u0d21', 159, 'kAmakreeDa', '---------------', 15],
[82, u'\u0d15\u0d3e\u0d30\u0d40\u0d30\u0d02', 235, 'kAreeram', 'vvvv--vv---vvvv-vv--', 20],
[83, u'\u0d15\u0d41\u0d2e\u0d3e\u0d30\u0d3f', 68, 'kumAri', 'v--v--v--v-', 11],
[84, u'\u0d15\u0d41\u0d2e\u0d3e\u0d30\u0d3f', 147, 'kumAri', 'vvvv-v-vvv-v--', 14],
[85, u'\u0d15\u0d41\u0d2e\u0d41\u0d26\u0d3f\u0d28\u0d3f', 246, 'kumudini', 'vvv-vvvvv-vvvvv-vv-v-', 21],
[86, u'\u0d15\u0d41\u0d2e\u0d41\u0d26\u0d4d\u0d35\u0d24\u0d3f', 270, 'kumudvathi', '-v-vv-v-vv-vv-vv-vv-vv-v-', 25],
[87, u'\u0d15\u0d41\u0d32\u0d2a\u0d3e\u0d32\u0d02', 227, 'kulapAlam', 'vv-vvvvvvvvvvvvvv--', 19],
[88, u'\u0d15\u0d41\u0d35\u0d32\u0d3f\u0d28\u0d3f', 226, 'kuvalini', 'vvvv-vvvvvvvv-vvvv-', 19],
[89, u'\u0d15\u0d41\u0d38\u0d41\u0d2e\u0d2e\u0d1e\u0d4d\u0d1c\u0d30\u0d3f', 242, 'kusumamanjjari', '-v-vvv-v-vvv-v-vvv-v-', 21],
[90, u'\u0d15\u0d41\u0d38\u0d41\u0d2e\u0d3f\u0d24\u0d32\u0d24\u0d3e\u0d35\u0d47\u0d32\u0d4d\u0d32\u0d3f\u0d24', 211, 'kusumithalathAvEllitha', '-----vvvvv--v--v--', 18],
[91, u'\u0d15\u0d41\u0d38\u0d41\u0d2e\u0d35\u0d3f\u0d1a\u0d3f\u0d24\u0d4d\u0d30', 93, 'kusumavichithra', 'vvvv--vvvv--', 12],
[92, u'\u0d15\u0d43\u0d36\u0d2e\u0d26\u0d4d\u0d27\u0d4d\u0d2f', 337, '', '', 0],
[93, u'\u0d15\u0d47\u0d15', 328, '', '', 0],
[94, u'\u0d15\u0d47\u0d24\u0d41\u0d2e\u0d24\u0d3f', 290, 'kEthumathi', 'AV|vv-v-vvv--|-vv-v-vvv--|vv-v-vvv--|-vv-v-vvv--', (10, 11)],
[95, u'\u0d15\u0d47\u0d30\u0d33\u0d3f', 63, 'kEraLi', 'v-v--v--v--', 11],
[96, u'\u0d15\u0d4b\u0d15\u0d30\u0d24\u0d02', 109, 'kOkaratham', 'vv-v--vv-v--', 12],
[97, u'\u0d15\u0d4d\u0d30\u0d4c\u0d1e\u0d4d\u0d1a\u0d2a\u0d26', 269, 'kraunchapada', '-vv---vv--vvvvvvvvvvvvvv-', 25],
[98, u'\u0d15\u0d4d\u0d30\u0d4c\u0d1e\u0d4d\u0d1a\u0d2a\u0d26\u0d02', 266, 'kraunchapadam', '-vv---vv--vvvvvvvvvvvv--', 24],
[99, u'\u0d15\u0d4d\u0d37\u0d2e', 120, 'kshama', 'vvvvvv--v--v-', 13],
[100, u'\u0d16\u0d17', 2, 'khaga', 'v', 1],
[101, u'\u0d17\u0d02\u0d17', 239, 'gamga', 'vvvv-----vvvvvv-vv--', 20],
[102, u'\u0d17\u0d3e\u0d25', 297, '', '', 0],
[103, u'\u0d17\u0d3f\u0d30\u0d3f\u0d36\u0d3f\u0d16\u0d30\u0d02', 150, 'giriSikharam', '-vvvvvvvvvvvv-', 14],
[104, u'\u0d17\u0d3f\u0d30\u0d3f\u0d38\u0d3e\u0d30\u0d02', 182, 'girisAram', 'vvvv-vv---vvvv--', 16],
[105, u'\u0d17\u0d40\u0d24\u0d3f', 309, '', '', 0],
[106, u'\u0d17\u0d41\u0d23\u0d1c\u0d3e\u0d32\u0d02', 199, 'guNajAlam', 'vvvv-vvvvvv--vv--', 17],
[107, u'\u0d17\u0d41\u0d23\u0d38\u0d26\u0d28\u0d02', 268, 'guNasadanam', 'vv--vv-vvvv-vvvv-vvvvvv-', 24],
[108, u'\u0d17\u0d41\u0d30\u0d41', 78, 'guru', '-vvvv-vvvv-', 11],
[109, u'\u0d17\u0d4c\u0d30\u0d3f', 9, 'gauri', '-----', 5],
[110, u'\u0d17\u0d4c\u0d30\u0d3f (\u0d2a\u0d4d\u0d30\u0d2d)', 92, 'gauri (prabha)', 'vvvvvv-v--v-', 12],
[111, u'\u0d1a\u0d1e\u0d4d\u0d1a\u0d30\u0d40\u0d15\u0d3e\u0d35\u0d32\u0d3f', 122, 'chanchareekAvali', 'v------v--v--', 13],
[112, u'\u0d1a\u0d23\u0d4d\u0d21\u0d35\u0d43\u0d37\u0d4d\u0d1f\u0d3f\u0d2a\u0d4d\u0d30\u0d2f\u0d3e\u0d24\u0d02', 298, '', '', 0],
[113, u'\u0d1a\u0d28\u0d4d\u0d26\u0d28\u0d38\u0d3e\u0d30\u0d02', 276, 'chandanasAram', '-vv-vv-vv-vv-vv-vv-vv-vv--', 26],
[114, u'\u0d1a\u0d28\u0d4d\u0d26\u0d4d\u0d30\u0d30\u0d47\u0d16', 163, 'chandrarEkha', '-v--v--v--v--v-', 15],
[115, u'\u0d1a\u0d28\u0d4d\u0d26\u0d4d\u0d30\u0d32\u0d47\u0d16', 123, 'chandralEkha', 'vvvvv--v--v--', 13],
[116, u'\u0d1a\u0d28\u0d4d\u0d26\u0d4d\u0d30\u0d32\u0d47\u0d16', 162, 'chandralEkha', '----v----v--v--', 15],
[117, u'\u0d1a\u0d28\u0d4d\u0d26\u0d4d\u0d30\u0d35\u0d30\u0d4d\u200d\u0d24\u0d4d\u0d2e', 103, 'chandravar_thma', '-v-vvv-vvvv-', 12],
[118, u'\u0d1a\u0d2a\u0d32\u0d3e\u0d35\u0d15\u0d4d\u0d24\u0d4d\u0d30\u0d02', 31, 'chapalAvakthram', 'ANUSHTUP', 8],
[119, u'\u0d1a\u0d2a\u0d32\u0d3e\u0d30\u0d4d\u0d2f', 308, '', '', 0],
[120, u'\u0d1a\u0d2e\u0d4d\u0d2a\u0d15\u0d2e\u0d3e\u0d32', 44, 'champakamAla', '-vv---vv--', 10],
[121, u'\u0d1a\u0d3e\u0d30\u0d23\u0d17\u0d40\u0d24\u0d02', 75, 'chAraNageetham', '-vv-vv-vv--', 11],
[122, u'\u0d1a\u0d3e\u0d30\u0d41\u0d39\u0d3e\u0d38\u0d3f\u0d28\u0d3f', 321, '', '', 0],
[123, u'\u0d1a\u0d3f\u0d24\u0d4d\u0d30\u0d2a\u0d26', 18, 'chithrapada', '-vv-vv--', 8],
[124, u'\u0d1a\u0d3f\u0d24\u0d4d\u0d30\u0d32\u0d47\u0d16', 192, 'chithralEkha', 'vvvv-vvv--vvv-v--', 17],
[125, u'\u0d1a\u0d3f\u0d24\u0d4d\u0d30\u0d35\u0d43\u0d24\u0d4d\u0d24', 71, 'chithravr^ththa', 'vvvvvv--v--', 11],
[126, u'\u0d1b\u0d3e\u0d28\u0d4d\u0d26\u0d38\u0d3f', 172, 'chhAndasi', '-v--v--v--v--v--', 16],
[127, u'\u0d1c\u0d17\u0d24\u0d40\u0d24\u0d3f\u0d32\u0d15\u0d02', 197, 'jagatheethilakam', 'vv-vv-vvvv-vvvv--', 17],
[128, u'\u0d1c\u0d18\u0d28\u0d1a\u0d2a\u0d32', 308, '', '', 0],
[129, u'\u0d1c\u0d32\u0d27\u0d30\u0d28\u0d40\u0d32\u0d02', 80, 'jaladharaneelam', 'vvvv-vvvv--', 11],
[130, u'\u0d1c\u0d32\u0d27\u0d30\u0d2e\u0d3e\u0d32', 98, 'jaladharamAla', '----vvvv----', 12],
[131, u'\u0d1c\u0d32\u0d4b\u0d26\u0d4d\u0d27\u0d24\u0d17\u0d24\u0d3f', 94, 'jalOddhathagathi', 'v-vvv-v-vvv-', 12],
[132, u'\u0d1c\u0d40\u0d2e\u0d42\u0d24\u0d02', 299, '', '', 0],
[133, u'\u0d1c\u0d4d\u0d35\u0d3e\u0d32', 112, 'jvAla', 'vvvvvv-vv---', 12],
[134, u'\u0d24\u0d1f\u0d3f\u0d28\u0d3f', 244, 'thaTini', 'vv-v-vvv-v-vvv-v-vvv-', 21],
[135, u'\u0d24\u0d28\u0d41\u0d2e\u0d26\u0d4d\u0d27\u0d4d\u0d2f', 11, 'thanumaddhya', '--vv--', 6],
[136, u'\u0d24\u0d28\u0d4d\u0d35\u0d3f', 263, 'thanvi', '-vv--vvvvvv--vv-vvvvvv--', 24],
[137, u'\u0d24\u0d30\u0d02\u0d17\u0d3f\u0d23\u0d3f', 330, '', '', 0],
[138, u'\u0d24\u0d30\u0d02\u0d17\u0d3f\u0d23\u0d3f', 255, 'tharamgiNi', 'vvv-v-vvv-v-vvv-v-vvv-', 22],
[139, u'\u0d24\u0d35\u0d3f\u0d2a\u0d41\u0d32', 36, 'thavipula', 'ANUSHTUP', 8],
[140, u'\u0d24\u0d3e\u0d2e\u0d30\u0d38\u0d02 (\u0d32\u0d33\u0d3f\u0d24\u0d2a\u0d26\u0d02)', 102, 'thAmarasam (laLithapadam)', 'vvvv-vv-vv--', 12],
[141, u'\u0d24\u0d4b\u0d1f\u0d15\u0d02', 86, 'thOTakam', 'vv-vv-vv-vv-', 12],
[142, u'\u0d24\u0d4d\u0d30\u0d3f\u0d16\u0d23\u0d4d\u0d21\u0d3f\u0d15', 305, '', '', 0],
[143, u'\u0d26\u0d15\u0d4d\u0d37\u0d3f\u0d23\u0d3e\u0d28\u0d4d\u0d24\u0d3f\u0d15', 316, '', '', 0],
[144, u'\u0d26\u0d33\u0d02', 164, 'daLam', 'vv-v-vvvvvvvvv-', 15],
[145, u'\u0d26\u0d3f\u0d36 (\u0d05\u0d32\u0d38)', 212, 'diSa (alasa)', 'vvvvvv-v--v--v--v-', 18],
[146, u'\u0d26\u0d42\u0d37\u0d23\u0d39\u0d30\u0d23\u0d02', 135, 'dooshaNaharaNam', 'vv-vvvv-vvvv-', 13],
[147, u'\u0d26\u0d4b\u0d27\u0d15\u0d02', 59, 'dOdhakam', '-vv-vv-vv--', 11],
[148, u'\u0d26\u0d4d\u0d30\u0d41\u0d24\u0d15\u0d3e\u0d15\u0d33\u0d3f', 327, '', '', 0],
[149, u'\u0d26\u0d4d\u0d30\u0d41\u0d24\u0d17\u0d24\u0d3f', 107, 'druthagathi', 'vvv-vvv-vv--', 12],
[150, u'\u0d26\u0d4d\u0d30\u0d41\u0d24\u0d2a\u0d26\u0d02', 106, 'druthapadam', 'vvv-vvvvvv--', 12],
[151, u'\u0d26\u0d4d\u0d30\u0d41\u0d24\u0d2e\u0d26\u0d4d\u0d27\u0d4d\u0d2f', 287, 'druthamaddhya', 'AV|-vv-vv-vv--|vvvv-vv-vv--|-vv-vv-vv--|vvvv-vv-vv--', (11, 12)],
[152, u'\u0d26\u0d4d\u0d30\u0d41\u0d24\u0d35\u0d3f\u0d33\u0d02\u0d2c\u0d3f\u0d24\u0d02', 84, 'druthaviLambitham', 'vvv-vv-vv-v-', 12],
[153, u'\u0d27\u0d30\u0d23\u0d3f', 79, 'dharaNi', 'vv-vv-vvvv-', 11],
[154, u'\u0d27\u0d30\u0d3e\u0d28\u0d28\u0d4d\u0d26\u0d3f\u0d28\u0d3f', 129, 'dharAnandini', 'v--v-vvv-vv--', 13],
[155, u'\u0d27\u0d40\u0d30\u0d32\u0d33\u0d3f\u0d24', 173, 'dheeralaLitha', '-vv-v-vvv-v-vvv-', 16],
[156, u'\u0d27\u0d43\u0d24\u0d15\u0d41\u0d24\u0d41\u0d15\u0d02', 229, 'dhr^thakuthukam', 'vvvvvv-vv-vvvvvvvv-', 19],
[157, u'\u0d28\u0d24\u0d4b\u0d28\u0d4d\u0d28\u0d24', 349, '', '', 0],
[158, u'\u0d28\u0d30\u0d4d\u200d\u0d15\u0d4d\u0d15\u0d41\u0d1f\u0d15\u0d02', 189, 'nar_kkuTakam', 'vvvv-v-vvv-vv-vv-', 17],
[159, u'\u0d28\u0d35\u0d24\u0d3e\u0d30\u0d41\u0d23\u0d4d\u0d2f\u0d02', 131, 'navathAruNyam', 'vvvvvvvvvv---', 13],
[160, u'\u0d28\u0d35\u0d2e\u0d3e\u0d32\u0d3f\u0d15', 99, 'navamAlika', 'vvvv-v-vvv--', 12],
[161, u'\u0d28\u0d35\u0d3f\u0d2a\u0d41\u0d32', 33, 'navipula', 'ANUSHTUP', 8],
[162, u'\u0d28\u0d3e\u0d17\u0d30\u0d3f\u0d15\u0d02', 26, 'nAgarikam', '-vv-v-v-', 8],
[163, u'\u0d28\u0d3e\u0d30\u0d3e\u0d1a\u0d3f\u0d15', 22, 'nArAchika', '--v-v-v-', 8],
[164, u'\u0d28\u0d3e\u0d30\u0d3f', 5, 'naari', '---', 3],
[165, u'\u0d28\u0d3f\u0d36 (\u0d05\u0d32\u0d38)', 212, 'niSa (alasa)', 'vvvvvv-v--v--v--v-', 18],
[166, u'\u0d28\u0d43\u0d2a\u0d24\u0d3f\u0d32\u0d32\u0d3e\u0d2e\u0d02 (\u0d32\u0d32\u0d3e\u0d2e\u0d02)', 251, 'nr^pathilalAmam (lalAmam)', 'vvvv-vv--vvvv--vvvv--', 21],
[167, u'\u0d2a\u0d1e\u0d4d\u0d1a\u0d1a\u0d3e\u0d2e\u0d30\u0d02 (\u0d38\u0d41\u0d2e\u0d02\u0d17\u0d32)', 101, 'panchachAmaram (sumamgala)', 'v-v-vvv-v-v-', 12],
[168, u'\u0d2a\u0d1e\u0d4d\u0d1a\u0d1a\u0d3e\u0d2e\u0d30\u0d02', 169, 'panchachAmaram', 'v-v-v-v-v-v-v-v-', 16],
[169, u'\u0d2a\u0d24\u0d4d\u0d25\u0d4d\u0d2f', 148, 'paththhya', 'vv-v-vvv-v--v-', 14],
[170, u'\u0d2a\u0d24\u0d4d\u0d25\u0d4d\u0d2f\u0d3e\u0d30\u0d4d\u0d2f', 307, '', '', 0],
[171, u'\u0d2a\u0d24\u0d4d\u0d25\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d4d\u0d24\u0d4d\u0d30\u0d02', 28, 'paththhyAvakthram', 'ANUSHTUP', 8],
[172, u'\u0d2a\u0d24\u0d4d\u0d30\u0d32\u0d24', 179, 'pathralatha', '-vvvv-vv-vv--vv-', 16],
[173, u'\u0d2a\u0d26\u0d1a\u0d24\u0d41\u0d30\u0d42\u0d30\u0d4d\u200d\u0d26\u0d4d\u0d27\u0d4d\u0d35\u0d02', 294, '', '', 0],
[174, u'\u0d2a\u0d26\u0d4d\u0d2f\u0d02', 37, '', '', 8],
[175, u'\u0d2a\u0d30\u0d3e\u0d35\u0d24\u0d3f', 285, 'parAvathi', 'AV|-v-v-v-v-v-v|v-v-v-v-v-v--|-v-v-v-v-v-v|v-v-v-v-v-v--', (12, 13)],
[176, u'\u0d2a\u0d30\u0d3f\u0d23\u0d3e\u0d2e\u0d02', 194, 'pariNAmam', '-vvvv-vvvvvv-vv--', 17],
[177, u'\u0d2a\u0d30\u0d3f\u0d2e\u0d33\u0d02', 175, 'parimaLam', 'vvvvvvvvvvvvvvv-', 16],
[178, u'\u0d2a\u0d30\u0d4d\u0d2f\u0d38\u0d4d\u0d24\u0d15\u0d3e\u0d1e\u0d4d\u0d1a\u0d3f', 337, '', '', 0],
[179, u'\u0d2a\u0d32\u0d4d\u0d32\u0d35\u0d3f\u0d28\u0d3f', 348, '', '', 0],
[180, u'\u0d2a\u0d3e\u0d24\u0d4d\u0d30\u0d02', 234, 'pAthram', 'vvvv-vv-vvvvvvvvvv--', 20],
[181, u'\u0d2a\u0d41\u0d1f\u0d02', 95, 'puTam', 'vvvvvv---v--', 12],
[182, u'\u0d2a\u0d41\u0d33\u0d15\u0d02', 200, 'puLakam', 'vv-vv-vvvv--vvvv-', 17],
[183, u'\u0d2a\u0d41\u0d37\u0d4d\u0d2a\u0d3f\u0d24\u0d3e\u0d17\u0d4d\u0d30', 280, 'pushpithAgra', 'AV|vvvvvv-v-v--|vvvv-vv-v-v--|vvvvvv-v-v--|vvvv-vv-v-v--', (12, 13)],
[184, u'\u0d2a\u0d43\u0d24\u0d4d\u0d25\u0d4d\u0d35\u0d3f', 70, 'pr^ththhvi', 'vvvvvv-vv--', 11],
[185, u'\u0d2a\u0d43\u0d24\u0d4d\u0d25\u0d4d\u0d35\u0d3f', 185, 'pr^ththhvi', 'v-vvv-v-vvv-v--v-', 17],
[186, u'\u0d2a\u0d4d\u0d30\u0d1a\u0d3f\u0d24\u0d15\u0d02', 300, '', '', 0],
[187, u'\u0d2a\u0d4d\u0d30\u0d25\u0d2e\u0d2a\u0d26\u0d02', 223, 'prathhamapadam', 'vvvvvv-vvvvvv-vvvv-', 19],
[188, u'\u0d2a\u0d4d\u0d30\u0d2d', 92, 'prabha', 'vvvvvv-v--v-', 12],
[189, u'\u0d2a\u0d4d\u0d30\u0d2d\u0d26\u0d4d\u0d30\u0d15\u0d02', 128, 'prabhadrakam', 'vvvv-vvv-v-v-', 13],
[190, u'\u0d2a\u0d4d\u0d30\u0d2d\u0d26\u0d4d\u0d30\u0d15\u0d02', 160, 'prabhadrakam', 'vvvv-v-vvv-v-v-', 15],
[191, u'\u0d2a\u0d4d\u0d30\u0d2e\u0d26', 141, 'pramada', 'vvvv-v-vvv-vv-', 14],
[192, u'\u0d2a\u0d4d\u0d30\u0d2e\u0d3e\u0d23\u0d3f\u0d15', 21, 'pramANika', 'v-v-v-v-', 8],
[193, u'\u0d2a\u0d4d\u0d30\u0d2e\u0d3f\u0d24\u0d3e\u0d15\u0d4d\u0d37\u0d30', 85, 'pramithAkshara', 'vv-v-vvv-vv-', 12],
[194, u'\u0d2a\u0d4d\u0d30\u0d2e\u0d41\u0d26\u0d3f\u0d24\u0d35\u0d26\u0d28 (\u0d2a\u0d4d\u0d30\u0d2d)', 92, 'pramudithavadana (prabha)', 'vvvvvv-v--v-', 12],
[195, u'\u0d2a\u0d4d\u0d30\u0d35\u0d43\u0d24\u0d4d\u0d24\u0d15\u0d02', 319, '', '', 0],
[196, u'\u0d2a\u0d4d\u0d30\u0d39\u0d30\u0d23\u0d24\u0d3f\u0d32\u0d15\u0d02', 146, 'praharaNathilakam', 'vvvvvv-vvvvvv-', 14],
[197, u'\u0d2a\u0d4d\u0d30\u0d39\u0d30\u0d4d\u200d\u0d37\u0d3f\u0d23\u0d3f', 117, 'prahar_shiNi', '---vvvv-v-v--', 13],
[198, u'\u0d2a\u0d4d\u0d30\u0d3e\u0d1a\u0d4d\u0d2f\u0d35\u0d43\u0d24\u0d4d\u0d24\u0d3f', 318, '', '', 0],
[199, u'\u0d2a\u0d4d\u0d30\u0d3f\u0d2f\u0d02\u0d35\u0d26', 96, 'priyamvada', 'vvv-vvv-v-v-', 12],
[200, u'\u0d2b\u0d32\u0d2e\u0d41\u0d16\u0d3f', 40, 'phalamukhi', '-v-vvvvv-', 9],
[201, u'\u0d2d\u0d26\u0d4d\u0d30\u0d15', 73, 'bhadraka', 'vvvvvv-v-v-', 11],
[202, u'\u0d2d\u0d26\u0d4d\u0d30\u0d15\u0d02', 253, 'bhadrakam', '-vv-v-vvv-v-vvv-v-vvv-', 22],
[203, u'\u0d2d\u0d26\u0d4d\u0d30\u0d35\u0d3f\u0d30\u0d3e\u0d33\u0d4d\u200d', 289, 'bhadravirAL', 'AV|--vv-v-v--|---vv-v-v--|--vv-v-v--|---vv-v-v--', (10, 11)],
[204, u'\u0d2d\u0d26\u0d4d\u0d30\u0d3f\u0d15', 42, 'bhadrika', '-v-vvv-v-', 9],
[205, u'\u0d2d\u0d35\u0d24\u0d30\u0d23\u0d02', 206, 'bhavatharaNam', '-vv-vvvvvvvv-vvvv-', 18],
[206, u'\u0d2d\u0d35\u0d38\u0d3e\u0d30\u0d02', 238, 'bhavasAram', 'vvvv-vv-vvvvvvvvvv--', 20],
[207, u'\u0d2d\u0d35\u0d3f\u0d2a\u0d41\u0d32', 32, 'bhavipula', 'ANUSHTUP', 8],
[208, u'\u0d2d\u0d3e\u0d30\u0d24\u0d3f (\u0d35\u0d3e\u0d23\u0d3f\u0d28\u0d3f)', 174, 'bhArathi (vANini)', 'vvvv-v-vvv-v-v--', 16],
[209, u'\u0d2d\u0d41\u0d1c\u0d02\u0d17\u0d2a\u0d4d\u0d30\u0d2f\u0d3e\u0d24\u0d02', 87, 'bhujamgaprayAtham', 'v--v--v--v--', 12],
[210, u'\u0d2d\u0d41\u0d1c\u0d02\u0d17\u0d35\u0d3f\u0d1c\u0d43\u0d02\u0d2d\u0d3f\u0d24\u0d02', 273, 'bhujamgavijr^mbhitham', '--------vvvvvvvvvv-v-vv-v-', 26],
[211, u'\u0d2d\u0d4d\u0d30\u0d2e\u0d30\u0d35\u0d3f\u0d32\u0d38\u0d3f\u0d24\u0d02', 60, 'bhramaravilasitham', '----vvvvvv-', 11],
[212, u'\u0d2d\u0d4d\u0d30\u0d2e\u0d30\u0d3e\u0d35\u0d32\u0d3f', 220, 'bhramarAvali', 'vvv-vv-v-vv-v-vv-v-', 19],
[213, u'\u0d2e\u0d15\u0d30\u0d28\u0d4d\u0d26\u0d3f\u0d15', 219, 'makarandika', 'v-----vvvvv-v-vv-v-', 19],
[214, u'\u0d2e\u0d1e\u0d4d\u0d1c\u0d30\u0d3f (\u0d2a\u0d24\u0d4d\u0d25\u0d4d\u0d2f)', 148, 'manjjari (paththhya)', 'vv-v-vvv-v--v-', 14],
[215, u'\u0d2e\u0d1e\u0d4d\u0d1c\u0d30\u0d3f', 295, '', '', 0],
[216, u'\u0d2e\u0d1e\u0d4d\u0d1c\u0d30\u0d3f', 338, '', '', 0],
[217, u'\u0d2e\u0d1e\u0d4d\u0d1c\u0d41\u0d2d\u0d3e\u0d37\u0d3f\u0d23\u0d3f', 118, 'manjubhAshiNi', 'vv-v-vvv-v-v-', 13],
[218, u'\u0d2e\u0d1e\u0d4d\u0d1c\u0d41\u0d33', 260, 'manjjuLa', 'vvvv-v-vvv-v-vvv-v-vvv-', 23],
[219, u'\u0d2e\u0d23\u0d3f\u0d15\u0d3e\u0d1e\u0d4d\u0d1a\u0d3f', 324, '', '', 0],
[220, u'\u0d2e\u0d23\u0d3f\u0d18\u0d43\u0d23\u0d3f', 262, 'maNighr^Ni', 'vvvv-vvvvvv-vvvvvv-vv--', 23],
[221, u'\u0d2e\u0d23\u0d3f\u0d26\u0d40\u0d2a\u0d02', 193, 'maNideepam', 'vvvvvvvvvvvvvvv--', 17],
[222, u'\u0d2e\u0d23\u0d3f\u0d26\u0d40\u0d2a\u0d4d\u0d24\u0d3f', 221, 'maNideepthi', '---vv-vv---vv-vv---', 19],
[223, u'\u0d2e\u0d23\u0d3f\u0d2e\u0d15\u0d41\u0d1f\u0d02', 271, 'maNimakuTam', 'vvvvvv-vvvv-vv-vvvv-vvvv-', 25],
[224, u'\u0d2e\u0d23\u0d3f\u0d2e\u0d26\u0d4d\u0d27\u0d4d\u0d2f\u0d02', 39, 'maNimaddhyam', '-vv---vv-', 9],
[225, u'\u0d2e\u0d23\u0d3f\u0d2e\u0d3e\u0d32', 91, 'maNimAla', '--vv----vv--', 12],
[226, u'\u0d2e\u0d24\u0d4d\u0d24', 45, 'maththa', '----vvvv--', 10],
[227, u'\u0d2e\u0d24\u0d4d\u0d24\u0d15\u0d3e\u0d36\u0d3f\u0d28\u0d3f', 127, 'maththakASini', 'v-v--vvv-v-v-', 13],
[228, u'\u0d2e\u0d24\u0d4d\u0d24\u0d2e\u0d2f\u0d42\u0d30\u0d02', 121, 'maththamayooram', '-----vv--vv--', 13],
[229, u'\u0d2e\u0d24\u0d4d\u0d24\u0d3e\u0d15\u0d4d\u0d30\u0d40\u0d21\u0d3e', 259, 'maththAkreeDa', '--------vvvvvvvvvvvvvv-', 23],
[230, u'\u0d2e\u0d24\u0d4d\u0d24\u0d47\u0d2d\u0d02', 252, 'maththEbham', '--v-vvv--v-vvv--v-vvv-', 22],
[231, u'\u0d2e\u0d24\u0d4d\u0d24\u0d47\u0d2d\u0d35\u0d3f\u0d15\u0d4d\u0d30\u0d40\u0d21\u0d3f\u0d24\u0d02', 233, 'maththEbhavikreeDitham', '----vv-v-vvv---v--v-', 20],
[232, u'\u0d2e\u0d26\u0d28\u0d3e\u0d30\u0d4d\u200d\u0d24\u0d4d\u0d24', 149, 'madanArththa', '--vv--vv--vv--', 14],
[233, u'\u0d2e\u0d26\u0d28\u0d40\u0d2f\u0d02', 201, 'madaneeyam', 'vvvvvv-vvvv--vv--', 17],
[234, u'\u0d2e\u0d26\u0d2e\u0d28\u0d4d\u0d25\u0d30', 336, '', '', 0],
[235, u'\u0d2e\u0d26\u0d32\u0d47\u0d16', 14, 'madalEkha', '---vv--', 7],
[236, u'\u0d2e\u0d26\u0d3f\u0d30', 254, 'madira', '-vv-vv-vv-vv-vv-vv-vv-', 22],
[237, u'\u0d2e\u0d27\u0d41\u0d15\u0d30\u0d15\u0d33\u0d2d\u0d02', 267, 'madhukarakaLabham', 'vvvvvv-vv---vv-vvvvvvvv-', 24],
[238, u'\u0d2e\u0d27\u0d41\u0d2e\u0d24\u0d3f', 15, 'madhumathi', 'vvv-vv-', 7],
[239, u'\u0d2e\u0d27\u0d41\u0d30\u0d24\u0d30\u0d02', 236, 'madhuratharam', 'vvvvvvvvvvvvvv-vvvv-', 20],
[240, u'\u0d2e\u0d28\u0d4b\u0d30\u0d2e', 48, 'manOrama', 'vvv-v-v-v-', 10],
[241, u'\u0d2e\u0d28\u0d4d\u0d26\u0d3e\u0d15\u0d4d\u0d30\u0d3e\u0d28\u0d4d\u0d24', 186, 'mandAkrAntha', '----vvvvv--v--v--', 17],
[242, u'\u0d2e\u0d2f\u0d42\u0d30\u0d38\u0d3e\u0d30\u0d3f\u0d23\u0d3f', 47, 'mayoorasAriNi', '-v-v-v-v--', 10],
[243, u'\u0d2e\u0d30\u0d24\u0d15\u0d28\u0d40\u0d32\u0d02', 168, 'marathakaneelam', 'vv---vvvv--vv--', 15],
[244, u'\u0d2e\u0d32\u0d4d\u0d32\u0d3f\u0d15', 203, 'mallika', '-v-vv-v-vv-v-vv-v-', 18],
[245, u'\u0d2e\u0d35\u0d3f\u0d2a\u0d41\u0d32', 35, 'mavipula', 'ANUSHTUP', 8],
[246, u'\u0d2e\u0d39\u0d3e\u0d2e\u0d3e\u0d32\u0d3f\u0d15', 215, 'mahAmAlika', 'vvvvvv-v--v--v--v-', 18],
[247, u'\u0d2e\u0d3e\u0d24\u0d4d\u0d30\u0d3e\u0d38\u0d2e\u0d15\u0d02', 312, '', '', 0],
[248, u'\u0d2e\u0d3e\u0d23\u0d35\u0d15\u0d02', 19, 'mANavakam', '-vv--vv-', 8],
[249, u'\u0d2e\u0d3e\u0d28\u0d3f\u0d28\u0d3f', 100, 'mAnini', 'vvvv-vv-v-v-', 12],
[250, u'\u0d2e\u0d3e\u0d32', 10, 'mAla', 'v-v--', 5],
[251, u'\u0d2e\u0d3e\u0d32\u0d3f\u0d28\u0d3f', 156, 'mAlini', 'vvvvvv---v--v--', 15],
[252, u'\u0d2e\u0d3f\u0d36\u0d4d\u0d30\u0d15\u0d3e\u0d15\u0d33\u0d3f', 308, '', '', 0],
[253, u'\u0d2e\u0d41\u0d16\u0d1a\u0d2a\u0d32', 308, '', '', 0],
[254, u'\u0d2e\u0d43\u0d17\u0d3f', 6, 'mr^gi', '-v-', 3],
[255, u'\u0d2e\u0d47\u0d18\u0d35\u0d3f\u0d37\u0d4d\u0d2b\u0d42\u0d30\u0d4d\u200d\u200c\u0d1c\u0d4d\u0d1c\u0d3f\u0d24\u0d02', 218, 'mEghavishphoor_jjitham', 'v-----vvvvv--v--v--', 19],
[256, u'\u0d2e\u0d4c\u0d15\u0d4d\u0d24\u0d3f\u0d15\u0d26\u0d3e\u0d2e', 88, 'maukthikadAma', 'v-vv-vv-vv-v', 12],
[257, u'\u0d2e\u0d4c\u0d15\u0d4d\u0d24\u0d3f\u0d15\u0d2a\u0d02\u0d15\u0d4d\u0d24\u0d3f', 65, 'maukthikapamkthi', 'vvvv---vv--', 11],
[258, u'\u0d2e\u0d4c\u0d15\u0d4d\u0d24\u0d3f\u0d15\u0d2e\u0d3e\u0d32', 61, 'maukthikamAla', '-vv--vvvv--', 11],
[259, u'\u0d2e\u0d02\u0d17\u0d33\u0d2b\u0d32\u0d15\u0d02', 138, 'mamgaLaphalakam', 'vvvvvv--vvvv-', 13],
[260, u'\u0d2f\u0d41\u0d17\u0d4d\u0d2e\u0d35\u0d3f\u0d2a\u0d41\u0d32', 29, '', '', 8],
[261, u'\u0d30\u0d24\u0d4d\u0d28\u0d3e\u0d35\u0d32\u0d3f', 13, 'rathnAvali', '-v--v-', 6],
[262, u'\u0d30\u0d25\u0d4b\u0d26\u0d4d\u0d27\u0d24', 55, 'rathhOddhatha', '-v-vvv-v-v-', 11],
[263, u'\u0d30\u0d1c\u0d28\u0d3f', 134, 'rajani', '-vvvv-vvvvvv-', 13],
[264, u'\u0d30\u0d2e\u0d23\u0d02', 76, 'ramaNam', 'vvvvvvvvvv-', 11],
[265, u'\u0d30\u0d2e\u0d23\u0d02', 133, 'ramaNam', 'vvvvvv-vv-vv-', 13],
[266, u'\u0d30\u0d2e\u0d23\u0d02', 204, 'ramaNam', '-vvvv-vvvv-vvvvvv-', 18],
[267, u'\u0d30\u0d2e\u0d23\u0d3f', 195, 'ramaNi', 'vvvvvv-vvvvvv----', 17],
[268, u'\u0d30\u0d2e\u0d23\u0d40\u0d2f\u0d02', 38, 'ramaNeeyam', '---vvvv--', 9],
[269, u'\u0d30\u0d35\u0d3f\u0d2a\u0d41\u0d32', 34, 'ravipula', 'ANUSHTUP', 8],
[270, u'\u0d30\u0d35\u0d3f\u0d30\u0d26\u0d28\u0d02', 250, 'raviradanam', 'vv-vvvvv-vvvv-vvvvvv-', 21],
[271, u'\u0d30\u0d38\u0d2a\u0d3e\u0d24\u0d4d\u0d30\u0d02', 240, 'rasapAthram', 'vvvv---vv--vvvv-vv--', 20],
[272, u'\u0d30\u0d38\u0d30\u0d02\u0d17\u0d02', 178, 'rasaramgam', 'vvvv--vvvv--vv--', 16],
[273, u'\u0d30\u0d41\u0d15\u0d4d\u0d2e\u0d35\u0d24\u0d3f (\u0d1a\u0d2e\u0d4d\u0d2a\u0d15\u0d2e\u0d3e\u0d32)', 44, 'rukmavathi (champakamAla)', '-vv---vv--', 10],
[274, u'\u0d30\u0d41\u0d1a\u0d3f\u0d30\u0d24\u0d30\u0d02', 176, 'ruchiratharam', '----vvvvvv-vvvv-', 16],
[275, u'\u0d32\u0d15\u0d4d\u0d37\u0d4d\u0d2e\u0d3f', 256, 'lakshmi', 'vvvv--vv--vvvvvvvvvv--', 22],
[276, u'\u0d32\u0d32\u0d28', 105, 'lalana', '-vv---vv-vv-', 12],
[277, u'\u0d32\u0d32\u0d3e\u0d2e\u0d02', 251, 'lalAmam', 'vvvv-vv--vvvv--vvvv--', 21],
[278, u'\u0d32\u0d35\u0d32\u0d3f', 295, '', '', 0],
[279, u'\u0d32\u0d33\u0d3f\u0d24', 293, 'laLitha', 'AV|vv-v-vvv-v|vvvvv-v-v-|vvvvvvvv-vv-|vv-v-vvv-v-v-', (10, 10, 12, 13)],
[280, u'\u0d32\u0d33\u0d3f\u0d24', 97, 'laLitha', '--v-vvv-v-v-', 12],
[281, u'\u0d32\u0d33\u0d3f\u0d24\u0d02', 111, 'laLitham', 'vvvvvv----v-', 12],
[282, u'\u0d32\u0d33\u0d3f\u0d24\u0d2a\u0d26\u0d02', 102, 'laLithapadam', 'vvvv-vv-vv--', 12],
[283, u'\u0d32\u0d33\u0d3f\u0d24\u0d02', 265, 'laLitham', 'vvvv-v-vvvv-v-vvv-v-vvv-', 24],
[284, u'\u0d32\u0d33\u0d3f\u0d24\u0d36\u0d30\u0d40\u0d30\u0d02', 132, 'laLithaSareeram', 'vvvv-vvvvvv--', 13],
[285, u'\u0d32\u0d40\u0d32\u0d3e\u0d15\u0d30\u0d02', 299, '', '', 0],
[286, u'\u0d35\u0d15\u0d4d\u0d24\u0d4d\u0d30\u0d02', 27, 'vakthram', 'ANUSHTUP', 8],
[287, u'\u0d35\u0d28\u0d2e\u0d3e\u0d32\u0d02', 237, 'vanamAlam', 'vv--vvvv--vvvv--vv--', 20],
[288, u'\u0d35\u0d30\u0d4d\u200d\u0d26\u0d4d\u0d27\u0d2e\u0d3e\u0d28\u0d02', 296, 'varddhamAnam', '', 0],
[289, u'\u0d35\u0d32\u0d1c\u0d02', 154, 'valajam', 'vvvv-vvvvvvvv-', 14],
[290, u'\u0d35\u0d38\u0d28\u0d4d\u0d24\u0d2e\u0d3e\u0d32\u0d3f\u0d15', 279, 'vasanthamAlika', 'AV|vv-vv-v-v--|vv--vv-v-v--|vv-vv-v-v--|vv--vv-v-v--', (11, 12)],
[291, u'\u0d35\u0d38\u0d28\u0d4d\u0d24\u0d24\u0d3f\u0d32\u0d15 (\u0d35\u0d38\u0d28\u0d4d\u0d24\u0d24\u0d3f\u0d32\u0d15\u0d02)', 139, 'vasanthathilaka (vasanthathilakam)', '--v-vvv-vv-v--', 14],
[292, u'\u0d35\u0d38\u0d28\u0d4d\u0d24\u0d24\u0d3f\u0d32\u0d15\u0d02', 139, 'vasanthathilakam', '--v-vvv-vv-v--', 14],
[293, u'\u0d35\u0d38\u0d41\u0d27', 136, 'vasudha', 'vv--vvvvvv-vv', 13],
[294, u'\u0d35\u0d38\u0d41\u0d2e\u0d24\u0d3f', 12, 'vasumathi', '--vvv-', 6],
[295, u'\u0d35\u0d3e\u0d23\u0d3f', 222, 'vANi', '----vvvv-vvvv--vv--', 19],
[296, u'\u0d35\u0d3e\u0d23\u0d3f\u0d28\u0d3f', 174, 'vANini', 'vvvv-v-vvv-v-v--', 16],
[297, u'\u0d35\u0d3e\u0d24\u0d4b\u0d30\u0d4d\u200d\u0d2e\u0d4d\u0d2e\u0d3f', 58, 'vAthOrMi', '----vv--v--', 11],
[298, u'\u0d35\u0d3e\u0d28\u0d35\u0d3e\u0d38\u0d3f\u0d15', 312, '', '', 0],
[299, u'\u0d35\u0d3f\u0d24\u0d3e\u0d28\u0d02', 25, 'vithAnam', 'v-v--v--', 8],
[300, u'\u0d35\u0d3f\u0d26\u0d4d\u0d2f\u0d41\u0d24\u0d4d\u0d24\u0d4d', 124, 'vidyuthth', 'vvvvvv--v--v-', 13],
[301, u'\u0d35\u0d3f\u0d26\u0d4d\u0d2f\u0d41\u0d28\u0d4d\u0d2e\u0d3e\u0d32', 17, 'vidyunmAla', '--------', 8],
[302, u'\u0d35\u0d3f\u0d2a\u0d30\u0d40\u0d24\u0d2a\u0d24\u0d4d\u0d25\u0d4d\u0d2f\u0d3e\u0d35\u0d15\u0d4d\u0d24\u0d4d\u0d30\u0d02', 30, 'vipareethapaththhyAvakthram', 'ANUSHTUP', 8],
[303, u'\u0d35\u0d3f\u0d2a\u0d30\u0d40\u0d24\u0d3e\u0d16\u0d4d\u0d2f\u0d3e\u0d28\u0d15\u0d3f', 282, 'vipareethAkhyAnaki', 'AV|v-v--vv-v--|--v--vv-v--|v-v--vv-v--|--v--vv-v--', (11, 11)],
[304, u'\u0d35\u0d3f\u0d2a\u0d41\u0d32\u0d3e\u0d30\u0d4d\u0d2f', 307, '', '', 0],
[305, u'\u0d35\u0d3f\u0d2f\u0d4b\u0d17\u0d3f\u0d28\u0d3f', 278, 'viyOgini', 'AV|vv-vv-v-v-|vv--vv-v-v-|vv-vv-v-v-|vv--vv-v-v-', (10, 11)],
[306, u'\u0d35\u0d3f\u0d32\u0d3e\u0d38\u0d3f\u0d28\u0d3f', 264, 'vilAsini', 'vvvvvvvvvvvv-v--v--v--v-', 24],
[307, u'\u0d35\u0d3f\u0d36\u0d4d\u0d32\u0d4b\u0d15\u0d02', 312, '', '', 0],
[308, u'\u0d35\u0d43\u0d24\u0d4d\u0d24', 72, 'vr^ththa', 'vvvvvvvv---', 11],
[309, u'\u0d35\u0d43\u0d24\u0d4d\u0d24\u0d02', 230, 'vr^ththam', '-v-v-v-v-v-v-v-v-v-v', 20],
[310, u'\u0d35\u0d47\u0d17\u0d35\u0d24\u0d3f', 288, 'vEgavathi', 'AV|vv-vv-vv--|-vv-vv-vv--|vv-vv-vv--|-vv-vv-vv--', (10, 11)],
[311, u'\u0d35\u0d47\u0d23\u0d3f', 8, 'vENi', '--v-', 4],
[312, u'\u0d35\u0d48\u0d24\u0d3e\u0d33\u0d40\u0d2f\u0d02', 313, '', '', 0],
[313, u'\u0d35\u0d48\u0d36\u0d4d\u0d35\u0d26\u0d47\u0d35\u0d3f', 90, 'vaiSvadEvi', '------v--v--', 12],
[314, u'\u0d35\u0d02\u0d36\u0d2a\u0d24\u0d4d\u0d30\u0d2a\u0d24\u0d3f\u0d24\u0d02', 188, 'vamSapathrapathitham', '-vv-v-vvv-vvvvvv-', 17],
[315, u'\u0d35\u0d02\u0d36\u0d2f\u0d37\u0d4d\u0d1f\u0d3f\u0d15', 304, '', '', 0],
[316, u'\u0d35\u0d02\u0d36\u0d38\u0d4d\u0d25\u0d02', 82, 'vamSasthham', 'v-v--vv-v-v-', 12],
[317, u'\u0d35\u0d4d\u0d2f\u0d3e\u0d33\u0d02', 299, '', '', 0],
[318, u'\u0d36\u0d19\u0d4d\u0d15\u0d30\u0d1a\u0d30\u0d3f\u0d24\u0d02', 209, 'Sankaracharitham', 'vv-vvvv-vvvv-vvvv-', 18],
[319, u'\u0d36\u0d36\u0d27\u0d30\u0d2c\u0d3f\u0d02\u0d2c\u0d02', 272, 'SaSadharabimbam', '-vvvvvv-vv-vvvvvv--vvvv--', 25],
[320, u'\u0d36\u0d36\u0d3f\u0d15\u0d32', 158, 'SaSikala', 'vvvvvvvvvvvvvv-', 15],
[321, u'\u0d36\u0d36\u0d3f\u0d15\u0d32', 247, 'SaSikala', '--vvvvvvvv--vvvv-vv--', 21],
[322, u'\u0d36\u0d3e\u0d30\u0d4d\u200d\u200c\u0d26\u0d4d\u0d26\u0d42\u0d32\u0d35\u0d3f\u0d15\u0d4d\u0d30\u0d40\u0d21\u0d3f\u0d24\u0d02', 217, 'SArddoolavikreeDitham', '---vv-v-vvv---v--v-', 19],
[323, u'\u0d36\u0d3e\u0d32\u0d3f\u0d28\u0d3f', 57, 'SAlini', '-----v--v--', 11],
[324, u'\u0d36\u0d3f\u0d16\u0d30\u0d3f\u0d23\u0d3f', 184, 'SikhariNi', 'v-----vvvvv--vvv-', 17],
[325, u'\u0d36\u0d3f\u0d35\u0d02', 4, 'Sivam', 'vv', 2],
[326, u'\u0d36\u0d3f\u0d24\u0d3e\u0d17\u0d4d\u0d30', 333, '', '', 0],
[327, u'\u0d36\u0d41\u0d26\u0d4d\u0d27\u0d35\u0d3f\u0d30\u0d3e\u0d33\u0d4d\u200d', 46, 'SuddhavirAL', '---vv-v-v-', 10],
[328, u'\u0d36\u0d3f\u0d36\u0d41\u0d2d\u0d43\u0d24', 41, 'SiSubhr^tha', 'vvvvvv---', 9],
[329, u'\u0d36\u0d41\u0d26\u0d4d\u0d27\u0d35\u0d3f\u0d30\u0d3e\u0d21\u0d3e\u0d30\u0d4d\u200d\u0d37\u0d2d\u0d02', 296, '', '', 0],
[330, u'\u0d36\u0d41\u0d2d\u0d17\u0d24\u0d3f', 155, 'Subhagathi', 'vv-vvvv-vvvvvv', 14],
[331, u'\u0d36\u0d41\u0d2d\u0d1a\u0d30\u0d3f\u0d24\u0d02', 81, 'Subhacharitham', 'vv-v-vvvvv-', 11],
[332, u'\u0d36\u0d41\u0d2d\u0d1c\u0d3e\u0d24\u0d02', 77, 'SubhajAtham', 'vvvvvv-vv--', 11],
[333, u'\u0d36\u0d48\u0d32\u0d36\u0d3f\u0d16', 171, 'SailaSikha', '-vv-v-vvv-vv-vv-', 16],
[334, u'\u0d36\u0d02\u0d2d\u0d41\u0d28\u0d1f\u0d28\u0d02', 274, 'SambhunaTanam', 'v-vvv-vvv-vvv-vvv-vvv-vvv-', 26],
[335, u'\u0d36\u0d4d\u0d2f\u0d47\u0d28\u0d3f\u0d15', 66, 'SyEnika', '-v-v-v-v-v-', 11],
[336, u'\u0d36\u0d4d\u0d30\u0d35\u0d23\u0d40\u0d2f\u0d02', 202, 'SravaNeeyam', 'vv--vv--vv--vvvv-', 17],
[337, u'\u0d36\u0d4d\u0d30\u0d40', 1, 'Sree', '-', 1],
[338, u'\u0d36\u0d4d\u0d30\u0d40 (\u0d2e\u0d4c\u0d15\u0d4d\u0d24\u0d3f\u0d15\u0d2e\u0d3e\u0d32)', 61, 'Sree (maukthikamAla)', '-vv--vvvv--', 11],
[339, u'\u0d36\u0d4d\u0d30\u0d40\u0d38\u0d26\u0d28\u0d02', 210, 'Sreesadanam', 'vv-vvvvvvvvvv--vv-', 18],
[340, u'\u0d36\u0d4d\u0d32\u0d4b\u0d15\u0d02', 37, '', '', 8],
[341, u'\u0d38\u0d15\u0d32\u0d15\u0d32\u0d02', 166, 'sakalakalam', '----vvvv--vvvv-', 15],
[342, u'\u0d38\u0d2e\u0d3e\u0d28\u0d3f\u0d15', 20, 'samAnika', '-v-v-v-v', 8],
[343, u'\u0d38\u0d2e\u0d3e\u0d38\u0d2e\u0d02', 341, '', '', 0],
[344, u'\u0d38\u0d2e\u0d4d\u0d2e\u0d24', 67, 'sammatha', 'vvv-v--v-v-', 11],
[345, u'\u0d38\u0d2e\u0d4d\u0d2a\u0d41\u0d1f\u0d3f\u0d24\u0d02', 343, '', '', 0],
[346, u'\u0d38\u0d30\u0d38', 126, 'sarasa', 'vv-v-vvv-vv--', 13],
[347, u'\u0d38\u0d30\u0d4b\u0d30\u0d41\u0d39\u0d02', 151, 'sarOruham', 'vvvv-vvvvvv-vv', 14],
[348, u'\u0d38\u0d30\u0d4b\u0d1c\u0d38\u0d2e\u0d02', 261, 'sarOjasamam', '-vv-vv-vv-vv-vv-vv-vv--', 23],
[349, u'\u0d38\u0d30\u0d4d\u200d\u0d2a\u0d4d\u0d2a\u0d3f\u0d23\u0d3f', 340, '', '', 0],
[350, u'\u0d38\u0d32\u0d3f\u0d32\u0d28\u0d3f\u0d27\u0d3f', 243, 'salilanidhi', 'vvvv-v-vvv-vv-vv-v-v-', 21],
[351, u'\u0d38\u0d02\u0d38\u0d3e\u0d30\u0d02', 165, 'samsAram', 'vvvv--vvvv-----', 15],
[352, u'\u0d38\u0d3e\u0d30\u0d35\u0d24\u0d3f', 49, 'sAravathi', '-vv-vv-vv-', 10],
[353, u'\u0d38\u0d3e\u0d30\u0d38\u0d15\u0d32\u0d3f\u0d15', 167, 'sArasakalika', '-----vvvv-vvvv-', 15],
[354, u'\u0d38\u0d3e\u0d30\u0d38\u0d28\u0d2f\u0d28', 177, 'sArasanayana', 'vvvvvv--vvvv----', 16],
[355, u'\u0d38\u0d3f\u0d02\u0d39\u0d35\u0d3f\u0d15\u0d4d\u0d30\u0d3e\u0d28\u0d4d\u0d24\u0d02', 302, '', '', 0],
[356, u'\u0d38\u0d3f\u0d02\u0d39\u0d35\u0d3f\u0d37\u0d4d\u0d2b\u0d42\u0d30\u0d4d\u200d\u200c\u0d1c\u0d4d\u0d1c\u0d3f\u0d24\u0d02', 213, 'simhavishphoor_jjitham', '-------vv---v--v--', 18],
[357, u'\u0d38\u0d3f\u0d02\u0d39\u0d4b\u0d26\u0d4d\u0d27\u0d24 (\u0d35\u0d38\u0d28\u0d4d\u0d24\u0d24\u0d3f\u0d32\u0d15\u0d02)', 139, 'simhOddhatha (vasanthathilakam)', '--v-vvv-vv-v--', 14],
[358, u'\u0d38\u0d3f\u0d02\u0d39\u0d4b\u0d28\u0d4d\u0d28\u0d24 (\u0d35\u0d38\u0d28\u0d4d\u0d24\u0d24\u0d3f\u0d32\u0d15\u0d02)', 139, 'simhOnnatha (vasanthathilakam)', '--v-vvv-vv-v--', 14],
[359, u'\u0d38\u0d41\u0d15\u0d43\u0d24\u0d02', 208, 'sukr^tham', '-vvvv-vvvvvv-vvvv-', 18],
[360, u'\u0d38\u0d41\u0d15\u0d47\u0d38\u0d30\u0d02', 142, 'sukEsaram', 'vvv-v-vvv-v-v-', 14],
[361, u'\u0d38\u0d41\u0d16\u0d15\u0d30\u0d02', 228, 'sukhakaram', 'vvvvvvvvvv-vvvvvv--', 19],
[362, u'\u0d38\u0d41\u0d16\u0d3e\u0d35\u0d39\u0d02', 116, 'sukhAvaham', 'vvv-v-vvv-v-', 12],
[363, u'\u0d38\u0d41\u0d26\u0d24\u0d3f', 114, 'sudathi', '-vvvv-v-vvv-', 12],
[364, u'\u0d38\u0d41\u0d2d\u0d17', 110, 'subhaga', '-vv--vvvvvv-', 12],
[365, u'\u0d38\u0d41\u0d2e\u0d02\u0d17\u0d32', 101, 'sumamgala', 'v-v-vvv-v-v-', 12],
[366, u'\u0d38\u0d41\u0d2e\u0d41\u0d16\u0d3f', 43, 'sumukhi', 'vv-vv-v-v-', 10],
[367, u'\u0d38\u0d41\u0d2e\u0d41\u0d16\u0d3f', 64, 'sumukhi', 'vvvv-vv-vv-', 11],
[368, u'\u0d38\u0d41\u0d32\u0d32\u0d3e\u0d2e\u0d02', 196, 'sulalAmam', 'vvvvvv--vvvv-vv--', 17],
[369, u'\u0d38\u0d41\u0d35\u0d26\u0d28', 231, 'suvadana', '----v--vvvvvv---vvv-', 20],
[370, u'\u0d38\u0d41\u0d36\u0d30\u0d40\u0d30\u0d02', 198, 'suSareeram', 'vvvv-vvvv-vv-vv--', 17],
[371, u'\u0d38\u0d41\u0d37\u0d2e', 50, 'sushama', '--vv---vv-', 10],
[372, u'\u0d38\u0d4c\u0d30\u0d2d\u0d02', 292, 'saurabham', 'AV|vv-v-vvv-v|vvvvv-v-v-|-v-vvv-vv-|vv-v-vvv-v-v-', (10, 10, 10, 13)],
[373, u'\u0d38\u0d4d\u0d24\u0d3f\u0d2e\u0d3f\u0d24', 345, '', '', 0],
[374, u'\u0d38\u0d4d\u0d30\u0d17\u0d4d\u0d26\u0d4d\u0d27\u0d30', 241, 'sragddhara', '----v--vvvvvv--v--v--', 21],
[375, u'\u0d38\u0d4d\u0d30\u0d17\u0d4d\u0d35\u0d3f\u0d23\u0d3f', 89, 'sragviNi', '-v--v--v--v-', 12],
[376, u'\u0d38\u0d4d\u0d35\u0d3e\u0d17\u0d24', 56, 'svAgatha', '-v-vvv-vv--', 11],
[377, u'\u0d38\u0d4d\u0d24\u0d4d\u0d30\u0d40', 3, 'sthree', '--', 2],
[378, u'\u0d39\u0d30\u0d28\u0d30\u0d4d\u200d\u0d24\u0d4d\u0d24\u0d28\u0d02', 205, 'haranar_ththanam', '-v-vvvv-vv---vv-v-', 18],
[379, u'\u0d39\u0d30\u0d3f', 190, 'hari', 'vvvvvv----v-vv-v-', 17],
[380, u'\u0d39\u0d30\u0d3f\u0d23\u0d2a\u0d4d\u0d32\u0d41\u0d24', 283, 'hariNaplutha', 'AV|vv-vv-vv-v-|vvv-vv-vv-v-|vv-vv-vv-v-|vvv-vv-vv-v-', (11, 12)],
[381, u'\u0d39\u0d30\u0d3f\u0d23\u0d2a\u0d4d\u0d32\u0d41\u0d24\u0d02', 214, 'hariNaplutham', '---vv-v-vvvv-vv-v-', 18],
[382, u'\u0d39\u0d30\u0d3f\u0d23\u0d3f', 187, 'hariNi', 'vvvvv-----v-vv-v-', 17],
[383, u'\u0d39\u0d02\u0d38\u0d2a\u0d4d\u0d32\u0d41\u0d24\u0d02', 334, '', '', 0],
[384, u'\u0d39\u0d02\u0d38\u0d2e\u0d3e\u0d32', 16, 'hamsamAla', 'vv--v--', 7],
[385, u'\u0d39\u0d02\u0d38\u0d30\u0d41\u0d24', 24, 'hamsarutha', '---vvv--', 8],	# End of Vruthams
[386, u'\u0d38\u0d1c\u0d38\u0d1c\u0d17', 278, 'sasajaga', 'vv-vv-v-v-', 0],
[387, u'\u0d38\u0d2d\u0d30\u0d32\u0d17', 278, 'sabharalaga', 'vv--vv-v-v-', 0],
[388, u'\u0d38\u0d38\u0d1c\u0d17\u0d17', 279, 'sasajagaga', 'vv-vv-v-v--', 0],
[389, u'\u0d38\u0d2d\u0d30\u0d2f', 279, 'sabharaya', 'vv--vv-v-v--', 0],
[390, u'\u0d28\u0d28\u0d30\u0d2f', 280, 'nanaraya', 'vvvvvv-v-v--', 0],
[391, u'\u0d28\u0d1c\u0d1c\u0d30\u0d17', 280, 'najajaraga', 'vvvv-vv-v-v--', 0],
[392, u'\u0d38\u0d38\u0d38\u0d32\u0d17', 283, 'sasasalaga', 'vv-vv-vv-v-', 0],
[393, u'\u0d28\u0d2d\u0d2d\u0d30', 283, 'nabhabhara', 'vvv-vv-vv-v-', 0],
[394, u'\u0d28\u0d28\u0d30\u0d32\u0d17', 284, 'nanaralaga', 'vvvvvv-v-v-', 0],
[395, u'\u0d28\u0d1c\u0d1c\u0d30', 284, 'najajara', 'vvvv-vv-v-v-', 0],
[396, u'\u0d30\u0d1c\u0d30\u0d1c', 285, 'rajaraja', '-v-v-v-v-v-v', 0],
[397, u'\u0d1c\u0d30\u0d1c\u0d30\u0d17', 285, 'jarajaraga', 'v-v-v-v-v-v--', 0],
[398, u'\u0d2d\u0d2d\u0d2d\u0d17\u0d17', 286, 'bhabhabhagaga', '-vv-vv-vv--', 0],
[399, u'\u0d28\u0d1c\u0d1c\u0d2f', 287, 'najajaya', 'vvvv-vv-vv--', 0],
[400, u'\u0d38\u0d38\u0d38\u0d17', 288, 'sasasaga', 'vv-vv-vv--', 0],
[401, u'\u0d24\u0d1c\u0d30\u0d17', 289, 'thajaraga', '--vv-v-v--', 0],
[402, u'\u0d2e\u0d38\u0d1c\u0d17\u0d17', 289, 'masajagaga', '---vv-v-v--', 0],
[403, u'\u0d38\u0d1c\u0d38\u0d17', 290, 'sajasaga', 'vv-v-vvv--', 0],
[404, u'\u0d2d\u0d30\u0d28\u0d17\u0d17', 290, 'bharanagaga', '-vv-v-vvv--', 0],
[405, u'\u0d38\u0d1c\u0d38\u0d32', 291, 'sajasala', 'vv-v-vvv-v', 0],
[406, u'\u0d28\u0d38\u0d1c\u0d17', 291, 'nasajaga', 'vvvvv-v-v-', 0],
[407, u'\u0d2d\u0d28\u0d1c\u0d32', 291, 'bhanajala', '-vvvvvv-vv', 0],
[408, u'\u0d38\u0d1c\u0d38\u0d1c\u0d17', 291, 'sajasajaga', 'vv-v-vvv-v-v-', 0],
[409, u'\u0d30\u0d28\u0d2d\u0d17', 292, 'ranabhaga', '-v-vvv-vv-', 0],
[410, u'\u0d28\u0d28\u0d38\u0d38', 293, 'nanasasa', 'vvvvvvvv-vv-', 0]]

def vruthamNameList():
	vruthamNames = []
	for x in vruthamTable:
		if x[0] <= 385 and x[2] <= 293 and x[0] != 51:
			vruthamNames.append(x[1] + '[' + str(x[5]) + ']')
	return vruthamNames

def getVruthamId(vruthamName):
	vruthamParts = vruthamName.split('[')
	vruthamName = vruthamParts[0]
	if vruthamParts[1][:-1][0] == '(':
		chandasParts = vruthamParts[1][1:-2].split(',')
		if len(chandasParts) == 2:
			chandas = int(chandasParts[0]), int(chandasParts[1])
		else:
			chandas = int(chandasParts[0]), int(chandasParts[1]), int(chandasParts[2]), int(chandasParts[3])
	else:
		chandas = int(vruthamParts[1][:-1])
	for x in vruthamTable:
		if x[1] == vruthamName and x[5] == chandas:
			return x[0]
	return -1

def getVruthamLakshanam(vruthamName):
	vruthamParts = vruthamName.split('[')
	vruthamName = vruthamParts[0]
	if vruthamParts[1][:-1][0] == '(':
		chandasParts = vruthamParts[1][1:-2].split(',')
		if len(chandasParts) == 2:
			chandas = int(chandasParts[0]), int(chandasParts[1])
		else:
			chandas = int(chandasParts[0]), int(chandasParts[1]), int(chandasParts[2]), int(chandasParts[3])
	else:
		chandas = int(vruthamParts[1][:-1])
	for x in vruthamTable:
		if x[1] == vruthamName and x[5] == chandas:
			return x[4]
	return ''

checkLabel = u'\u0d2a\u0d30\u0d3f\u0d36\u0d4b\u0d27\u0d3f\u0d15\u0d4d\u0d15\u0d42'
checkVruthamLabel = u'\u0d35\u0d43\u0d24\u0d4d\u0d24\u0d02 \u0d2a\u0d30\u0d3f\u0d36\u0d4b\u0d27\u0d3f\u0d15\u0d4d\u0d15\u0d42'
clearAreYouSureLabel = u'\u0d2a\u0d26\u0d4d\u0d2f\u0d02 \u0d2e\u0d3e\u0d2f\u0d4d\u0d15\u0d4d\u0d15\u0d1f\u0d4d\u0d1f\u0d47 ?'
clearLabel = u'\u0d2e\u0d3e\u0d2f\u0d4d\u0d15\u0d4d\u0d15\u0d42'
closeLabel = u'\u0d05\u0d1f\u0d2f\u0d4d\u0d15\u0d4d\u0d15\u0d42'
dontKnowVruthamLabel = u'\u0d08 \u0d35\u0d43\u0d24\u0d4d\u0d24\u0d24\u0d4d\u0d24\u0d3f\u0d28\u0d4d\u0d31\u0d46 \u0d2a\u0d47\u0d30\u0d4d\u200d\u200c \u0d05\u0d31\u0d3f\u0d2f\u0d3f\u0d32\u0d4d\u0d32'
emptySylLabel = u'\u0d07\u0d35\u0d3f\u0d1f\u0d46 \u0d05\u0d15\u0d4d\u0d37\u0d30\u0d02 \u0d35\u0d47\u0d23\u0d02'
enterPadyamLabel = u'\u0d07\u0d35\u0d3f\u0d1f\u0d46 \u0d2a\u0d26\u0d4d\u0d2f\u0d02 \u0d0e\u0d34\u0d41\u0d24\u0d42:'
extraSylLabel = u'\u0d08 \u0d05\u0d15\u0d4d\u0d37\u0d30\u0d02 \u0d05\u0d27\u0d3f\u0d15\u0d2e\u0d3e\u0d23\u0d41\u0d4d'
findLabel = u'\u0d15\u0d23\u0d4d\u0d1f\u0d41\u0d2a\u0d3f\u0d1f\u0d3f\u0d15\u0d4d\u0d15\u0d42'
findVruthamLabel = u'\u0d35\u0d43\u0d24\u0d4d\u0d24\u0d02 \u0d15\u0d23\u0d4d\u0d1f\u0d41\u0d2a\u0d3f\u0d1f\u0d3f\u0d15\u0d4d\u0d15\u0d42'
ganamLabel = u'\u0d17\u0d23\u0d02'
givePadyamInMalLabel = u'\u0d2a\u0d26\u0d4d\u0d2f\u0d02 \u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02 \u0d2f\u0d41\u0d28\u0d40\u0d15\u0d4b\u0d21\u0d4d \u0d09\u0d2a\u0d2f\u0d4b\u0d17\u0d3f\u0d1a\u0d4d\u0d1a\u0d41\u0d4d \u0d0e\u0d34\u0d41\u0d24\u0d42 !!!'
guruLabel = u'\u0d17\u0d41\u0d30\u0d41'
iDontKnowLabel = u'\u0d05\u0d31\u0d3f\u0d2f\u0d3f\u0d32\u0d4d\u0d32'
laghuLabel = u'\u0d32\u0d18\u0d41'
lineLabel = u'\u0d35\u0d30\u0d3f'
lineVruthamGanangalLabel = u'\u0d35\u0d30\u0d3f\u0d2f\u0d41\u0d1f\u0d46 \u0d35\u0d43\u0d24\u0d4d\u0d24\u0d02/\u0d17\u0d23\u0d19\u0d4d\u0d19\u0d33\u0d4d\u200d'
noPadyamGivenLabel = u'\u0d2a\u0d26\u0d4d\u0d2f\u0d02 \u0d12\u0d28\u0d4d\u0d28\u0d41\u0d02 \u0d15\u0d3e\u0d23\u0d41\u0d28\u0d4d\u0d28\u0d3f\u0d32\u0d4d\u0d32\u0d32\u0d4d\u0d32\u0d4b !!!'
noVruthamGivenLabel = u'\u0d0f\u0d24\u0d41 \u0d35\u0d43\u0d24\u0d4d\u0d24\u0d02 \u0d2a\u0d30\u0d3f\u0d36\u0d4b\u0d27\u0d3f\u0d15\u0d4d\u0d15\u0d23\u0d2e\u0d46\u0d28\u0d4d\u0d28\u0d41\u0d4d \u0d24\u0d3f\u0d30\u0d1e\u0d4d\u0d1e\u0d46\u0d1f\u0d41\u0d15\u0d4d\u0d15\u0d42 !!!'
pleaseConfirmLabel = u'\u0d09\u0d31\u0d2a\u0d4d\u0d2a\u0d3e\u0d15\u0d4d\u0d15\u0d42'
quitAreYouSureLabel = u'\u0d35\u0d43\u0d24\u0d4d\u0d24\u0d38\u0d39\u0d3e\u0d2f\u0d3f \u0d35\u0d3f\u0d1f\u0d4d\u0d1f\u0d41 \u0d2a\u0d4b\u0d15\u0d23\u0d2e\u0d46\u0d28\u0d4d\u0d28\u0d41\u0d4d \u0d09\u0d31\u0d2a\u0d4d\u0d2a\u0d3e\u0d23\u0d4b ?'
rightLabel = u'\u0d36\u0d30\u0d3f'
seeResultsHereLabel = u'\u0d07\u0d35\u0d3f\u0d1f\u0d46 \u0d2b\u0d32\u0d02 \u0d15\u0d3e\u0d23\u0d3e\u0d02:'
selectVruthamLabel = u'\u0d0f\u0d24\u0d41\u0d4d \u0d35\u0d43\u0d24\u0d4d\u0d24\u0d02 \u0d28\u0d4b\u0d15\u0d4d\u0d15\u0d23\u0d02\u200c ?'
slokamLabel = u'\u0d36\u0d4d\u0d32\u0d4b\u0d15\u0d02'
slokamsVruthamLabel = u'\u0d36\u0d4d\u0d32\u0d4b\u0d15\u0d24\u0d4d\u0d24\u0d3f\u0d28\u0d4d\u0d31\u0d46 \u0d35\u0d43\u0d24\u0d4d\u0d24\u0d02'
slokaVruthamLabel = u'\u0d36\u0d4d\u0d32\u0d4b\u0d15\u0d35\u0d43\u0d24\u0d4d\u0d24\u0d02'
syllableCountLabel = u'\u0d05\u0d15\u0d4d\u0d37\u0d30\u0d02'
thisIsCorrectLabel = u'\u0d08 \u0d05\u0d15\u0d4d\u0d37\u0d30\u0d02 \u0d36\u0d30\u0d3f\u0d2f\u0d3e\u0d23\u0d41\u0d4d'
thisLineIsCorrectLabel = u'\u0d08 \u0d35\u0d30\u0d3f \u0d36\u0d30\u0d3f\u0d2f\u0d3e\u0d23\u0d41\u0d4d'
thisLineIsWrongLabel = u'\u0d08 \u0d35\u0d30\u0d3f \u0d24\u0d46\u0d31\u0d4d\u0d31\u0d3e\u0d23\u0d41\u0d4d'
vruthaSahayiLabel = u'\u0d35\u0d43\u0d24\u0d4d\u0d24\u0d38\u0d39\u0d3e\u0d2f\u0d3f'
whatToDoLabel = u'\u0d0e\u0d28\u0d4d\u0d24\u0d3e\u0d23\u0d41\u0d4d \u0d1a\u0d46\u0d2f\u0d4d\u0d2f\u0d47\u0d23\u0d4d\u0d1f\u0d24\u0d41\u0d4d ?'
wrongGanamLabel = u'\u0d08 \u0d17\u0d23\u0d02 \u0d07\u0d35\u0d3f\u0d1f\u0d46 \u0d24\u0d46\u0d31\u0d4d\u0d31\u0d3e\u0d23\u0d41\u0d4d'
wrongLabel = u'\u0d24\u0d46\u0d31\u0d4d\u0d31\u0d4d'
wronglyPlacedGuruLabel = u'\u0d07\u0d35\u0d3f\u0d1f\u0d46 \u0d32\u0d18\u0d41\u0d35\u0d3e\u0d23\u0d41\u0d4d \u0d35\u0d47\u0d23\u0d4d\u0d1f\u0d24\u0d4d'
wronglyPlacedLaghuLabel = u'\u0d07\u0d35\u0d3f\u0d1f\u0d46 \u0d17\u0d41\u0d30\u0d41\u0d35\u0d3e\u0d23\u0d41\u0d4d \u0d35\u0d47\u0d23\u0d4d\u0d1f\u0d24\u0d4d'
yathiBhangamLabel = u'\u0d2a\u0d15\u0d4d\u0d37\u0d47 \u0d2f\u0d24\u0d3f\u0d2d\u0d02\u0d17\u0d02'
yathiRequiredLabel = u'\u0d08 \u0d05\u0d15\u0d4d\u0d37\u0d30\u0d24\u0d4d\u0d24\u0d3f\u0d28\u0d41 \u0d2e\u0d41\u0d28\u0d4d\u200d\u200c\u0d2a\u0d47 \u0d2f\u0d24\u0d3f \u0d35\u0d47\u0d23\u0d02'

aboutName = 'Vrutha Sahayi'
aboutVersion = '0.1'
aboutDescription = 'A utility to find/check the "vrutham" (metrics) of a given Malayalam poem'
aboutDevelopers = ['Sushen V Kumar','Sanjeev Kozhisseri']
aboutCopyright = 'Copyright (C) 2007 Sushen V Kumar\nCopyright (C) 2007 Sanjeev Kozhisseri'
aboutWebSite = 'http://vruthasahayi.sourceforge.net'
aboutLicense = 'Vrutha Sahayi is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.\n\nVrutha Sahayi is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License along with Vrutha Sahayi; if not, write to the, Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA'
