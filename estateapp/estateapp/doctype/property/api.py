import frappe

@frappe.whitelist()
def check_property_type(property_type):
    sql = frappe.db.sql(f"""SELECT name, property_type FROM tabProperty WHERE property_type='{property_type}';""", as_dict=True)
    return sql
