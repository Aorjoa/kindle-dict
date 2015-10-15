#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Script for conversion of Stardict tabfile (<header>\t<definition>
# per line) into the OPF file for MobiPocket Dictionary
#
# For usage of dictionary convert it by:
# (wine) mobigen.exe DICTIONARY.opf
#
# MobiPocket Reader at: www.mobipocket.com for platforms:
#   PalmOs, Windows Mobile, Symbian (Series 60, Series 80, 90, UIQ), Psion, Blackberry, Franklin, iLiad (by iRex), BenQ-Siemens, Pepper Pad..
#   http://www.mobipocket.com/en/DownloadSoft/DownloadManualInstall.asp
# mobigen.exe available at:
#   http://www.mobipocket.com/soft/prcgen/mobigen.zip
#
# Copyright (C) 2007 - Klokan Petr Přidal (www.klokan.cz)
#

###################################
# Bhuridech Sudsee improve script #
###################################
# สงวนลิขสิทธิ์ พ.ศ. 2546 โดยศูนย์เทคโนโลยีอิเล็กทรอนิกส์และคอมพิวเตอร์แห่งชาติ
# ข้อตกลงการอนุญาตใช้สิทธิ์ (LICENSE AGREEMENT)

# ข้อตกลงการอนุญาตใช้สิทธิ์ หมายถึง ข้อตกลงทางกฎหมายระหว่างผู้ใช้และศูนย์ฯ 
# กรุณาอ่านรายละเอียดของข้อตกลงนี้ก่อนเป็น "ผู้ใช้" เพื่อใช้ประโยชน์จากซอฟต์แวร์
# พจนานุกรมอิเล็กทรอนิกส์นี้ สาระสำคัญของข้อตกลงการอนุญาตใช้สิทธิ์ฉบับนี้ประกอบด้วย 
# ข้อความสงวนลิขสิทธิ์ (Copyright Notice) คำนิยาม (Definitions) การยอมรับข้อ
# ตกลงการอนุญาตใช้สิทธิ์ (Acceptance of License Agreement) เงื่อนไขการใช้ 
# (Terms of Use) และข้อสงวนสิทธิ์การรับประกัน (Disclaimer of Warranty) 

# 1. คำนิยาม (Definitions)
# (ก) "ศูนย์ฯ" หมายถึง ศูนย์เทคโนโลยีอิเล็กทรอนิกส์และคอมพิวเตอร์แห่งชาติ 
# สำนักงานพัฒนาวิทยาศาสตร์และเทคโนโลยี ภายใต้การกำกับดูแลของกระทรวงวิทยาศาสตร์และเทคโนโลยี
# (ข) "พจนานุกรมเล็กซิตรอน" หรือ "LEXiTRON" หมายถึง โปรแกรมคอมพิวเตอร์
# และข้อมูลพจนานุกรมอิเล็กทรอนิกส์ที่พัฒนาโดยศูนย์ฯ และให้หมายความรวมถึง
# โปรแกรมคอมพิวเตอร์และข้อมูลอื่นที่ศูนย์ฯ เผยแพร่ด้วย
# (ค) "บริการ" หมายถึง การเข้าถึงสาระต่างๆ ที่ปรากฏบนเครือข่ายเว็บไซต์ของศูนย์ฯ 
# เครื่องมืออำนวยความสะดวก (Tools) การ Downloadโปรแกรมคอมพิวเตอร์ 
# การสื่อสารและให้ข้อมูลสารสนเทศ การปรับปรุงเพิ่มเติม การเพิ่มสมรรถนะ การเพิ่มเติมลักษณะ 
# การใช้งาน และ/หรือสิ่งต่างๆ ที่ทำขึ้นใหม่ตามที่ปรากฏในเว็บไซต์
# (ง) "เงื่อนไขการใช้" หมายถึง ข้อความบังคับที่ระบุไว้สำหรับผู้หนึ่งผู้ใดที่ใช้ประโยชน์จากพจนานุกรมเล็กซิตรอน
# (จ) "ผู้ใช้" หมายถึง ผู้ใช้ประโยชน์จากพจนานุกรมเล็กซิตรอน  เพื่อการนำไปใช้งาน   
# การนำไปดัดแปลง การปรับปรุงเพิ่มเติม การเพิ่มสมรรถนะและการนำไปใช้ประโยชน์ในเชิงพาณิชย์
# (ฉ) "รหัสต้นฉบับ" หมายถึง โปรแกรมคอมพิวเตอร์หรือข้อมูลต้นฉบับ (Source Code) 
# ที่พัฒนาขึ้นในรูปแบบที่สามารถนำไปปรับปรุงพัฒนาต่อได้ โดยทั่วไปโปรแกรมคอมพิวเตอร์ในรูปแบบ
# รหัสต้นฉบับต้องผ่านกระบวนการแปลงเป็นโปรแกรมคอมพิวเตอร์ในรูปแบบไบนารีก่อนจึงสามารถนำไปใช้ได้
# (ช) "รูปแบบไบนารี" หมายถึง โปรแกรมคอมพิวเตอร์หรือข้อมูลที่ถูกแปลงให้อยู่ในรูปแบบที่คอมพิวเตอร์
# หรือโปรแกรมคอมพิวเตอร์เข้าใจ (Binary Form) เพื่อทำให้นำไปใช้งานได้ทันที

