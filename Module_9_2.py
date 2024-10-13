first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


first_result = [len(l) for l in first_strings if len(l) >= 5]

second_result = [(x, i) for x in first_strings for i in second_strings if len(x) == len(i)]

combined_strings = first_strings + second_strings
third_result = {s: len(s) for s in combined_strings if len(s) % 2 == 0}

# Пример выполнения кода:
print(first_result)
print(second_result)
print(third_result)