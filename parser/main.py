import json
import requests
import xmltodict
import psycopg2


def persist_data(data):
    # forming connection
    conn = psycopg2.connect(
        host="localhost",
        database="dbtest",
        user="postgres",
        password="Novonoia1!")
    conn.autocommit = True

    sql = "INSERT INTO public.api_disorder VALUES(%s,%s,%s)"

    cursor = conn.cursor()
    cursor.executemany(sql, data)


def loadFile():
    url = 'http://www.orphadata.org/data/xml/en_product4.xml'
    resp = requests.get(url)
    # saving the xml file
    with open('diseases.xml', 'wb') as f:
        f.write(resp.content)


def parseXML(xmlfile):
    list = []
    with open(xmlfile, 'r') as file:
        obj = xmltodict.parse(file.read())

    data = obj['JDBOR']['HPODisorderSetStatusList']['HPODisorderSetStatus']
    for element in data:
        hpo_list = []
        # element['Disorder']['Name'] = element['Disorder']['Name']['#text']
        # element['Disorder']['DisorderType'] = element['Disorder']['DisorderType']['Name']['#text']
        # element['Disorder']['DisorderGroup'] = element['Disorder']['DisorderGroup']['Name']['#text']
        # del element['Disorder']['ExpertLink']
        # del element['Source']
        # del element['ValidationStatus']
        # del element['Online']
        # del element['ValidationDate']

        if len(element['Disorder']['HPODisorderAssociationList']) > 1:
            hpo_elements = element['Disorder']['HPODisorderAssociationList']['HPODisorderAssociation']
            for hpo in hpo_elements:
                hpo_list.append(hpo['HPO']['HPOId'])
                # hpo['HPOId'] = hpo['HPO']['HPOId']
                # hpo['HPOTerm'] = hpo['HPO']['HPOTerm']
                # hpo['HPOFrequency'] = hpo['HPOFrequency']['Name']['#text']
                # del hpo['@id']
                # del hpo['DiagnosticCriteria']
                # del hpo['HPO']
        tuple = (element['Disorder']['OrphaCode'], element['Disorder']['Name']['#text'], hpo_list)
        list.append(tuple)

    # with open('diseases.json', 'w') as f:
    #     json.dump(data, f)
    # return data
    return list


if __name__ == '__main__':
    loadFile()
    data_parsed = parseXML('diseases.xml')
    persist_data(data_parsed)
