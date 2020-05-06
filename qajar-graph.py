
#!This code make a graph visualization of data in qajarwomen.com

# *Importing required libraries
from pyvis.network import Network
import json
file = 'data.json'

# *Defining a function for getting json data


def get_data():
    with open(file, 'r', encoding='utf_8') as json_file:
        data = json.load(json_file)
        return(data['data'])

# *Defining a function for making graph


def map_data(qajar_data, name_color='#a0b038', relative_color='#38b03e',
             edge_color='#018786', name_shape='ellipse', relative_shape='box', buttons=False, name_size=100,
             relative_size=100, name_title='', name_image='', relative_image=''):
    # make a graph named g
    g = Network(height='1500px', width='100%',
                bgcolor='black', font_color='white')
    # show buttons if we call this fuction later with argument buttons=True
    if buttons == True:
        g.width = '65%'
        g.show_buttons()
    # make an empty list (qajarnames) to fill it by all the names
    qajarnames = []
    # parsing the data in json file
    for qajar in qajar_data:
        nam = (qajar['name'])
        namimag = (qajar['image'])
        relat = (qajar['relatives'])
        # set the number of relatives of each name to size of its node
        namessize = len(relat)*10
        # add a node for each name in data
        g.add_node(nam, color=name_color,
                   shape=name_shape, image=namimag, physics=False, size=namessize, title=relat)
        # fill the list of all names
        qajarnames.append(nam)
    # add edges between each name and its relative if...
    for qajar in qajar_data:
        nam = (qajar['name'])
        namimag = (qajar['image'])
        relat = (qajar['relatives'])
        # if the relative has node already...
        for eachrelative in relat:
            # if the relative doesn't have node, add one(this didn't occur in our case)
            if eachrelative not in qajarnames:
                g.add_node(eachrelative, color=relative_color,
                           shape=relative_shape, physics=False, size=relative_size)
            # add edges between names and their relatives
            g.add_edge(nam, eachrelative, color=edge_color)
    # the algorithm for model for visualizing data
    g.barnes_hut()
    # show an html of this interactive graph
    g.show('qajar.html')
    g.save_graph('qajar.html')


# use the function get data and name the returned data as names_data
names_data = get_data()
# use the function of map_data and make a graph or network of names_data
map_data(names_data, name_shape='circularImage', relative_shape='dot',
         buttons=False, name_title='relatives')