# 2. การยอมรับข้อตกลงการอนุญาตใช้สิทธิ์
# ศูนย์ฯ สงวนสิทธิ์ในการปรับปรุงแก้ไข "ข้อตกลงการอนุญาตใช้สิทธิ์" เมื่อใดก็ตามที่ศูนย์ฯ เห็นสมควรโดยไม่ต้องบอกกล่าวล่วงหน้า

# 3. เงื่อนไขการใช้
# การเผยแพร่ต่อและการใช้พจนานุกรมเล็กซิตรอน ทั้งในรูปแบบรหัสต้นฉบับ และรูปแบบไบนารี 
# ไม่ว่าจะมีการแก้ไขดัดแปลงหรือไม่ก็ตาม สามารถกระทำได้ภายใต้เงื่อนไข ดังนี้
# (ก) หากต้องการเผยแพร่พจนานุกรมเล็กซิตรอนต่อไปในรูปแบบรหัสต้นฉบับ (Source Code) 
# ต้องคงไว้ซึ่งข้อความสงวนลิขสิทธิ์ การยอมรับข้อตกลงการอนุญาตใช้สิทธิ์ เงื่อนไขการใช้ และข้อสงวนสิทธิ์การรับประกัน
# (ข) หากต้องการเผยแพร่พจนานุกรมเล็กซิตรอนต่อไปในรูปแบบไบนารี (Binary Form)       
# ต้องคัดลอกข้อความสงวนลิขสิทธิ์ การยอมรับข้อตกลงการอนุญาตใช้สิทธิ์ เงื่อนไขการใช้ 
# และข้อสงวนสิทธิ์การรับประกันไว้ในเอกสาร และ/หรือสื่อที่ใช้ในการเผยแพร่ด้วย
# (ค) ถ้าผู้ใช้ได้สร้างสรรค์ผลิตภัณฑ์ที่มีส่วนหนึ่งส่วนใดดัดแปลงมาจากพจนานุกรมเล็กซิตรอน 
# และนำไปเผยแพร่ต่อไป ผู้ใช้ต้องแสดงข้อความให้ปรากฏในผลิตภัณฑ์นั้น ดังนี้
# "ผลิตภัณฑ์นี้สร้างสรรค์ขึ้นโดยดัดแปลงมาจากพจนานุกรมเล็กซิตรอนซึ่งพัฒนาโดย
# ศูนย์เทคโนโลยีอิเล็กทรอนิกส์และคอมพิวเตอร์แห่งชาติ (http://www.nectec.or.th)" 
# (ง) ผลิตภัณฑ์ที่สร้างสรรค์ขึ้นโดยมีส่วนหนึ่งส่วนใดดัดแปลงมาจากพจนานุกรมเล็กซิตรอน 
# ต้องไม่ใช้ชื่อภาษาไทยว่า "เล็กซิตรอน" หรือชื่อภาษาอังกฤษ "LEXiTRON" และ/หรือนำชื่อภาษาไทย
# และ/หรือภาษาอังกฤษดังกล่าวไปเป็นส่วนหนึ่งของชื่อ เว้นแต่จะได้รับอนุญาตเป็นลายลักษณ์อักษรจากศูนย์ฯ ก่อน
# (จ) ผู้ใช้ต้องไม่นำพจนานุกรมเล็กซิตรอนไปใช้ในทางที่น่าจะก่อให้เกิดความเสียหายแก่ศูนย์ฯ 
# หรือบุคคลภายนอก ศูนย์ฯ สงวนสิทธิ์ในการเรียกร้องค่าสินไหมทดแทน ค่าทนายความ 
# ค่าธรรมเนียมในการดำเนินคดีและบังคับคดี และค่าใช้จ่ายต่างๆ ที่เกิดขึ้นจากการกระทำของผู้ใช้เช่นว่านั้น
# (ฉ) ห้ามกล่าวอ้างชื่อศูนย์ฯ/สำนักงานพัฒนาวิทยาศาสตร์และเทคโนโลยีแห่งชาติ (สวทช.) 
# และชื่อผู้สนับสนุนของศูนย์ฯ ในการรับรองหรือประชาสัมพันธ์ผลิตภัณฑ์ที่สร้างสรรค์ขึ้น
# โดยอาศัยพจนานุกรมเล็กซิตรอนเป็นส่วนประกอบ เว้นแต่จะได้รับอนุญาตเป็นลายลักษณ์อักษรจากศูนย์ฯ ก่อน

