"""Write a Python program to SORT and print the result data of the above table.
User must have option to choose the Sorting parameter
[1. Sort by P_ID, 2. Sort by Start Time, 3. Sort by Priority]"""
flight_Table = [
    {'P_ID': 'P1', 'Process':  'VSCode', 'Start Time': 100, 'Priority':  'MID'},
{'P_ID': 'P23', 'Process': 'Eclipse', 'Start Time': 234 , 'Priority': 'MID'},
{'P_ID': 'P93', 'Process': 'Chrome', 'Start Time': 189 , 'Priority': 'High'},
{'P_ID': 'P42', 'Process': 'JDK', 'Start Time': 9, 'Priority':  'High'},
{'P_ID': 'P9', 'Process': 'CMD', 'Start Time': 7, 'Priority':  'High'},
{'P_ID': 'P87', 'Process': 'NotePad', 'Start Time': 23, 'Priority':  'Low'}
]

def sort_data(data, sort_by):
    if sort_by == 'P_ID':
        return sorted(data, key=lambda x: x['P_ID'])
    elif sort_by == 'Start Time':
        return sorted(data, key=lambda x: x['Start Time'])
    elif sort_by == 'Priority':
        return sorted(data, key=lambda x: x['Priority'])
    else:
        return data


sort_by = input("Enter the sorting parameter (P_ID, Start Time, Priority): ")

sorted_data = sort_data(flight_Table, sort_by)

for item in sorted_data:
    print(item)