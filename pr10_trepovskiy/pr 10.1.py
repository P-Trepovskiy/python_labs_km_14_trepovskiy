salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
new_salaries = [round(i + i * 0.3, 2) for i in salary_list]
index_sum = [round(i * 0.3, 2) for i in salary_list]

print('Salary table:')
for i, j, k in zip(salary_list, new_salaries, index_sum):
    print(i, j, k)