import frappe


def on_update(doc, event):
    frappe.msgprint(f"{doc.name} has been updated by {doc.owner}")

def after_insert(doc, event):
    note = frappe.get_doc({
    'doctype':'Note',
    'title': f"Property {doc.name} has been add",
    'public': True,
    'content': f"{doc.property_name} is now available"
    })
    note.insert()
    frappe.db.commit()
    frappe.msgprint(f"Note has been created : <br/> {note.title}")