# 4. ข้อสงวนสิทธิ์การรับประกัน
# พจนานุกรมเล็กซิตรอน ข้อมูล สาระ สื่อ หรือผลิตภัณฑ์ทั้งหมดที่ศูนย์ฯ ได้ให้บริการหรือเผยแพร่ 
# ถือเป็นงานอันมีลิขสิทธิ์ของศูนย์ฯ ทั้งนี้ พจนานุกรมเล็กซิตรอน ข้อมูล สาระ สื่อ หรือผลิตภัณฑ์ที่ศูนย์ฯ 
# หรือผู้สนับสนุนจัดให้บริการหรือเผยแพร่นั้น จะเป็นไปตามรูปแบบที่ปรากฏอยู่ (AS IS) 
# และรูปแบบที่จัดให้ใช้ประโยชน์ (AS AVAILABLE)   ดังนั้นศูนย์ฯ ขอสงวนสิทธิ์ทั้ง
# โดยชัดเจนและโดยปริยาย และไม่จำกัดเฉพาะกรณีที่ระบุไว้ ในการไม่รับประกันผลประโยชน์
# ในทางการค้าหรือความเหมาะสมกับวัตถุประสงค์การใช้งาน ไม่ว่ากรณีใดๆ ศูนย์ฯ หรือผู้สนับสนุน
# จะไม่รับผิดชอบ ไม่ว่าโดยตรงหรือโดยอ้อม ในค่าเสียหายอันเนื่องมาจากการผิดสัญญา 
# ค่าเสียหายจำเพาะ ค่าเสียหายตามความเป็นจริง หรือความเสียหายต่อเนื่อง และไม่จำกัดเฉพาะ
# การจัดหาของหรือบริการแทน การสูญเสียประโยชน์ในการใช้ข้อมูล การสูญเสียผลประโยชน
# หรือธุรกิจหยุดชะงัก ไม่ว่าจะเป็นเหตุโดยทฤษฎีของความรับผิดในเรื่องสัญญา ความรับผิดโดยเด็ดขาด 
# หรือละเมิด (รวมถึงความประมาทเลินเล่อหรือประการอื่น)  ซึ่งเกิดขึ้นจากการใช้พจนานุกรม
# เล็กซิตรอน ข้อมูล สาระ สื่อ หรือผลิตภัณฑ์นั้น   ไม่ว่าจะมีการแนะนำถึงความเป็นไปได้ในการ
# เกิดความเสียหายเช่นว่านั้นไว้แล้วหรือไม่ก็ตาม

#
# Version history:
# 0.1 (19.7.2007) Initial version
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

# VERSION
VERSION = "0.1"

# FILENAME is a first parameter on the commandline now

import sys
import re
import os

from unicodedata import normalize, decomposition, combining
import string
from exceptions import UnicodeEncodeError

# Hand-made table from PloneTool.py
mapping_custom_1 =  {
138: 's', 142: 'z', 154: 's', 158: 'z', 159: 'Y' }

