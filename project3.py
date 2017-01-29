import pandas as pd # import pandas to be able to use the DataFrame, which creates table-like objects
import bokeh # import bokeh to be able to make a variety of charts from within Python
from bokeh.charts import Bar, output_file, save
# import Bar from bokeh.charts to be able to make the actual plots
# import output_file to get the function needed to create the html file
# import save to get the function needed to save the html file
df = pd.read_csv('Pokemon.csv%3Fsv%3D2015-12-11%26sr%3Db%26sig%3DZ9S6p8prK6gi7hWD6XW86RbqhRLzWHIH3fjFYz19hAw%3D%26se%3D2017-01-31T01%3A49%3A57Z%26.csv')                             #accesses the data and converts it into a data frame
# access the data and convert it into a data frame
p = Bar(df, # create a Bar chart from the DataFrame
        label = 'Type 1', # set Type 1 as the list of string representing the categories
        values = 'HP', # set the value of HP to be used for producing the Bar chart using table-like input data
        agg = 'mean', # aggregate the data using mean statistic
        group = 'Type 1', # use the column Type 1 for grouping
        title = 'Average HP by Pokemon Type', # set the graph title as Average HP by Pokemon Type
        plot_width = 1000, # set the width of the plot to 1000
        plot_height = 1000, # set the height of the plot to 1000
        bar_width = 1000) # set the width of the bar to 1000

output_file('bar.html') # give the file a name and make it into a visual

save(p) # save the file

