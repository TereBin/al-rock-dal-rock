import json
import pprint as pp

def engineering(student_json_path, student_dict, w):
    i = 2
    while len(w.row_values(i)) > 0:
        data = w.row_values(i)
        score = data[1]
        email = data[-1]
        print(email)
        if score[0] == score[-1]:
            print("정답")
            if email in student_dict.keys():
                print("기존 유저")
                student_dict[email]["engineering"] = "True"
                pp.pprint(student_dict)
                with open(student_json_path, 'w', encoding='utf-8') as file:
                    json.dump(student_dict, file, indent="\t")
            else:
                print("신규 유저")
                student_dict[email] = {}
                student_dict[email]["humanities"] = "False"
                student_dict[email]["social"] = "False"
                student_dict[email]["mas"] = "False"
                student_dict[email]["natural"] = "False"
                student_dict[email]["engineering"] = "True"
                student_dict[email]["economic"] = "False"
                student_dict[email]["business"] = "False"
                pp.pprint(student_dict)
                with open(student_json_path, 'w', encoding='utf-8') as file:
                    json.dump(student_dict, file, indent="\t")

        else:
            print("오답\n")
        i += 1
