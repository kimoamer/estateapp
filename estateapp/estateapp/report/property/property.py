# Copyright (c) 2022, test and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	return get_columns(), get_data(filters)

def get_columns():
	return [
		"ID:Link/Property:70",
		"Property Name:Data:150",
		"Type:Data:80",
		"Agent:Data:150",
		"Status:Select:70",
	]

def get_data(filters):
	_from = filters["from"]
	to = filters["to"]
	conditions = ''
	if (filters.get('property')): conditions += f" AND property_name LIKE '%{filters.get('property')}%'"
	if (filters.get('agent')): conditions += f" AND agent='{filters.get('agent')}'"
	list = frappe.db.sql(f"""SELECT name,property_name,property_type,agent,status FROM tabProperty WHERE (creation BETWEEN '{_from}' AND '{to}') {conditions}""")
	return list
