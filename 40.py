cities = {"sa":"san fransisco","la":"los angles"}

def find_city(themap,state):
    if state in themap:
        return themap[state]

    else:return "not found"

cities['_find'] = find_city
 
while True:
    print "state?"

    state=raw_input(">")

    if not state:break

    city_found= cities['_find'](cities,state)

    print city_found
