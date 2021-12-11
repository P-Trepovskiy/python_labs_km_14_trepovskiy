import csv

with open('Madvillain.csv', 'w', newline='') as csvfile:
    fieldnames = ['Song', 'Year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    songs = ['Boulder Holder', 'All Caps', 'Figaro', 'Accordion', 'Curls', 'Monkey Suit', 'Running Around With Another']
    years = ['2008', '2004', '2004', '2004', '2004', '2008', '2008']
    for i, j in zip(songs, years):
        writer.writerow({'Song': i, 'Year': j})
    print(csvfile.name)

with open('Madvillain.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        print(f'Song: {i["Song"]}, Year: {i["Year"]}')