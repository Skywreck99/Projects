# **********************************************************************
# Slide #9: Dictionaries and JSON Files
# **********************************************************************
# JSON file is a dict with a single key-value pair
# {data:[day1, day2, ..., day48 ]}
# You can see 48 in the header next the "cnt" key
# Each list element like day1 is a more complex dictionary 
# day1 = {attr1: value1, attrib2: value2, ... }
# where most of the attributes are dictionaries themselves.
# There are 5 sub-dictionaries:
# * main (with temperature, humidity and pressure info)
# * wind (with speed, gust and angle)
# * clouds (with percent cloud cover)
# * weather (with id, main designator, description and icon)
# * rain observations (largely absent except for rainy days, of course)
# There is also a date/time key-pair right before rain dict.
# The units of various observations take some time to figure out, for
# example, the temperature is in degrees Kelvin, etc..
# Since we are going to concentrate on counts, rather then measures,
# it's OK to ignore most of these numbers at the moment.
# **********************************************************************
# Note: The objective is to determine the frequency of weather 
# conditions: Clear, Clouds, Rain, and Thunderstorm (as it turns out) 
# and also list the percent cloud cover for each of these conditions. 
# While this can be done in a number of different ways, we will build
# the two dictionaries: weather_conds and cloud_cover to do the job.
# **********************************************************************
import json

def main():
  # Open JSON file for reading
  in_json_file = open('MSP.json', 'r')

  # Load the data to deserialize JSON file
  msp_data = json.load(in_json_file)

  # Close the file
  in_json_file.close()

  # Use the 'data' key to reference the value, which is
  # a list of 5 elements, each of which is a sub-dictionary
  # representing different weather related info.
  num_readings = len(msp_data['data'])

  # Create a dictionary of weather conditions, where the key
  # key is the condition, like Clear and the value is the
  # frequency of occurrence
  weather_conds = {}

  # At the same time, create another dictionary of cloud cover,
  # where the key is also the weather condition, and the value
  # is the list of percent cloud cover for that condition
  cloud_cover = {}

  for i in range(num_readings):
    # Weather is a one element sublist of the data list, and
    # that element is a dictionary with 4 key-value pairs,
    # one of which is called "main" and has the value for
    # the "main weather condition" on that day
    wc = msp_data['data'][i]['weather'][0]['main']

    # The cloud cover is right above the weather, but instead
    # of being a one element sublist, it is a one element
    # dict, notice the absence of [] when compared to above 
    cc = msp_data['data'][i]['clouds']['all']

    # Check if this weather condition is already in
    # the weather condition dict
    if wc in weather_conds:
      # Increment the value by one
      weather_conds[wc] += 1
    # Otherwise add the weather condition to the list with
    # the initial value of 1
    else:
      weather_conds[wc] = 1

    # Check if weather condition already in the cloud cover dict
    if wc in cloud_cover:
      # Add the percent cloud cover to the list
      cloud_cover[wc].append(cc)
    # Otherwise add the weather condition with the
    # cloud cover - notice this initializes the list
    else:
      cloud_cover[wc] = [cc]

  # Print the weather condition frequency dict
  for key in weather_conds:
    print(key, weather_conds[key])
    
  print()

  # Print the weather condition cloud cover dict
  for key in cloud_cover:
    print(key, cloud_cover[key])

# Call main()
if __name__ == '__main__':
  main()
