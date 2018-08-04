#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import re

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Data points: ", len(enron_data)
print "Features: ", len(enron_data[enron_data.keys()[0]])

poi_dataset, n_email, n_sal, total_payments, poi_total_pay =0,0,0,0,0

for i in enron_data:
	if enron_data[i]["poi"]:
		poi_dataset += 1
		if enron_data[i]["total_payments"]=="NaN":
			poi_total_pay += 1
	if enron_data[i]["email_address"]!="NaN":
		n_email += 1
	if enron_data[i]["salary"] != "NaN":
		n_sal +=1
	if enron_data[i]["total_payments"]=="NaN":
		total_payments += 1
		
print "POI in Dataset: ", poi_dataset

poi_all=0
with open("../final_project/poi_names.txt") as f:
	content=f.readlines()
for line in content:
	if re.match(r'\((y|n)\)', line):
		poi_all+=1
print "POI ALL: ", poi_all

print "Stock value of James Prentice:", enron_data["PRENTICE JAMES"]['total_stock_value']
print "Wesley Colwell to POI emails:", enron_data["COLWELL WESLEY"]['from_this_person_to_poi']
print "Stock options of Jeffrey Skilling:", enron_data["SKILLING JEFFREY K"]['exercised_stock_options']

people =("SKILLING JEFFREY K", "FASTOW ANDREW S", "LAY KENNETH L")
who =""
money=0
for i in people:
	if money < enron_data[i]["total_payments"]:
		money=enron_data[i]["total_payments"]
		who = i
	
print "Who took the most money? ",who
print "How much? ",money

print "How many have quantified salary: ",n_sal
print "How many known emails: ",n_email
print "NaN percentage in total payments: ",total_payments/float(len(enron_data))
print "NaN percentage of POIs in total payments: ",poi_total_pay/float(poi_dataset)
