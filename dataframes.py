import pandas as pd

# create dataframe
info_marks = pd.DataFrame({'name': ['Parker', 'Smith', 'William', 'Terry'],
                           'Maths': [78, 84, 67, 72],
                           'Science': [89, 92, 61, 77],
                           'English': [72, 75, 64, 82]})

# render dataframe as html
writer = pd.
info_marks.to_excel(writer)
writer.save()
print('DataFrame is written successfully to the Excel File.')