

from fetching_database import store_data
import math
import time
import sys

def coordinates(item):
    data=store_data()
    item=input("enter the items :")
    if item in data:
        a=data[item]['latitude']
        b=data[item]['longitude']
        print(f'{item} is\n latitude: {a} \n and \n longitude: {b}')
        return (a,b)
    else:
        print("code exited because invalid input")
        return None

def details(item):
    data=store_data()
    if item in data and data[item]["type_airport"]=="small_airport":
        print(data[item])
        print(data[item]["name"],data[item]["continent"],data[item]["country"],data[item]["gps_code"])


def country():
    countries=[]
    count=0
    data=store_data()
    for item  in data:
        if data[item]['country'] not in countries:
            countries.append(data[item]['country'])
            print(data[item]["continent"])

            count+=1
    print(countries)
    print(count)

def calculate_distance(lat1,long1,lat2,long2):
    radius=6371 #earth radius

    #converting the latitude and longitude to radians
    rad_lat1=math.radians(lat1)
    rad_long1=math.radians(long1)
    rad_lat2=math.radians(lat2)
    rad_long2=math.radians(long2)
    new_lat=math.radians(lat2-lat1)
    new_long=math.radians(long2-long1)
    #now using the haversine formula to calculate distance
    a = math.sin(new_lat / 2) ** 2 + math.cos(rad_lat1) * math.cos(rad_lat2) * math.sin(new_long / 2) ** 2
    c=2*math.asin(math.sqrt(a))
    distance=radius*c
    print(distance)
    return distance

def calculate_coordinates(lat,long1,distance,degree):
    radius=6371 #earth radius in km

    rad_lat=math.radians(lat)
    rad_long=math.radians(long1)
    rad_degree=math.radians(degree)

    #angular distance
    a_distance=distance/radius

    latitude=math.asin(math.sin(rad_lat)*math.cos(a_distance)+math.cos(rad_lat)*math.sin(a_distance)*math.cos(rad_degree))
    longitude= rad_long+ math.atan2(math.sin(rad_degree)*math.sin(a_distance)*math.cos(rad_lat),math.cos(a_distance)-math.sin(rad_lat)*math.sin(latitude))

    latitude= math.degrees(latitude)
    longitude= math.degrees(longitude)
    # print(latitude,longitude)
    return (latitude,longitude)


def current_location(lat,longi,silent=False):
    data=store_data()
    tolerance=0.002 #this generally helps with the small difference
    for item in data:
        if (abs(float(data[item]['latitude'])-lat))<=tolerance and (abs(float(data[item]['longitude'])-longi))<=tolerance:

            a=data[item]["name"]
            b=data[item]['continent']
            c=data[item]['gps_code']
            d=data[item]['ident']
            e=data[item]['airport_name']
            if not silent: #small changes because it kept printing
               type_with_cursor(    f'Your Current Location is :\n\033[32m[AIRPORT NAME]: {e}\033[0m \n[CONTINENT]: {b}\n[COUNTRY]: {a}\n[gps_code]: {c}\n')

            return d

    if not silent:
        print("Location not found")
    return None



def radar(lat,lon,radius_km=500,ident=None):
    data=store_data()
    nearby_airports={}

    lat_diff=radius_km/111
    lon_diff=radius_km/(111*math.cos(math.radians(lat)))

    for item in data:
        lat1=float(data[item]['latitude'])
        lon1=float(data[item]['longitude'])


        if(abs(lat1-lat)<=lat_diff) and (abs(lon1-lon)<=lon_diff):
            nearby_airports[item]=data[item]
    a=[]
    for items in nearby_airports:
        if nearby_airports[items]['type_airport']=="large_airport" and items!=ident:
            a.append(nearby_airports[items])
    return a


import sys
import time

def type_with_cursor(text, speed=0.01, cursor='_', blip_speed=0.2, blip_times=1):
    """
    Prints text one character at a time with a blinking cursor effect at the end.

    Parameters:
    - text: str, the string to print
    - speed: float, delay between characters
    - cursor: str, the character to blink at the end
    - blip_speed: float, how fast the cursor blinks
    - blip_times: int, number of times the cursor blinks after finishing text
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)

    # Blinking cursor after finishing
    for _ in range(blip_times):
        print(cursor, end='', flush=True)
        time.sleep(blip_speed)
        print('\b \b', end='', flush=True)  # erase the cursor
        time.sleep(blip_speed)
    print()  # move to the next line

def blip_line(text, blip_speed=0.3):
    """
    Makes an entire line of text blink twice (appear and disappear).

    Parameters:
    - text: str, the line to blip
    - blip_speed: float, time in seconds for each blink
    """
    for _ in range(2):  # blink exactly twice
        print(text, end='\r', flush=True)  # show text
        time.sleep(blip_speed)
        print(' ' * len(text), end='\r', flush=True)  # erase text
        time.sleep(blip_speed)
    print(text)





def line_by_line_print(lines, pause=1.0):
    """
    Prints each line immediately, waits for a pause, then prints the next line.

    Parameters:
    - lines: list of str, each string is a full line to print
    - pause: float, seconds to wait before printing the next line
    """
    for line in lines:
        print(line)       # full line prints instantly
        time.sleep(pause)




import winsound  # Windows-only


def type_with_sound(text, speed=0.05, cursor=None, blip_speed=0.2, frequency=800, duration=30):
    """
    Prints text with typing effect and optional blinking cursor,
    with a typing sound for each character.

    Parameters:
    - text: str, the text to print
    - speed: float, delay between characters
    - cursor: str or None, optional blinking cursor character at the end
    - blip_speed: float, cursor blink speed if cursor is used
    - frequency: int, pitch of typing sound in Hz
    - duration: int, duration of each typing sound in ms
    """
    for char in text:
        print(char, end='', flush=True)
        winsound.Beep(frequency, duration)  # typing sound
        time.sleep(speed)

    # optional blinking cursor at the end
    if cursor:
        print(cursor, end='', flush=True)
        time.sleep(blip_speed)
        print('\b \b', end='', flush=True)

    print()  # move to next line


















