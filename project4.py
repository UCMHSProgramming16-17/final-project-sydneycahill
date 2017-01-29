import pandas as pd # import pandas to be able to use the DataFrame, which creates table-like objects
import bokeh # import bokeh to be able to make a variety of charts from within Python
from bokeh.charts import Scatter, output_file, save
# import Scatter from bokeh.charts to be able to make the actual plots
# import output_file to get the function needed to create the html file
# import save to get the function needed to save the html file
df = pd.read_csv('Pokemon.csv%3Fsv%3D2015-12-11%26sr%3Db%26sig%3DZ9S6p8prK6gi7hWD6XW86RbqhRLzWHIH3fjFYz19hAw%3D%26se%3D2017-01-31T01%3A49%3A57Z%26.csv')
# access the data and convert it into a data frame
p = Scatter(df, # create a Scatter chart from the DataFrame
        x  = 'HP', # set HP as the column label to use for the x dimension
        y = 'Speed', # set Speed as the column label to use for the y dimension
        title = 'HP of Pokemon vs. Speed', # set the title of the graph to HP of Pokemon vs. Speed
        xlabel ='HP of Pokemon', # label the x axis as HP of Pokemon
        ylabel = 'Speed of Pokemon', # label the y axis as Speed of Pokemon
        plot_width = 500, # set the width of the plot to 500
        plot_height = 500, # set the height of the plot to 500
        color = 'Type 1', # color the coordinates by Type 1, the type of Pokemon
        marker = 'Type 1', # mark the coordinates by Type 1, the type of Pokemon
        legend = 'top_right') # set the location of the legend to the top right

output_file('scatter2.html') # give the file a name and make it into a visual

save(p) # save the file