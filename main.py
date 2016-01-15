################################################################################ IMPORTS ##############

from flask import Flask, request, jsonify
from fetchData import timetable, get_facultyAdvisor_details, get_attendance_details, get_exam_schedule, get_marks, get_spotlight, get_apt_attendance, get_acad_history, change_password, getFaculties
from CoursePage import get_courses, get_slot, get_faculty, get_data
from majorRoute import majorRoute
import os

app = Flask(__name__)

################################################################################ HOME ##################

@app.route('/home')
def hello_world(): return "welcome_to_student_login_api"

################################################################################ SPOTLIGHT #############

@app.route('/spotlight')
def spotlight():

	data = get_spotlight()
	return jsonify(**data)

################################################################################ FACULTY ADVISOR #######

@app.route('/facadvdet', methods=["GET"])
def login_facultyAdvisor():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")

	data = get_facultyAdvisor_details(reg_no, pwd)
	return jsonify(**data)

################################################################################ TIME TABLE ############

@app.route('/timetable', methods=["GET"])
def login_timetable():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")

	data = timetable(reg_no, pwd)
	return jsonify(**data)

################################################################################ ATTENDANCE ############

@app.route('/attendance', methods=["GET"])
def login_attendance():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")

	data = get_attendance_details(reg_no, pwd)
	return jsonify(**data)

################################################################################ MARKS #################

@app.route('/marks', methods=["GET"])
def get_mark():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")

	data = get_marks(reg_no, pwd)
	return jsonify(**data)

################################################################################ EXAM SCHEDULE #########

@app.route('/examschedule', methods=["GET"])
def login_examschedule():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")

	data = get_exam_schedule(reg_no, pwd)
	return jsonify(**data)

################################################################################ COURSE PAGE ###########

@app.route('/coursepage/courses', methods=["GET"])
def courseBase():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")

	data = get_courses(reg_no, pwd)
	return jsonify(**data)

@app.route('/coursepage/slots', methods=["GET"])
def courselevel1():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")
	crs = request.args.get("crs")

	data = get_slot(reg_no, pwd,crs)
	return jsonify(**data)

@app.route('/coursepage/faculties', methods=["GET"])
def courselevel2():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")
	crs = request.args.get("crs")
	slt = request.args.get("slt").replace(" ","+")

	data = get_faculty(reg_no, pwd,crs,slt)
	return jsonify(**data)

@app.route('/coursepage/data', methods=["GET"])
def courselevel3():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")
	crs = request.args.get("crs")
	slt = request.args.get("slt").replace(" ","+")
	fac = request.args.get("fac")

	data = get_data(reg_no, pwd,crs,slt,fac)
	return jsonify(**data)

################################################################################ APT ATTENDANCE ########

@app.route('/aptattn', methods=["GET"])
def aptattendance():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")

	data = get_apt_attendance(reg_no, pwd)
	return jsonify(**data)

################################################################################ ACADEMIC HISTORY ######

@app.route('/acadhist', methods=["GET"])
def acadHistory():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")

	data = get_acad_history(reg_no, pwd)
	return jsonify(**data)

################################################################################ RESULT ################

@app.route('/')
def result():
	return 'hello_world'
	#return jsonify(**results())

################################################################################ CHANGE PASSWORD #######

@app.route('/changepswd', methods=["GET"])
def passwordchange():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")
	newpwd = request.args.get("npsswd")

	data = change_password(reg_no, pwd,newpwd)
	return jsonify(**data)

################################################################################ FACULTY DATABASE ######

@app.route('/getFaculty', methods = ["GET"])
def getData():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")
	data = getFaculties(reg_no, pwd)
	return jsonify(**data)

################################################################################ REFRESH ###############

@app.route('/refresh', methods = ["GET"])
def Refresh():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")
	data = majorRoute(reg_no, pwd)
	return jsonify(**data)

################################################################################ MAIN ##################

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)

################################################################################ END ###################
