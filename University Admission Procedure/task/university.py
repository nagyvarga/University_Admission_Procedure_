applicants = {}
DEPARTMENTS = {'Biotech': [0, 1], 'Chemistry': [1], 'Engineering': [2, 3], 'Mathematics': [2], 'Physics': [0, 2]}
applicants_to_departments = {dep: [] for dep in DEPARTMENTS}


def give_back_integer():
    while True:
        try:
            user_input = int(input())
        except TypeError:
            pass
        else:
            break
    return user_input


def write_files_from_departments():
    for department in DEPARTMENTS.keys():
        f = open(f'{department}.txt', 'w', encoding='utf-8')
        for full_name, gpa_data in sorted(applicants_to_departments[department], key=lambda x: (-x[1], x[0])):
            f.write(f'{full_name} {gpa_data}\n')
        f.close()


applicants_file = open('applicants.txt', 'r')
for data_about_applicant in applicants_file:
    f_name, surname, physics, chemistry, math, cs, special_exam, dp1, dp2, dp3 = data_about_applicant.split()
    applicants.update({f'{f_name} {surname}': [float(physics), float(chemistry), float(math), float(cs),
                                               float(special_exam), dp1, dp2, dp3]})
applicants_file.close()

limit = give_back_integer()

for i in range(3):
    filtered_data = []
    for name, applicant_data in applicants.items():
        department_name = applicant_data[5 + i]
        exams = DEPARTMENTS.get(department_name)
        sum_up_exams = 0
        for exam in exams:
            sum_up_exams += applicant_data[exam]
        exam_score = sum_up_exams / len(exams)
        exam_score = max(exam_score, applicant_data[4])
        filtered_data.append([name, department_name, exam_score])
        filtered_data.sort(key=lambda x: (-x[2], x[0]), reverse=True)
    for k in reversed(list(range(len(applicants)))):
        if len(applicants_to_departments[filtered_data[k][1]]) < limit:
            applicants_to_departments[filtered_data[k][1]] += [[filtered_data[k][0], filtered_data[k][2]]]
            del applicants[filtered_data[k][0]]

write_files_from_departments()
