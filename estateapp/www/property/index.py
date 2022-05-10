import frappe

def get_context(context):
    context.details = frappe.get_doc("Property", "000002")
    context.agent = frappe.get_doc("Agent", context.details.agent)
    return context
