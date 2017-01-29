import pandas as pd # import pandas to be able to use the DataFrame, which creates table-like objects
import bokeh # import bokeh to be able to make a variety of charts from within Python
from bokeh.charts import HeatMap, output_file, save
# import HeatMap from bokeh.charts to be able to make the actual plots
# import output_file to get the function needed to create the html file
# import save to get the function needed to save the html file
df = pd.read_csv('Pokemon.csv%3Fsv%3D2015-12-11%26sr%3Db%26sig%3DZ9S6p8prK6gi7hWD6XW86RbqhRLzWHIH3fjFYz19hAw%3D%26se%3D2017-01-31T01%3A49%3A57Z%26.csv')
# access the data and convert it into a DataFrame
p = HeatMap(df, # create a HeatMap from the DataFrame
        x = 'Type 1', # specify the variable of Type 1 (which is the column that lists the type 1 of each Pokemon) to be used for the x axis
        y = 'Speed', # specify the variable of Speed (which is the column that lists the speed of each Pokemon) to be used for the y axis
        xlabel = 'Type of Pokemon', # set the label of the x axis to Type of Pokemon
        ylabel = 'Speed', # set the label of the y axis to Speed
        values = 'Speed', # set the value of Speed to be used for producing the Heatmap using table-like input data
        title = 'Speed of Types of Pokemon') # set the title of the graph to Speed of Types of Pokemon

output_file('heatmap.html') # give the file a name and make it into a visual

save(p) # save the file

