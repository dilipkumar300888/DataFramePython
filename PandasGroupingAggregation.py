import pandas as pd

data = {
    'Department' : ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
    'Employee' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Salary' : [50000, 60000, 70000, 65000, 55000, 62000],
    'Experience' : [2, 3, 5, 4, 3, 6]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

print("\nTotal Salary per Department:\n", df.groupby('Department')['Salary'].sum())

print("\nAverage Experience:\n",df.groupby('Department')['Experience'].mean())