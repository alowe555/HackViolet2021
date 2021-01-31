#Runner: This module holds the dictionary and runs the program tools
#from compare_crime_data import plot_graph_crime, plot_graph_housing
#from builtins import int
from hack_violet.data_visuals import plot_graph_crime, plot_graph_housing
from hack_violet.tracker import find_lat_long, registry_website

zipcode = input("Type zipcode: ")    
zipcode = str(zipcode)
if len(zipcode) == 5:    
    plot_graph_crime(zipcode)
    plot_graph_housing(zipcode)
    find_lat_long(zipcode)
    registry_website(zipcode)
else:
    print("Input Invalid")
    quit




