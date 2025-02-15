# Copyright (c) 2025, nidhi-boghara and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CustomerInteractionLog(Document):
    
    def after_insert(self):
        # Check if the current document has a customer linked to it
        if self.customer:
            # Fetch the name of the Lead associated with the given customer (if exists)
            lead = frappe.get_value("Lead", {"customer": self.customer}, "name")
            
            # If a Lead exists for the customer, update its 'custom_next_contact_date' field
            if lead:
                frappe.db.set_value("Lead", lead, "custom_next_contact_date", self.follow_up_date)
                
                # Commit the changes to the database to ensure the update is saved
                frappe.db.commit()  # nosemgrep (used to suppress linting warnings)
