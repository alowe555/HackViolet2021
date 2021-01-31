from firebase import firebase

db = firebase.FirebaseApplication('https://hackviolet2021-default-rtdb.firebaseio.com/', None)

#Tempalete for adding data to database
#data = {'City': "New York, New York",
    #     'Total Crime': 3988,
    #    'Violent Crime': 679,
    #    "Avg Property Value": 299920,
    #   "Price Sqr Ft" : 1790
    #  }

#db.put("Zipcode",10001, data)
#--------------------------------------------------------------------
def check_db(input_zipcode):
    #check_db cross checks a zipcode against the database to find
    #stored information
    #If the zipcode is not stored a dictionary of data is not returned, 
    #throwing an error.
    
    dic = db.get('/Zipcode/', '')  
    for key in dic:
        if key == input_zipcode:
            print("zipcode found")
            return dic[str(input_zipcode)]        
    print("zipcode not found")  
    




