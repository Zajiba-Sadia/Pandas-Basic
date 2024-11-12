import pandas as pd
def convert_people_cell(cell):
    if cell =="n.a":
        return 'sam walton'
    return cell
def convert_eps_cell(cell):
    if cell=="not available":
        return None
    return cell


df = pd.read_excel("Businessman.xlsx", converters = {'people': convert_people_cell,
                                                     'eps': convert_eps_cell})
df.to_excel("newxl.xlsx",sheet_name="New attempt", startrow = 1, startcol = 2)
print(df)