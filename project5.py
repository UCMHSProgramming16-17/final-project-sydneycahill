import pandas as pd # import pandas to be able to use the DataFrame, which creates table-like objects
import bokeh # import bokeh to be able to make a variety of charts from within Python
from bokeh.charts import Scatter, output_file, save
# import Scatter from bokeh.charts to be able to make the actual plots
# import output_file to get the function needed to create the html file
# import save to get the function needed to save the html file
df = pd.read_csv('Pokemon.csv%3Fsv%3D2015-12-11%26sr%3Db%26sig%3DZ9S6p8prK6gi7hWD6XW86RbqhRLzWHIH3fjFYz19hAw%3D%26se%3D2017-01-31T01%3A49%3A57Z%26.csv')
# access the data and convert it into a data frame
p = Scatter(df, # create a Scatter chart from the DataFrame
        x = 'Sp. Atk', # set Sp. Atk as the column label to use for the x dimension
        y = 'Sp. Def', # set Sp. Def as the column label to use for the y dimension
        title = 'Sp. Atk vs. Sp. Def', # set the title to Sp. Atk vs. Sp. Def
        xlabel = 'Sp. Atk of Pokemon', # set the x label as Sp. Atk of Pokemon
        ylabel = 'Sp. Def of Pokemon', # set the y label as Sp. Def of Pokemon
        plot_width = 1000, # set the width of the plot to 1000
        plot_height = 1000, # set the height of the plot to 1000
        color = 'violet') # set the color of the graph to violet

output_file('scatter1.html') # give the file a name and make it into a visual

save(p) # save the file