# UnicodeData.txt does not contain normalization of Greek letters.
mapping_greek = {
912: 'i', 913: 'A', 914: 'B', 915: 'G', 916: 'D', 917: 'E', 918: 'Z',
919: 'I', 920: 'TH', 921: 'I', 922: 'K', 923: 'L', 924: 'M', 925: 'N',
926: 'KS', 927: 'O', 928: 'P', 929: 'R', 931: 'S', 932: 'T', 933: 'Y',
934: 'F', 936: 'PS', 937: 'O', 938: 'I', 939: 'Y', 940: 'a', 941: 'e',
943: 'i', 944: 'y', 945: 'a', 946: 'b', 947: 'g', 948: 'd', 949: 'e',
950: 'z', 951: 'i', 952: 'th', 953: 'i', 954: 'k', 955: 'l', 956: 'm',
957: 'n', 958: 'ks', 959: 'o', 960: 'p', 961: 'r', 962: 's', 963: 's',
964: 't', 965: 'y', 966: 'f', 968: 'ps', 969: 'o', 970: 'i', 971: 'y',
972: 'o', 973: 'y' }

# This may be specific to German...
mapping_two_chars = {
140 : 'O', 156: 'o', 196: 'A', 246: 'o', 252: 'u', 214: 'O',
228 : 'a', 220: 'U', 223: 's', 230: 'e', 198: 'E' }

mapping_latin_chars = {
192 : 'A', 193 : 'A', 194 : 'A', 195 : 'a', 197 : 'A', 199 : 'C', 200 : 'E',
201 : 'E', 202 : 'E', 203 : 'E', 204 : 'I', 205 : 'I', 206 : 'I', 207 : 'I',
208 : 'D', 209 : 'N', 210 : 'O', 211 : 'O', 212 : 'O', 213 : 'O', 215 : 'x',
216 : 'O', 217 : 'U', 218 : 'U', 219 : 'U', 221 : 'Y', 224 : 'a', 225 : 'a',
226 : 'a', 227 : 'a', 229 : 'a', 231 : 'c', 232 : 'e', 233 : 'e', 234 : 'e',
235 : 'e', 236 : 'i', 237 : 'i', 238 : 'i', 239 : 'i', 240 : 'd', 241 : 'n',
242 : 'o', 243 : 'o', 244 : 'o', 245 : 'o', 248 : 'o', 249 : 'u', 250 : 'u',
251 : 'u', 253 : 'y', 255 : 'y' }

# Feel free to add new user-defined mapping. Don't forget to update mapping dict
# with your dict.

mapping = {}
mapping.update(mapping_custom_1)
mapping.update(mapping_greek)
mapping.update(mapping_two_chars)
mapping.update(mapping_latin_chars)

# On OpenBSD string.whitespace has a non-standard implementation
# See http://plone.org/collector/4704 for details
whitespace = ''.join([c for c in string.whitespace if ord(c) < 128])
allowed = string.ascii_letters + string.digits + string.punctuation + whitespace

def normalizeUnicode(text, encoding='humanascii'):
    """
    This method is used for normalization of unicode characters to the base ASCII
    letters. Output is ASCII encoded string (or char) with only ASCII letters,
    digits, punctuation and whitespace characters. Case is preserved.
    """
    unicodeinput = True
    if not isinstance(text, unicode):
        text = unicode(text, 'utf-8')
        unicodeinput = False

    res = ''
    global allowed
    if encoding == 'humanascii':
        enc = 'ascii'
    else:
        enc = encoding
    for ch in text:
        if (encoding == 'humanascii') and (ch in allowed):
            # ASCII chars, digits etc. stay untouched
            res += ch
            continue
        else:
            try:
                ch.encode(enc,'strict')
                res += ch
            except UnicodeEncodeError:
                ordinal = ord(ch)
                if mapping.has_key(ordinal):
                    # try to apply custom mappings
                    res += mapping.get(ordinal)
                elif decomposition(ch) or len(normalize('NFKD',ch)) > 1:
                    normalized = filter(lambda i: not combining(i), normalize('NFKD', ch)).strip()
                    # normalized string may contain non-letter chars too. Remove them
                    # normalized string may result to  more than one char
                    res += ''.join([c for c in normalized if c in allowed])
                else:
                    # hex string instead of unknown char
                    res += "%x" % ordinal
    if unicodeinput:
        return res
    else:
        return res.encode('utf-8')

