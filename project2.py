import pandas as pd # import pandas to be able to use the DataFrame, which creates table-like objects
import bokeh # import bokeh to be able to make a variety of charts from within Python
from bokeh.charts import Histogram, output_file, save
# import Histogram from bokeh.charts to be able to make the actual plots
# import output_file to get the function needed to create the html file
# import save to get the function needed to save the html file
df = pd.read_csv('Pokemon.csv%3Fsv%3D2015-12-11%26sr%3Db%26sig%3DZ9S6p8prK6gi7hWD6XW86RbqhRLzWHIH3fjFYz19hAw%3D%26se%3D2017-01-31T01%3A49%3A57Z%26.csv')
# access the data and convert it into a data frame
p = Histogram(df, # create a Histogram from the DataFrame
    values = 'HP', # set the value of HP to be used for producing the Histogram using table-like input data
    color = 'Type 1', # set the coordinates to be colored according to Type 1, the type 1 of each Pokemon
    title = "HP Distribution by Pokemon Type", # set the title of the graph as HP Distribution by Pokemon Type
    legend = 'top_right', # set the location of the legend as the top right
    xlabel = 'HP of Pokemon', # label the x axis as HP of Pokemon
    ylabel = 'Number of Pokemon') # label the y axis as Number of Pokemon

output_file("histogram.html",) # give the file a name and make it into a visual

save(p) # save the file
