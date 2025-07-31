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

df['Bonus'] = df['Salary'] * 0.10

print("\nDataframe with Bonus:\n", df)

print("\nAverage Bonus by Department:\n",df.groupby('Department')['Bonus'].mean())

exp_filtered = df[df['Experience'] > 3]

print("\nGive rows greater than 3 years Experience:\n",exp_filtered)

exp_count = exp_filtered.groupby('Department')['Employee'].count()

print("\nEmployees with Experience > 3 (per Department):\n",exp_count)