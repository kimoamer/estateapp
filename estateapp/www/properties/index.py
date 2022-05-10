import frappe

def get_context(context):
    context.properties = frappe.db.sql("SELECT name,property_name,address,property_type,property_price,status,image FROM tabProperty ORDER BY creation DESC LIMIt 5", as_dict=True)
    return context
