from os import listdir
from os.path import isfile, join

import csv
import pandas as pd
import json

def readFiles(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print('listing files...')
    edges_list = []
    for file in onlyfiles:
        f = open(mypath+"\\"+file,)
        data = json.load(f)
        for ref in data['bib_entries']:
            edges_list.append([data['metadata']['title'], data['bib_entries'][ref]['title']])
        f.close()
    return edges_list

def writeTitleEdges():
    finalList = readFiles("C:\\Users\isilva\Downloads\document_parses\pdf_json") + readFiles("C:\\Users\isilva\Downloads\document_parses\pmc_json")
    with open('fileEdges', 'w', encoding="utf-8") as f:
        print('writing...')
        write = csv.writer(f)
        write.writerows(finalList)

def openMetadata():
    my_file = open('metadata.csv', encoding="utf-8")
    data = pd.read_csv(my_file, usecols=[3,0])
    return data

def ccleanEdges(metadata):
    filtered = []
    titlesUsed = []
    my_file = open('fileEdges', encoding="utf-8")
    data = csv.reader(my_file)
    for edge in data:
        if len(edge)>0 and edge[0] != '' and edge[1] != '' and edge[0]+edge[1] not in titlesUsed:
            filtered.append(edge)
            titlesUsed.append(edge[0]+edge[1])
    print('was {} files... now its {}',len(data), len(filtered))
    with open('fileEdgesFiltered', 'w', encoding="utf-8") as f:
        print('writing...')
        write = csv.writer(f)
        write.writerows(filtered)

        
def cleanEdges(metadata):
    my_file = open('fileEdges', encoding="utf-8")
    data = pd.read_csv(my_file, header=None)
    print('replacing names...')
    for index, row in metadata.iterrows():
        if index > 0:
            data[0].replace({row[1]: row[0]})
            data[1].replace({row[1]: row[0]})
    data.to_csv("uids_net.csv")

metadata = openMetadata()
cleanEdges(metadata)