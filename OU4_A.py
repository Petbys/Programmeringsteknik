def load_csv(filename):
    
    import csv

    with open(filename, 'r') as csvFile:
        reader = csv.reader(csvFile)
        d={}
        for row in reader:
            if row[1] == 'Country Code':
                continue
            landskod = row[1].lower()
            utslapp = [float(s) for s in row[3:]]
            d[landskod]= utslapp
    return d
data=load_csv('CO2Emissions_filtered.csv')
print(data)