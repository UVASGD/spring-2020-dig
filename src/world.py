from threading import Thread
import time
import nwtworkx as nx

class World(Thread):
    
    done = False
    
    locations = nx.Graph()
    
    xy_locs = list(list(list()))
    xz_locs = list(list(list()))
    yz_locs = list(list(list()))
    
    def __init__(self, save):
        
        Thread.__init__(self)

    def run(self):
        
        while not self.done:
            time.sleep(.1)
            self.tick()
            
    def tick(self):
        
        for location in list(self.locations.nodes):
            location.update()
            
            
    def add_location(self, loc):
        
        locations.add_node(loc)
        
        xy_locs[loc.coordinates[0]][loc.coordinates[1]].append(locations)
        xz_locs[loc.coordinates[0]][loc.coordinates[2]].append(locations)
        yz_locs[loc.coordinates[1]][loc.coordinates[2]].append(locations)
        
        
    
    
    
    
    
    
            
        