OPFTEMPLATEHEAD1 = """<?xml version="1.0"?><!DOCTYPE package SYSTEM "oeb1.ent">

<!-- the command line instruction 'prcgen dictionary.opf' will produce the dictionary.prc file in the same folder-->
<!-- the command line instruction 'mobigen dictionary.opf' will produce the dictionary.mobi file in the same folder-->

<package unique-identifier="uid" xmlns:dc="Dublin Core">

<metadata>
	<dc-metadata>
		<dc:Identifier id="uid">%s</dc:Identifier>
		<!-- Title of the document -->
		<dc:Title><h2>%s</h2></dc:Title>
		<dc:Language>EN</dc:Language>
	</dc-metadata>
	<x-metadata>
"""
OPFTEMPLATEHEADNOUTF = """		<output encoding="Windows-1252" flatten-dynamic-dir="yes"/>"""
OPFTEMPLATEHEAD2 = """
		<DictionaryInLanguage>en-us</DictionaryInLanguage>
		<DictionaryOutLanguage>en-us</DictionaryOutLanguage>
	</x-metadata>
</metadata>

<!-- list of all the files needed to produce the .prc file -->
<manifest>
"""

OPFTEMPLATELINE = """ <item id="dictionary%d" href="%s%d.html" media-type="text/x-oeb1-document"/>
"""

OPFTEMPLATEMIDDLE = """</manifest>


<!-- list of the html files in the correct order  -->
<spine>
"""

OPFTEMPLATELINEREF = """	<itemref idref="dictionary%d"/>
"""

OPFTEMPLATEEND = """</spine>

<tours/>
<guide> <reference type="search" title="Dictionary Search" onclick= "index_search()"/> </guide>
</package>
"""

################################################################
# MAIN
################################################################

UTFINDEX = False
if len(sys.argv) > 1:
    FILENAME = sys.argv[1]
    if sys.argv[1] == '-utf':
        UTFINDEX = True
        FILENAME = sys.argv[2]
    else:
        FILENAME = sys.argv[1]
else:
    print "tab2opf (Stardict->MobiPocket)"
    print "------------------------------"
    print "Version: %s" % VERSION
    print "Copyright (C) 2007 - Klokan Petr Pridal"
    print
    print "Usage: python tab2opf.py [-utf] DICTIONARY.tab"
    print
    print "ERROR: You have to specify a .tab file"
    sys.exit(1)

fr = open(FILENAME,'rb')
name = os.path.splitext(os.path.basename(FILENAME))[0]

i = 0
to = False

for r in fr.xreadlines():
   
    if i % 10000 == 0:
        if to:
            to.write("""
                </mbp:frameset>
              </body>
            </html>
            """)
            to.close()
        to = open("%s%d.html" % (name, i / 10000), 'w')

        to.write("""<?xml version="1.0" encoding="utf-8"?>
<html xmlns:idx="www.i-aor.com" xmlns:mbp="www.i-aor.com" xmlns:xlink="http://www.w3.org/1999/xlink">
  <body>
    <mbp:pagebreak/>
    <mbp:frameset>
      <mbp:slave-frame display="bottom" device="all" breadth="auto" leftmargin="0" rightmargin="0" bottommargin="0" topmargin="0">
      </mbp:slave-frame>
      <mbp:pagebreak/>
""")
    try:
        dt, dd =  r.split('\t',1)
        if not UTFINDEX:
            dt = normalizeUnicode(dt,'cp1252')
            dd = normalizeUnicode(dd,'cp1252')
        dtstrip = normalizeUnicode( dt )
        dd = dd.replace("\\\\","\\").replace("\\n","<br/>\n")
        to.write("""      <idx:entry name="word" scriptable="yes">
            <h2>
              <idx:orth>%s</idx:orth><idx:key key="%s">
            </h2>
            <h3> %s </h3>
          </idx:entry>
          <mbp:pagebreak/>
    """ % (dt, dtstrip, dd))
        #print dt
        i += 1
    except ValueError:
        pass
to.write("""
    </mbp:frameset>
  </body>
</html>
""")
to.close()
fr.close()
lineno = i - 1

to = open("%s.opf" % name, 'w')
to.write(OPFTEMPLATEHEAD1 % (name, name))
if not UTFINDEX:
    to.write(OPFTEMPLATEHEADNOUTF)
to.write(OPFTEMPLATEHEAD2)
for i in range(0,(lineno/10000)+1):
    to.write(OPFTEMPLATELINE % (i, name, i))
to.write(OPFTEMPLATEMIDDLE)
for i in range(0,(lineno/10000)+1):
    to.write(OPFTEMPLATELINEREF % i)
to.write(OPFTEMPLATEEND)
