
def read_weather_data(file_path: str):
    
    """ Reads weather data from a file, and returns a list of tuples
    First item is stored as string, second and third are floats.
    Tuples are then made and added to weather_data_list."""
    
    weather_file = open(file_path, 'r')
    weather_data = weather_file.readlines()
    weather_data_list=[]
    
    for line in weather_data:
        line_data = line[:-1]
        line_data = line_data.split(',')
        date=str(line_data[0])
        temperature=float(line_data[1])
        rain=float(line_data[2])
        line_tuple= date, temperature, rain
        weather_data_list.append(line_tuple)  
    
    weather_file.close()
    return(weather_data_list)
        
    




def calculate_average_temperature(weather_data):

    """Calculates the average temperature from the weather data. 
    Takes the second index from each tuple, which are the temperatures and makes a list.
    That list is then summed up and averaged from length of list.
    Simplifies to 2 decimal places for simplicity."""
    
    temperature_list=[]

    for tuple in weather_data:
        temperature_list.append(tuple[1])
    average_temp=(sum(temperature_list))/(len(temperature_list))

    return(average_temp) 




def calculate_total_rainfall(weather_data):
    
    '''This calculates total rainfall by summing up all rainfalls from list of tuples'''
    
    rain_fall_list=[]

    for tuple in weather_data:
        rain_fall_list.append(tuple[2])

    return(sum(rain_fall_list))
    



def find_highest_temperature(weather_data):
    
    """Finds the highest temperature and the corresponding date from the weather data.
    Finds the max of the temperature data list then sees what tuple in the list has max value"""
    
    temperature_list=[]

    for tuple in weather_data:
        temperature_list.append(tuple[1])
   
    for tuple in weather_data:
        if max(temperature_list) == tuple[1]:
            return(tuple[0:2])
    
        



def find_lowest_temperature(weather_data):
    
    """Finds the lowest temperature and the corresponding date from the weather data.
    Finds the min of the temperature data list then sees what tuple in the list has min value"""
    
    temperature_list=[]
    
    for tuple in weather_data:
        temperature_list.append(tuple[1])
    
    for tuple in weather_data:
        if min(temperature_list) == tuple[1]:
            return(tuple[0:2])
    




def find_day_with_most_rainfall(weather_data):
    
    """Finds the day with most rainfall and the corresponding date from the weather data.
    Finds the max of the rainfall data list then sees what tuple in the list has the max rainfall value"""

    rainfall_list=[]
    
    for tuple in weather_data:
        rainfall_list.append(tuple[2])
    
    for tuple in weather_data:
        if (max(rainfall_list)) == tuple[2]:
            return tuple[0], tuple[2]