import mechanize, json, datetime 
from bs4 import BeautifulSoup
from CaptchaParser import CaptchaParser
from PIL import Image
from collections import defaultdict
    
#browser initialise
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)

#open website
response = br.open("https://academics.vit.ac.in/student/stud_login.asp")
print br.geturl()
    
#select form
br.select_form("stud_login")    
    
#extracting captcha url
soup = BeautifulSoup(response.get_data())
img = soup.find('img', id='imgCaptcha')
print img['src']
    
#retrieving captcha image
br.retrieve("https://academics.vit.ac.in/student/"+img['src'], "captcha_student.bmp")
print "captcha retrieved"
img = Image.open("captcha_student.bmp")

parser = CaptchaParser()

captcha = parser.getCaptcha(img)
print str(captcha)
#fill form
reg_no="14BCE0141"    #fill ur data
pwd="gogoosgdlsgd"
br["regno"] = str(reg_no)
br["passwd"] = str(pwd)
br["vrfcd"] = str(captcha)
br.method = "POST"

res=br.submit().read()
print br.geturl()
if br.geturl()==("https://academics.vit.ac.in/student/home.asp"):
    print "SUCCESS"

    #opening timetable page
    #opening faculty advisor details page
    br.open("https://academics.vit.ac.in/student/faculty_advisor_view.asp")
    response = br.open("https://academics.vit.ac.in/student/faculty_advisor_view.asp")
    soup = BeautifulSoup(response.get_data())
    #print br.geturl()
    #extracting data
    '''
    facDetails = defaultdict(list)
    for i in range(1,8):
        day = defaultdict(list)
        for j in range(0,2):
            day[j] = soup("table")[0][0].findAll("tbody")[0].findAll("tr")[i].findAll("td")[j].getText().encode('utf-8').replace("\xc2\xa0"," ")
            if len(day[j]) > 10:
                print day[j]
                pass
            else:
                day[j] = 0
        facDetails[i-1] = day
    print facDetails
    '''
    #print soup
    tables = soup.findChildren('table')
    myTable = tables[0]
    rows = myTable.findChildren(['th','tr'])

    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            value = cell.string
            print value