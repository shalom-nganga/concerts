#!/usr/bin/env python3
import ipdb;
from lib.Band import Band
from lib.Concert import Concert
from lib.Venue import Venue




if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    
    # create a Band instance
    sauti_sol = Band("Sauti Sol", "Nairobi")
    print(sauti_sol.__dict__)

    # create a Venue instance
    Carnivore = Venue("Carnivore", "Nairobi")
    print(Carnivore.__dict__)  

    # create a concert instance
    sol_fest = Concert("12-12-2023", sauti_sol, Carnivore)
    print(sol_fest.__dict__)
    # print(sauti_sol.name)

    # sauti_sol.hometown = "Nairobi"
    # print(sauti_sol.hometown)
 








# DO NOT REMOVE THIS
    # ipdb.set_trace()
