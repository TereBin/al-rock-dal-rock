import gspread
import json
import time

from humanities import humanities
from social import social
from mas import mas
from natural import natural
from engineering import engineering
from economic import economic
from business import business

json_key_path = 'D:/TereBin/GatherTown/code/gathertown-359823-7e83d8ff5f37.json'
student_json_path = 'D:/TereBin/GatherTown/code/student_list.json'

student_json = open(student_json_path, 'r', encoding='utf-8')
student_dict = json.load(student_json)

gc = gspread.service_account(filename=json_key_path)

business_url = "https://docs.google.com/spreadsheets/d/1PD5otVhL6cwZ3R88nlCknunVfvb2CPAazLd-nvlZzc4/edit?resourcekey#gid=669225574"
economic_url = "https://docs.google.com/spreadsheets/d/16OlNxE5xSD6LfAOjvO-lHFLEch0c-tCuN2A2gph6p_I/edit?resourcekey#gid=686587266"
engineering_url = "https://docs.google.com/spreadsheets/d/187x0PLt0MKovMORpMjH_I8k1scDnSgDDWwhTSUgC_Ck/edit?resourcekey#gid=642057197"
humanities_url = "https://docs.google.com/spreadsheets/d/1-r-i0Ct28gAZkmXSsneqoRvAjyuNXABsEWHd1ZRKDD4/edit?resourcekey#gid=1248365205"
mas_url = "https://docs.google.com/spreadsheets/d/11xt6N_fHtEQvoizIIhiohhaMM3aZ9K2dVpVsqBKUFR4/edit?resourcekey#gid=248119554"
natural_url = "https://docs.google.com/spreadsheets/d/1QapYrOfr3_BwzRJ_0ZOur2pzc-ZKjszngoDjeUQy078/edit?resourcekey#gid=888322051"
social_url = "https://docs.google.com/spreadsheets/d/1Bmm3Eb4_wlrys_R3ZqjV44U1VI1GrAgEP5U389l7k_w/edit?resourcekey#gid=743222954"

while True:
    print("인문대")
    humanities_w = gc.open_by_url(humanities_url).worksheet('설문지 응답 시트1')
    humanities(student_json_path, student_dict, humanities_w)
    print("사과대")
    social_w = gc.open_by_url(social_url).worksheet("설문지 응답 시트1")
    social(student_json_path, student_dict, social_w)
    print("지융미")
    mas_w = gc.open_by_url(mas_url).worksheet("설문지 응답 시트1")
    mas(student_json_path, student_dict, mas_w)
    print("자연대")
    natural_w = gc.open_by_url(natural_url).worksheet("설문지 응답 시트1")
    natural(student_json_path, student_dict, natural_w)
    print("공과대")
    engineering_w = gc.open_by_url(engineering_url).worksheet("설문지 응답 시트1")
    engineering(student_json_path, student_dict, engineering_w)
    print("겅제대")
    economic_w = gc.open_by_url(economic_url).worksheet("설문지 응답 시트1")
    economic(student_json_path, student_dict, economic_w)
    print("경영대")
    business_w = gc.open_by_url(business_url).worksheet("설문지 응답 시트1")
    business(student_json_path, student_dict, business_w)

    time.sleep(30)
