# Copyright (c) 2022, test and contributors
# For license information, please see license.txt


from frappe.model.document import Document
import frappe


class Property(Document):
    pass
    # def validate(self):
    #     if self.property_type == "Flat":
    #         for amenity in self.amenities:
    #             if amenity.amenity == "Balcony":
    #                 frappe.throw((f"can't add Balcony to {self.name} Property"))

    # def validate(self):
    #     frappe.msgprint((f"Saved "))
    #     sql = frappe.db.sql(f"""SELECT * FROM `_5767dd9ad659b88b`.`tabProperty Amenity Details` ;""", as_dict=True)
    #     html = ''
    #     for item in sql[0].keys():
    #         html += str(item)
    #     frappe.msgprint((f"Saved {sql[0]}"))
