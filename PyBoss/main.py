import os
import csv
from datetime import datetime

csvpath = os.path.join('employee_data.csv')
output_path = os.path.join('PyBank','Resources','outfile.txt')

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


data = csv.DictReader(open(csvpath))
first_name = []
last_name = []
lastfour = []
current_format = "%Y-%m-%d"
new_format = "%m/%d/%Y"
emp_states = []
for d in data:
    empid = int(d['Emp ID'])
    name = str(d['Name'])
    first = name.split()[0]
    last = name.split()[1]
    first_name = first
    last_name = last
    dob = str(d['DOB'])
    currentdob = datetime.strptime(dob,current_format)
    newdob = currentdob.strftime(new_format)
    ssn = str(d['SSN'])
    last = ssn.split('-')[2]
    lastfour = '***-**-'+last
    state_abbr = us_state_abbrev[d['State']]
    # emp_states = emp_states + [state_abbr]
    # for key, value in us_state_abbrev.items():
    #     if value == state_abbr:
    #         emp_states = value
    print(empid,first_name,last_name,newdob,lastfour,state_abbr)