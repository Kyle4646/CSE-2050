 
import weather_analysis

def weather_analyze(file_path):
   
    """Analyzes weather data from a file and prints the results.
    Creates dictionary of all the data anayalzed with weather_anaylsis function"""

    
    weather_data = weather_analysis.read_weather_data(file_path)

    data_dict={}
    data_dict['average_temperature'] = weather_analysis.calculate_average_temperature(weather_data)
    data_dict['total_rainfall'] = weather_analysis.calculate_total_rainfall(weather_data)
    data_dict['highest_temperature'] = {'date': (weather_analysis.find_highest_temperature(weather_data))[0], 'temperature:': (weather_analysis.find_highest_temperature(weather_data))[1]}
    data_dict['lowest_temperature'] = {'date': (weather_analysis.find_lowest_temperature(weather_data))[0], 'temperature:': (weather_analysis.find_lowest_temperature(weather_data))[1]}
    data_dict['most_rainfall'] = {'date': (weather_analysis.find_day_with_most_rainfall(weather_data))[0], 'rainfall:': (weather_analysis.find_day_with_most_rainfall(weather_data))[1]}
    return(data_dict)


if __name__ == '__main__':
    results=(weather_analyze('Homeworks/Homework1/weather_data.txt'))
    print(results)