# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:28:59 2022

@author: marin
"""

import requests as r
import json as j

#exporting data from the pokemon API, information related to the characteristics of each pokemon
url = 'https://pokeapi.co/api/v2/pokemon-species/'

names=[]         
def get_pokemon(url,offset,limit):
    #introducing arguments we will list more than the 20 pokemons for default
    args = {'limit': limit, 'offset' : offset} if offset else {}
    response = r.get(url, params=args)
    
    #print(response) is equal to 200 it means that the request was made alright
    if response.status_code == 200:   
        #get the information from the url in json
        payload = response.json()
        #from json to a dictionary with the information about pokemons
        results = payload.get('results',[])    
        #now we get the names of the pokemons listed
        for pokemon in results:
            name = pokemon['name']
            names.append(name)
    return names,results,payload
                    
offset = 300
limit = 300
names,results,payload = get_pokemon(url,offset,limit)


''' now we are going to select more specific information '''

url_base = 'https://pokeapi.co/api/v2/pokemon-species/'

def pokemon_characteristics(url_base,id_number):
    url = url_base +str(id_number)
    response = r.get(url)
    payload = response.json()
    #we get especific information from the selected pokemon
    pokemon_name = payload['name']
    color_description = payload['color']['name']
    habitat = payload['habitat']['name']
    growth_rate = payload['growth_rate']['name']
    egg_groups = payload.get('egg_groups',[]) #we transform the list from the json file to a dictionary
    egg_groups_ = []
    for groups in egg_groups:
        egg = groups['name']
        egg_groups_.append(egg)
    
    return pokemon_name,color_description,habitat,growth_rate ,egg_groups_

pokemon_name,color,habitat,growth_rate,egg_groups = pokemon_characteristics(url_base,3)

#we make a dataset to store everything   
for i in range (1,300):
    data = pokemon_characteristics(url_base,i)
    
#continue...
    