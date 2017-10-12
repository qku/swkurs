#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import time

tplist=[]

from xml.sax.handler import ContentHandler
class GPXHandler(ContentHandler):
    #A handler to deal with articles in XML
    name = ""
    inTrkPt = 0
    tpinfo = {}

    def startElement(self, name, attrs):
        # print "startElement", name
        if name == "trkpt":
            lat = attrs.get("lat","")
            lon = attrs.get("lon","")
            self.tpinfo["lat"] = lat
            self.tpinfo["lon"] = lon
            self.inTrkPt = 1
        elif self.inTrkPt:
            self.name = name

    def characters(self, characters):
        # print "characters", characters

        if self.inTrkPt and self.name != None and len(self.name)>0 :
            self.tpinfo[self.name] = characters
            
            # print self.name, characters

    def endElement(self, name):
        namlist=[ "lat", "lon", "ele", "time", "gpxtpx:hr" ]

        # print "endElement", name
        self.name = None
        if name == "trkpt":
            self.inTrkPt = 0
#           print self.tpinfo

            for nam in namlist:
                
                try:
                    print nam, ' = ',  self.tpinfo[nam], " , " ,
                except:
                    print "None", " , "  ,


            tplist.append( self.tpinfo )
            self.tpinfo = {}



from xml.sax import make_parser

global tnow
tnow = time.localtime()

ch = GPXHandler()
saxparser = make_parser()
saxparser.setContentHandler(ch)
saxparser.parse("GPS_example.gpx")

ntp = len(tplist)

print ntp, " Trackpunkte gefunden"

import gpxutil

# store info in straight arrays: ele == Hoehe
ea, hra, lata, longa, datea, vela = [], [], [], [], [], []

for tp in tplist:
	ea.append(float(tp["ele"]))
	hra.append(float(tp["gpxtpx:hr"]))
	lata.append(float(tp["lat"]))
	longa.append(float(tp["lon"]))
	datea.append(gpxutil.parsedate(tp["time"]))
	print tp["time"]

		
# calculate velocities
for i in range(ntp-1):
	distance, a, b = gpxutil.distance(lata[i], longa[i], lata[i+1], longa[i+1])
	try:
		diff = float(gpxutil.timediff(datea[i+1], datea[i]))
	except:
		print "trouble calculating diff"
	vela.append(distance/diff)
	print diff

# plotting
import pylab as pl

fig = pl.figure()

e = fig.add_subplot(311)
#e.title('Hoehenprofil')
e.plot(range(ntp), ea)

v = fig.add_subplot(312)
#h.title('Geschwindigkeit')
v.plot(range(ntp), vela, "green")

h = fig.add_subplot(313)
#h.title('Herzfrequenz')
h.plot(range(ntp), hra, "red")

pl.show()


# <gpx xmlns="http://www.topografix.com/GPX/1/1"
# ... 
# <trk><name>GPX-example</name>
# <extensions><gpxx:TrackExtension>
# <gpxx:DisplayColor>Blue</gpxx:DisplayColor>
# </gpxx:TrackExtension></extensions>
# <trkseg>
# <trkpt lat="47.5788825285" lon="10.5603028927">
# <ele>865.32</ele>
# <time>2014-06-15T08:02:21Z</time>
# <extensions><gpxtpx:TrackPointExtension>
# <gpxtpx:hr>68</gpxtpx:hr></gpxtpx:TrackPointExtension></extensions>
# </trkpt>
# ...


# p.Parse(sexam,1)

