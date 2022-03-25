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

    sql = "INSERT INTO public.api_app_disease VALUES(%s,%s,%s)"

    cursor = conn.cursor()
    cursor.executemany(sql, data)
    conn.close()


def load_file():
    url = 'http://www.orphadata.org/data/xml/en_product4.xml'
    resp = requests.get(url)
    # saving the xml file
    with open('diseases.xml', 'wb') as f:
        f.write(resp.content)


def parse_xml(xmlfile):
    parsed_list = []
    frequencies = ["Obligate", "Very frequent"]
    with open(xmlfile, 'r') as file:
        xml_file = xmltodict.parse(file.read())

    root = xml_file['JDBOR']['HPODisorderSetStatusList']['HPODisorderSetStatus']
    for element in root:
        hpo_list: list[str] = []
        if len(element['Disorder']['HPODisorderAssociationList']) > 1:
            hpo_elements = element['Disorder']['HPODisorderAssociationList']['HPODisorderAssociation']
            for hpo in hpo_elements:
                if any(value in str(hpo['HPOFrequency']['Name']['#text']) for value in frequencies):
                    hpo_list.append(hpo['HPO']['HPOId'])
        tuple = (element['Disorder']['OrphaCode'], element['Disorder']['Name']['#text'], hpo_list)
        parsed_list.append(tuple)

    return parsed_list


if __name__ == '__main__':
    load_file()
    data_parsed = parse_xml('diseases.xml')
    persist_data(data_parsed)
