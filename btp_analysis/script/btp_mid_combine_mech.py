import pandas as pd
import re

btp_midsem_marks = open('../data/btp_midsem_marks.txt', 'r').read().splitlines()
for i, x in enumerate(btp_midsem_marks):
    btp_midsem_marks[i] = re.sub(r'\s+', '  ', btp_midsem_marks[i])

roll, marks = [], []
for i in btp_midsem_marks:
    r, m = i.split('  ')
    roll.append(r)
    marks.append(m)

btp_allocation = pd.read_csv('../data/btp_allocation.csv', sep=',').fillna('')
btp_allocation['All_Guides'] = btp_allocation['Guide'] + ', ' + \
    btp_allocation['Co-guide']
del btp_allocation['Guide']
del btp_allocation['Co-guide']

btp_allocation['Marks'] = marks  # since the order was same in both the files
btp_allocation['roo'] = roll

# Sanity check
for row in btp_allocation.iterrows():
    if row[1]['roll_number'].strip() != row[1]['roo'].strip():
        print(row, 'something wrong')
    # Remove ugly commas
    if row[1]['All_Guides'].split(',')[1] == ' ':
        row[1]['All_Guides'] = row[1]['All_Guides'].split(',')[0]
del btp_allocation['roo']

btp_allocation.to_csv('../output/btp_analysis.csv')
