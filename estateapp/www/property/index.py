import frappe

def get_context(context):
    try:
        context.docname = frappe.form_dict
        context.details = frappe.get_doc("Property", context.docname.docname)
        context.agent = frappe.get_doc("Agent", context.details.agent)
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), str(e))
        frappe.local.flags.redirect_location = f'{frappe.utils.get_url()}/404'
        raise frappe.Redirect

    return context
