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


data1 = {'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
        'Salary': [50000, 60000, 70000, 65000, 55000, 62000],
        'Bonus': [5000, 6000, 7000, 6500, 5500, 6200]}

df1 = pd.DataFrame(data1)


# Multiple aggregations
result = df1.groupby('Department').agg({
    'Salary': ['mean', 'max'],
    'Bonus': ['sum', 'min']
})
print("\nMultiple Aggregations:\n", result)


# Custom aggregation function
def range_func(x):
    return x.max() - x.min()

result_custom = df1.groupby('Department').agg({
    'Salary': range_func,
    'Bonus': range_func
})
print("\nCustom Aggregation Function:\n", result_custom)