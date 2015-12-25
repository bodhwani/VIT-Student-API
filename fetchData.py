from login import login
from bs4 import BeautifulSoup
import time

#####################################################################################################################################################

def results(reg_no = "14BCE0104", pswd = "gogogogogoogle4"):

	#logging into student login
	br = login(reg_no,pswd)

	#checking that are we logged in or not
	if br.geturl() == ("https://academics.vit.ac.in/student/home.asp"):
		print "SUCCESS"

		br.open("https://academics.vit.ac.in/student/grade.asp?sem=FS")
		response = br.open("https://academics.vit.ac.in/student/grade.asp?sem=FS")
		soup = BeautifulSoup(response.get_data())

		#extracting tables
		tables = soup.findChildren('table')

		try:
			myTable = tables[1]
		except IndexError:
			myTable = 'null'
			return {"status" : "Not_Updated"}

		rows = myTable.findChildren(['th','tr'])
		result = {}


		return {"status" : "Updated"}
	else:
		print "FAIL"
		return {"status" : "Failure"}

#####################################################################################################################################################

def timetable(reg_no = "", pswd = ""):

	#logging into student login
	br = login(reg_no,pswd)

	#checking that are we logged in or not
	if br.geturl() == ("https://academics.vit.ac.in/student/home.asp"):
		print "SUCCESS"

		#opening time table page
		br.open("https://academics.vit.ac.in/student/timetable_fs.asp")
		response = br.open("https://academics.vit.ac.in/student/timetable_fs.asp")
		soup = BeautifulSoup(response.get_data())

		#extracting tables
		tables = soup.findAll('table')

		#getting required table
		myTable = tables[1]
		rows = myTable.findChildren(['th','tr'])

		#initialising some required variables
		ttable = {}
		j = 0

		#extracting data
		for row in rows:

			rowdata =  {}
			cells = row.findAll('td')
			if len(cells) == 1:
				print "row_with_no_entries"
				continue
			else:
				j = 0
				for cell in cells:
					value = cell.string
					print value
					rowdata[j] = value
					j = j+1

				#if the course contains embedded lab
				if len(cells) == 10:
					ttable[rowdata[0].replace("\r\n\t\t","")] = list({rowdata[1].replace("\r\n\t\t",""), rowdata[2].replace("\r\n\t\t",""), rowdata[5].replace("\r\n\t\t",""), rowdata[6].replace("\r\n\t\t",""), rowdata[7].replace("\r\n\t\t",""), rowdata[8].replace("\r\n\t\t",""), rowdata[9].replace("\r\n\t\t","")})
				else:
					ttable[rowdata[2].replace("\r\n\t\t","")] = list({rowdata[3].replace("\r\n\t\t",""), rowdata[4].replace("\r\n\t\t",""), rowdata[7].replace("\r\n\t\t",""), rowdata[8].replace("\r\n\t\t",""), rowdata[9].replace("\r\n\t\t",""), rowdata[10].replace("\r\n\t\t","") if rowdata[10] is not None else "not_given", rowdata[11].replace("\r\n\t\t","")})

		return {"status" : "Success" , "time_table" : ttable}
	else :
		print "FAIL"
		return {"status" : "Failure"}

#####################################################################################################################################################

def get_facultyAdvisor_details(reg_no = "", pwd = ""):

	br = login(reg_no,pwd)

	print br.geturl()

	#checking that are we logged in or not

	if br.geturl() == ("https://academics.vit.ac.in/student/home.asp"):
		print "SUCCESS"

		#opening faculty advisor details page
		br.open("https://academics.vit.ac.in/student/faculty_advisor_view.asp")
		response = br.open("https://academics.vit.ac.in/student/faculty_advisor_view.asp")
		soup = BeautifulSoup(response.get_data())

		#extracting tables
		tables = soup.findChildren('table')
		myTable = tables[1]
		rows = myTable.findChildren(['th','tr'])

		#initialising some required variables
		facdet = {}
		j = 0

		#extracting data
		for row in rows:

			rowdata =  {}
			cells = row.findChildren('td')

			if len(cells) == 1:
				continue
			else:
				j=0
				for cell in cells:

					value = cell.string
					print value
					rowdata[j] = value
					j = j+1

				facdet[rowdata[0].replace("\r\n\t\t","")] = rowdata[1].replace("\r\n\t\t","")
		return {"status" : "Success" , "faculty_det" : facdet}

	else :
		print "FAIL"
		return {"status" : "Failure"}

#####################################################################################################################################################

def get_attendance_details(reg_no = "", pwd = ""):

	br = login(reg_no,pwd)

	print br.geturl()

	if br.geturl() == ("https://academics.vit.ac.in/student/home.asp"):
		print "SUCCESS"

		#getting today's date
		today = time.strftime("%d-%m-%Y")

		#opening the attendance page
		br.open("https://academics.vit.ac.in/student/attn_report.asp?sem=FS")
		response = br.open("https://academics.vit.ac.in/student/attn_report.asp?sem=FS")
		soup = BeautifulSoup(response.get_data())

		#selecting the form
		#br.select_form("attn_report")

		#setting the current date
		#br["to_date"] = str(today)

		#br.method = "POST"
		#br.submit()

		br.open("https://academics.vit.ac.in/student/attn_report.asp?sem=FS&fmdt=09-Jul-2015&todt=%(to_date)s" % {"to_date" : today })
		response = br.open("https://academics.vit.ac.in/student/attn_report.asp?sem=FS&fmdt=09-Jul-2015&todt=%(to_date)s" % {"to_date" : today })
		soup = BeautifulSoup(response.get_data())

		#extracting tables
		tables = soup.findChildren('table')
		myTable = tables[3]
		rows = myTable.findChildren(['th','tr'])

		#initialising some required variables
		attndet = {}
		i,j = 0,0

		#extracting data
		for row in rows:

			rowdata = {}
			cells = row.findChildren('td')
			j = 0
			for cell in cells:

				value = cell.string
				print value
				rowdata[j] = value
				j = j+1

			attndet[i] = rowdata
			i = i+1
		return {"status" : "Success" , "attendance_det" : attndet}

	else :
		print "FAIL"
		return {"status" : "Failure"}

