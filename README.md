## Pandas
### Dependencies
- pandas==1.1.2
- python-dateutil==2.8.1
- pytz==2020.1
- six==1.15.0
 
 If we install pandas, above dependencies are automatically installs.
Internal structure of pandas data frame is like below:
```
covid_data_dict = {
'date' : ['2020-01-12','2020-01-13'],
'new_cases': [133,233],
'new_deaths': [11,12],
'new_tests': [544,332]
}
```
For detail please follow this reference [ref](https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas/lesson/lesson-4-analyzing-tabular-data-with-pandas)

## Visualization with matplotlib and seaborn
### Dependencies
- cycler==0.10.0
- kiwisolver==1.2.0
- matplotlib==3.3.2
￿- Pillow==7.2.0
- pyparsing==2.4.7
 Those dependency will be automatically install if we install matplotlib.
### Line Chart
#### Styling lines and marker
- color (c): set the color of line
- linestyle (ls): choose between solid or dashesd
- linewidth (lw): set width of the line
- markersize(ls): set the size of marker
- markeredgedcolor(mec): set edge color of the marker
- markeredgedwidth(mew): edge width of marker
- markerfacecolor (mfc): set the fill color of the marker
- alpha: opacity of the plot
### Scatter plot
### Historgram
### Bar