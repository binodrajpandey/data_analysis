import pandas as pd
from urllib.request import urlretrieve

urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/italy-covid-daywise.csv',
            'italy-covid-daywise.csv')
covid_df = pd.read_csv('italy-covid-daywise.csv')

# <class 'pandas.core.frame.DataFrame'>s
print(type(covid_df))

# Gives info like rows column, datatype, memory etc.
# RangeIndex: 248 entries, 0 to 247
# Data columns (total 4 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   date        248 non-null    object
#  1   new_cases   248 non-null    float64
#  2   new_deaths  248 non-null    float64
#  3   new_tests   135 non-null    float64
# dtypes: float64(3), object(1)
# memory usage: 7.9+ KB
covid_df.info()
# Gives mean median, std, max etc.
#         new_cases  new_deaths     new_tests
# count   248.000000  248.000000    135.000000
# mean   1094.818548  143.133065  31699.674074
# std    1554.508002  227.105538  11622.209757
# min    -148.000000  -31.000000   7841.000000
# 25%     123.000000    3.000000  25259.000000
# 50%     342.000000   17.000000  29545.000000
# 75%    1371.750000  175.250000  37711.000000
# max    6557.000000  971.000000  95273.000000
print(covid_df.describe())
print(covid_df.columns)
print(covid_df.shape)
print(covid_df['date'][243])
field_value = covid_df.at[243,'new_tests']
print(field_value)
print(covid_df.new_cases)

covid_df_copy = covid_df.copy()
print(covid_df_copy.loc[243])
covid_df_copy.head(5)
covid_df_copy.tail(4)
covid_df_copy.new_tests.first_valid_index()
covid_df_copy.sample(10)
covid_df_copy.new_cases.sum()

death_rate = covid_df.new_deaths.sum()/ covid_df.new_cases.sum()

#Querying and sorting rows
# Return series of True and False
high_new_cases = covid_df.new_cases>1000
print(covid_df[high_new_cases])
high_cases_df = covid_df[covid_df.new_cases>100]
print(high_cases_df)

# Elementwise division
covid_df.new_cases/covid_df.new_tests
# Add new column
covid_df['positive_rate'] = covid_df.new_cases/covid_df.new_tests
print(covid_df)
covid_df.drop(columns=['positive_rate'], inplace=True)
print(covid_df)

# Sorting
covid_df.sort_values('new_cases', ascending= False).head(10)

#Date
covid_df['date'] = pd.to_datetime(covid_df.date)
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday
print(covid_df)

covid_df_may = covid_df[covid_df.month==5]
print(covid_df_may)
covid_df_may_matrix = covid_df_may[[ 'new_cases', 'new_deaths','new_tests']]
print(covid_df_may_matrix)
print(covid_df_may_matrix.sum())
print(covid_df.new_cases.mean())
average_for_sunday = covid_df[covid_df.weekday==6].new_cases.mean()
print(average_for_sunday)

#Grouping
monthly_sum = covid_df.groupby('month')[['new_cases','new_deaths', 'new_tests']].sum()
#   new_cases  new_deaths  new_tests
# month
# 1            3.0         0.0        0.0
# 2          885.0        21.0        0.0
# 3       100851.0     11570.0        0.0
# 4       101852.0     16091.0   419591.0
# 5        29073.0      5658.0  1078720.0
# 6         7772.0      1404.0   830354.0
# 7         6722.0       388.0   797692.0
# 8        21060.0       345.0  1098704.0
# 9         3297.0        20.0    54395.0
# 12           0.0         0.0        0.0
print(monthly_sum)

#Cumulative Sum
covid_df['total_cases'] =  covid_df.new_cases.cumsum()
print(covid_df)

# Write to file
covid_df.to_csv('result.csv', index=None)