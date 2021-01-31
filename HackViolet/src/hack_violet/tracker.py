import webbrowser, os
from gmplot import gmplot 
from pgeocode import Nominatim
from hack_violet.get_data import check_db

def plot_lat_long(lat, long, city):   
    #plot_lat_long generates a google map and plots the location of the
    #latitude and longitude coordinates as well as the name of the location
    #Using gmplot.
      
    # the initial lat long and the zoom levels for the map as well as initial zoom
    gmap = gmplot.GoogleMapPlotter(lat, long, 10)
    
    #Makes markers easier to find for windows
    if ":\\" in gmap.coloricon:
        gmap.coloricon = gmap.coloricon.replace('/', '\\')
        gmap.coloricon = gmap.coloricon.replace('\\', '\\\\')
    
   
    gmap.marker(lat, long, color = "blue", title = 'Location: '+ city)
    
    # get the currentdirectory
    cwd = os.getcwd()
    # saving the map as an HTML into the project directory
    gmap.draw("traceroute.html")   
    # opening the HTML via default browser
    webbrowser.open("file:///" + cwd +"/traceroute.html")




def find_lat_long(current_zip):
    #find_lat_long takes a zipcode as a parameter and uses pgeocode to 
    #find the latitude and longitude of the zipcode
    #as well as make a reference to the name of the location
    
    geolocator = Nominatim('us')
    lat = geolocator.query_postal_code(current_zip)[-3]
    long = geolocator.query_postal_code(current_zip)[-2]
    current_data = check_db(current_zip)
    
    plot_lat_long(lat, long, current_data['City'])
    
  
    
def registry_website(current_zip):
    #*******Website not creted or owned******* registry_website links
    #to an external resource by City-Data.com which provides location
    #based information about the sex offender registry
    #This link is explicity used as a resource for further information
    
    site = 'http://www.city-data.com/soz/soz-'+current_zip+'.html'
    webbrowser.open(site)