from fetchData import *

def majorRoute(reg_no = "", pswd = ""):
	time_table = timetable(reg_no,pswd)['time_table']
	attendance = get_attendance_details(reg_no,pswd)['attendance_det']
	marks = get_marks(reg_no,pswd)['marks']

	keys = marks.keys()
	data = []
	i = 0
	for key in keys:
		data.append(time_table[key])
		data[i]["attendance"] = attendance[key]
		data[i]["marks"] = marks[key]
		i = i+1


	#print course
	#refresh = { "reg_no": reg_no, "campus": "vellore", "course" : [] , "status": {"message": "Successful execution", "code": 0} }
	return {"refresh": data}