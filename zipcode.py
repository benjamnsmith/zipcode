import csv, locale
locale.setlocale(locale.LC_ALL, '')


def prettyPrint(dic):

    for elem in dic: 

        amt = dic[elem]

        print("%5s | $%.2f " % (elem, locale.currency( float(amt) ) ) )


def process(year):
    fn = ""
    if year == "2019":
        fn = "./data/17zpallagi.csv"
    elif year == "2018":
        fn = "./data/18zpallagi.csv"
    elif year == "2017":
        fn = "./data/19zpallagi.csv"
    
    else:
        print("Year format not recognized, or no data on this year")
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
            print(state, line[tia_idx], line[agi_idx])
            continue

        if state in agis:
            agis[state] = (agis[state] + agi) / 2
            tias[state] = (tias[state] + tia) / 2
        
        else:
            agis[state] = agi
            tias[state] = tia

    print("Average AGI per state in %d: " % int(year))
    prettyPrint(agis)
    print("\nAverage TIA per state in %d: " % int(year))
    prettyPrint(tias)



def user_interface():
    print("ZIP CODE DATA ANALYSIS")
    print("Please enter a year:")
    process(input(">> "))

    


user_interface()


"""
What is the average AGI per state? 
For a given state, which zip codes have the highest average AGI? 


"""