import pandas as pd

employees = pd.DataFrame({
    'EmpID' : [1,2,3],
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'DeptID': [101,102,103]
})

departments = pd.DataFrame({
    'DeptID': [101, 102, 104],
    'DeptName': ['HR', 'IT', 'Finance']
})

#Merge on DeptID (like inner join)
merged_df = pd.merge(employees, departments, on='DeptID', how='inner')
print("Inner Join:\n",merged_df)


# Left join
left_join_df = pd.merge(employees, departments, on='DeptID', how='left')
print("Left Join:\n",left_join_df)