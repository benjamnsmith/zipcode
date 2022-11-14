import csv

states_all = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


def prettyPrint(dic):

    for elem in dic: 
        print("{} | ${:>13,.2f} ".format(elem, dic[elem]))


def avgAll(reader):
        pass


def process(inp):

    try:
        if 2019 >= int(inp) >= 2013:
            fn = f"./data/{inp[2:]}zpallagi.csv"
            print()
        else:
            print("Year format not recognized, or no data on this year")
            return
    except ValueError:
        if inp in states_all:
            print(f"Looks like you entered a state {inp}")
            print(len(states_all))
        else:
            print("State format not recognized")
        
        return

    fh = open(fn, "r", newline='')

    reader = csv.reader(fh)

    agis = {}
    tias = {}

    agi_idx = 0
    tia_idx = 0


    for line in reader:
        state = line[1]

        try:
            agi = float(line[agi_idx])
            tia = float(line[tia_idx])
        except ValueError:
            agi_idx = line.index("A00100")
            tia_idx = line.index("A02650")
            continue

        if state in agis:
            agis[state] = (agis[state] + agi) / 2
            tias[state] = (tias[state] + tia) / 2
        
        else:
            agis[state] = agi
            tias[state] = tia

    fh.close()

    print("Average AGI per state in %d: " % int(inp))
    prettyPrint(agis)
    print("\nAverage TIA per state in %d: " % int(inp))
    prettyPrint(tias)



def user_interface():
    print("\nZIP CODE DATA ANALYSIS")
    print("Please enter a year (2013-2019, inclusive):")
    process(input(">> "))

    


user_interface()


"""
What is the average AGI per state? 
For a given state, which zip codes have the highest average AGI? 

"""