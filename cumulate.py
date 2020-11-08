# this prpgram is for creating csv of cumulative TRICO count
# REMARK: run after running "naming.py"!!!

import datetime 
import os
import itertools
import csv

dateList = []

TRICOfiles = os.listdir("TRICO")

for f in TRICOfiles:
	if (f == ".DS_Store"):
		continue

	d = f.replace(".jpg", "")
	dateFormatted = [datetime.datetime.strptime(d, "%Y-%m-%d %H-%M-%S")]


	dateList.append(dateFormatted)



# sort according to date
sortedDate = sorted(dateList, key = lambda d: d[0])
sortedDate = list(itertools.chain.from_iterable(sortedDate))


# create csv with cummulative
allDate = [["Y/M/D", "Cummulate"]]
#origin = sortedDate[0]
#lastdate = sortedDate[len(sortedDate) - 1]
origin = datetime.datetime(2015, 4, 1, 0, 0, 0)
lastdate = datetime.datetime.today()
thisday = origin

oneday = datetime.timedelta(days = 1)
cummulate = 0

while True:
	for i in range(cummulate, len(sortedDate)):
		if thisday.date() == sortedDate[i].date():
			cummulate = cummulate + 1
			break

	d = [thisday.strftime("%Y/%m/%d"), cummulate]
	allDate.append(d)

	if (thisday.year == lastdate.year and thisday.month == lastdate.month and thisday.day == lastdate.day):
		break

	thisday = thisday + oneday

with open("tricofreq.csv", "w") as f:
	writer = csv.writer(f, lineterminator = "\n")
	writer.writerows (allDate)