#####################################################################################################################################################

def get_exam_schedule(reg_no = "", pwd = ""):

	br = login(reg_no,pwd)

	print br.geturl()

	if br.geturl() == ("https://academics.vit.ac.in/student/home.asp"):
		print "SUCCESS"

		#inmporting Queue
		import Queue as q

		br.open("https://academics.vit.ac.in/student/exam_schedule.asp?sem=FS")
		response = br.open("https://academics.vit.ac.in/student/exam_schedule.asp?sem=FS")
		soup = BeautifulSoup(response.get_data())

		#extracting tables
		tables = soup.findAll('table')
		try:
			myTable = tables[1]
		except IndexError:
			myTable = 'null'
			return {"status" : "Not_Updated"}

		rows = myTable.findChildren(['th','tr'])
		rows = rows[2:]

		#initialising some required variables for getting schedule for CAT-1
		schedule = {}

		#holding the cat1, cat2, termend schedules in queue
		p = q.Queue()
		
		#extracting data
		for row in rows:

			rowdata = {}
			cells = row.findChildren('td')
			j = 0
			if len(cells) != 1:
				for cell in cells:

					value = cell.string
					print value
					rowdata[j] = value
					j = j+1
				schedule[rowdata[1].replace("\r\n\t\t","")] = list({rowdata[2].replace("\r\n\t\t",""), rowdata[4].replace("\r\n\t\t",""), rowdata[5].replace("\r\n\t\t",""), rowdata[6].replace("\r\n\t\t",""), rowdata[7].replace("\r\n\t\t",""), rowdata[8].replace("\r\n\t\t","")})
			
			elif len(cells) == 1:
				p.put(schedule)
				schedule = {}
				continue
		cat1 = p.get()
		cat2 = p.get()
		termend = p.get()
		#print cat1
		#print "\n\n\n\n"
		#print cat2
		#print "\n\n\n\n"
		#print trmend
		return {"status" : "Success" , "cat1" : cat1 , "cat2" : cat2 , "term_end" : termend}

	else :
		print "FAIL"
		return {"status" : "Failure"}

#####################################################################################################################################################

def get_marks(reg_no = "", pwd = ""):

	br = login(reg_no,pwd)

	print br.geturl()

	if br.geturl() == ("https://academics.vit.ac.in/student/home.asp"):
		print "SUCCESS"

		br.open("https://academics.vit.ac.in/student/marks.asp?sem=FS")
		response = br.open("https://academics.vit.ac.in/student/marks.asp?sem=FS")
		soup = BeautifulSoup(response.get_data())

		tables = soup.findAll('table')
		myTable = tables[1]
		marks = {}
		rows = myTable.findChildren(['th','tr'])
		rows = rows[2:]
		j = 0

		for row in rows:
			rowdata = {}
			cells = row.findAll('td')
			j = 0

			for cell in cells:
				value = cell.string
				print value
				rowdata[j] = value
				j = j+1

			if len(cells) == 20: 
				marks[rowdata[2].replace("\r\n\t\t","")] = {"coruse_code" : rowdata[2].replace("\r\n\t\t",""), "course_title" : rowdata[3].replace("\r\n\t\t",""), "course_type" : rowdata[4].replace("\r\n\t\t",""), "cat1" : rowdata[6].replace("\r\n\t\t",""), "cat2" : rowdata[8].replace("\r\n\t\t",""), "quiz1" : rowdata[10].replace("\r\n\t\t",""), "quiz2" : rowdata[12].replace("\r\n\t\t",""), "quiz3" : rowdata[14].replace("\r\n\t\t",""), "assignment" : rowdata[16].replace("\r\n\t\t",""),"final_assesment" : rowdata[19].replace("\r\n\t\t","")}
			else:
				marks[rowdata[2].replace("\r\n\t\t","")] = {"coruse_code" : rowdata[2].replace("\r\n\t\t",""), "course_title" : rowdata[3].replace("\r\n\t\t",""), "course_type" :  rowdata[4].replace("\r\n\t\t",""), "lab_cat" : rowdata[7].replace("\r\n\t\t",""), "lab_termend" : rowdata[9].replace("\r\n\t\t","")}

		try:
			myTable = tables[2]
		except IndexError:
			myTable = 'null'
			return {"status" : "Success" , "marks" : marks}

		rows = myTable.findAll(['th','tr'])

		for row in rows:
			print row
			print "\n\n"
		return {"status" : "Success" , "marks" : marks}

	else :
		print "FAIL"
		return {"status" : "Failure"}
