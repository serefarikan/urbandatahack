import csv
import glob
import os

def filter_crime_types(crime_type_dict,items):
    for item in items:
        if not crime_type_dict.has_key(item[9]):
            crime_type_dict[item[9]] = item[9]


os.chdir("c:\\work\\data\\temp\\London-crime-data-from-data.police.org")  
f_names = []
for file in glob.glob("*.csv"):
    f_names.append(file)
    
def get_crime_data():
    ds = []
    for f in f_names:
        temp_lst = []
        crime_file = open(f,'r')
        rd = csv.reader(crime_file)
        for row in rd:
            temp_lst.append(tuple(row))
        ds.extend(temp_lst[1:])
        crime_file.close()
    return ds       

ds = get_crime_data()

crime_type_dict = {}
filter_crime_types(crime_type_dict,ds)

def sanitize_ct_dict(ct_src_dict):
    ct_dict = {}
    for key in ct_src_dict.keys():
        if key == 'Anti-social behaviour':
            ct_dict[key] = 'anti-social-behaviour'
        elif key == 'Burglary':
            ct_dict[key] = 'burglary'
        elif key == 'Bicycle theft':
            ct_dict[key] = 'bicycle-theft'
        elif key == 'Criminal damage and arson':
            ct_dict[key] = 'criminal-damage-arson'
        elif key == 'Drugs':
            ct_dict[key] = 'drugs'
        elif key == 'Other crime':
            ct_dict[key] = 'other-crime'
        elif key == 'Other theft':
            ct_dict[key] = 'other-theft'
        elif key == 'Possession of weapons':
            ct_dict[key] = 'possession-of-weapons'
        elif key == 'Public disorder and weapons':
            ct_dict[key] = 'public-disorder-weapons'
        elif key == 'Public order':
            ct_dict[key] = 'public-order'
        elif key == 'Robbery':
            ct_dict[key] = 'robbery'
        elif key == 'Shoplifting':
            ct_dict[key] = 'shoplifting'
        elif key == 'Theft from the person':
            ct_dict[key] = 'theft-from-the-person'
        elif key == 'Vehicle crime':
            ct_dict[key] = 'vehicle-crime'
        elif key == 'Violence and sexual offences':
            ct_dict[key] = 'violent-sex-offence'
        elif key == 'Violent crime':
            ct_dict[key] = 'violent-crime'
        else:
            ct_dict[key] = 'UNKNOWN'
    return ct_dict

longitude = 4
latitude = 5
san_crime_type_dict = sanitize_ct_dict(crime_type_dict)
#account for empty long/lat
coords = [(c[latitude],c[longitude],san_crime_type_dict[c[9]]) for c in ds if c[latitude] != '' and c[longitude] != '']
locs_statements = ['locs.push({lat:' + c[0] + ',lon:' + c[1] + ',cat:\'' + c[2] +'\'});' for c in coords]

ftest = open('c:\\work\\data\\temp\\test.txt','w')
ftest.write(''.join(locs_statements[-10000:]))
ftest.close()

