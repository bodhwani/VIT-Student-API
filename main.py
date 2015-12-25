from flask import Flask, request, jsonify
from fetchData import timetable, get_facultyAdvisor_details, get_attendance_details, get_exam_schedule, get_marks
from CoursePage import get_courses, get_slot, get_faculty, get_data
import os

app = Flask(__name__)

@app.route('/home')
def hello_world():
	return "welcome_to_student_login_api"

######################################################################

@app.route('/facultyadvdet', methods=["GET"])
def login_facultyAdvisor():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")

	data = get_facultyAdvisor_details(reg_no, pwd)
	return jsonify(**data)

######################################################################

@app.route('/timetable', methods=["GET"])
def login_timetable():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")

	data = timetable(reg_no, pwd)
	return jsonify(**data)

######################################################################

@app.route('/attendance', methods=["GET"])
def login_attendance():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")

	data = get_attendance_details(reg_no, pwd)
	return jsonify(**data)

######################################################################

@app.route('/marks', methods=["GET"])
def get_mark():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")

	data = get_marks(reg_no, pwd)
	return jsonify(**data)

######################################################################

@app.route('/examschedule', methods=["GET"])
def login_examschedule():
	reg_no = request.args.get("regNo")
	pwd = request.args.get("psswd")

	data = get_exam_schedule(reg_no, pwd)
	return jsonify(**data)

######################################################################

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

######################################################################

@app.route('/')
def result():
	return 'hello_world'
	#return jsonify(**results())

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)

######################################################################
