# #les2 opdracht 1 integers

# from operator import truediv

import math

people = 7861304740
print(people)
people = 7_861_304_740
print(people)

meals = 3
people_eat = people * meals
print(people_eat)

days = 365
meals_per_year = people_eat * days
print(meals_per_year)

type(meals_per_year)


#opdracht2 float

# Ethernet capacity
ethernet_speed_mbps = 1000
efficiency = 0.7
maximum_capacity = ethernet_speed_mbps * efficiency
print(maximum_capacity)

#print capacity used on ethernet
download_speed_average = 96.25
usage = ethernet_speed_mbps / download_speed_average
print(usage)

# speed of light in m/s

speed_of_light = 299_792_458

# Distance Rotterdam / New york in km
distance_Rotterdam_NewYork= 5_862.03
time_to_reach_NYC = (distance_Rotterdam_NewYork * 1000) / speed_of_light
print(time_to_reach_NYC)

type(time_to_reach_NYC)


#opdracht3 String
ship = 'Titanic'
print(ship)
# let op: in de zin is een apostrof gebruikt
# Dat kan bij dubbele aanhalingstekens
sentence= "He doesn’t think it’s a good idea to spend all his money on videogames."
print(sentence)

# Gebruik """ """ als je meerdere regels tekst moet tonen
paragraph = """Computer Technology means all designs, drawings, procedures(including design, manufacturing, test and maintenance procedures),specifications, software (other than as described within the meaning of the term"Software" defined elsewhere herein), printed circuit board art work, integratedcircuit masks, test equipment, tools, fixtures, documentation, training materials,and information, in whatever form, related to, useful, utilizable or necessary inthe design, manufacture, test and/or maintenance of the computer system, or relateto any Technology Licenses."""
print(paragraph)

# Met len kan je vragen hoeveel karakters er in de string zitten
characters_in_paragraph = len(paragraph)
print(f"{paragraph}\n\nThe paragraph has {characters_in_paragraph} characters.")

year = 1936
inventor = "Alan Turning"
name_of_machine = "automatic machine"
# Let op: In de tekst zijn dubbele aanhalingstekens gebruikt.# De string zelf moet dan met iets anders beginnen. In dit geval enkele# aanhalingstekens
invention= f'The Turing machine was invented in {year} by {inventor}, who calledit an "a-machine" ({name_of_machine}).'
print(invention)

#welke datatype is het?
type(invention)

#opdracht3 Boolean

logged_in = False
print(logged_in)

netwerk_activity = True
print(netwerk_activity)

user_name = "John Doe"
entered_name = input("User name, please: ")
size_user_name = len(user_name)
size_entered_name = len(entered_name)
user_name_is_bigger = size_user_name > size_entered_name
entered_name_is_bigger = size_entered_name > size_user_name
print(f"The user name {user_name} has more characters then the entered name {entered_name} is: {user_name_is_bigger}")
print(f"The entered name {entered_name} has more characters then the user name {user_name} is: {entered_name_is_bigger}")

lights_on = False
lock_closed = True
# Not keert de waarde van een boolean om not True is hetzelfde als False# Andersom is not False dus True
alarm_activated = not lights_on and lock_closed
print(f"The alarm is  activated, is: {alarm_activated}")


y= math.sqrt(3*9.1-1)+(1+9.1)**2
print(y)

# y= -2.7+math.sqrt(2.7**2-4*0.87+5.03) /2*0.87
# print(y)


containers_gelost= 331
minuten_gelost_min= 441 
geladen_containers= 287
minuten_geladen= 295

x= gemiddelde_tijd_lossen= minuten_gelost_min / containers_gelost
y= gemiddelde_tijd_lossen= minuten_geladen / geladen_containers

delta= 4*1 / (179875474.8*(1-179875474.8**2 / 299792458**2)
print(delta)


