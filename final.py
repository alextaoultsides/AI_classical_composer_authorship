import csv
import glob
import re
'''
title slide
intro(story) differences beethoven, haydn, Mozart.  Influences of Mozart and haydn
results

'''

def main():
	C = ComposerAuth()
		
			
				
			


class ComposerAuth(object):
	
	def __init__(self):
		
		
		self.All = {}
		self.check = 0
		lists = glob.glob('*/*')
		for nextsub in lists:
			print nextsub
			self.read(nextsub)
		self.initAll()
		self.finalCSV()
	def read(self,compcsv):
		chordMaker = {}
		chord = []
		style = {}
		
		with open(compcsv, 'rb') as csvfile:
			csvreader = csv.reader(csvfile, delimiter=',')
			for row in csvreader:
				
				if row[0] == "NoteOn":
					
					if row[2] in chordMaker:
						i += 1
						chordMaker[row[2]].append(row[5])
					else:
						i = 0
						chordMaker[row[2]]=  [row[5]]
		
		print chordMaker
		for i in chordMaker:
			chordMaker[i].sort()
			chordString = "".join(chordMaker[i])
			if chordString in style:
				style[chordString] += 1
			else:
				style[chordString] = 1
				
			self.All[chordString] = []
		
		print style
		print len(style)
		self.middleCSV(compcsv,style)
	def initAll(self):
		for key in self.All:
			L=[]
			for i in range(0,68):
				L.append(0)
			self.All[key] = L		
	def middleCSV(self,composer,style):
		
		
		
		OUT = open("all.csv", "a")
		OUT.write(composer)
		
		for nextChord in style.keys():
			OUT.write(","+nextChord +":"+str(style[nextChord]))
		OUT.write("\n")
		OUT.close()
	def  finalCSV(self):
		self.All["composer"] = []
		INPUT = open("all.csv", "r")
		
		OUT = open("CARTready.csv", "w")
		
		songI = 0
		for nextLine in INPUT:
			data = nextLine.split(",")
			self.All["composer"].append(data[0])
			for i in range(1,len(data)):
				chord, value = data[i].split(":")
				#if chord in self.All:
				#	print "hello"
				
				self.All[chord][songI] = value
		
			songI += 1
		print self.All
		Allkeys = self.All.keys()
		print Allkeys
		OUT.write("Composer")
		for key in Allkeys:
			OUT.write(","+ key)
		OUT.write("\n")
		for i in range(0,68):
			OUT.write(self.All["composer"][i])
			for chord in self.All.keys():
				if(chord != "composer"):
					OUT.write("," + str(self.All[chord][i]))
			OUT.write("\n")
		
		INPUT.close()
		
		OUT.close()
		
if __name__ == '__main__':
	main()