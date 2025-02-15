import frappe
from frappe.utils import nowdate

def send_lead_notification(doc, method):
    """Send an email notification when a Lead moves to 'In Progress'."""
    if doc.workflow_state == "In Progress":
        # Get the Lead Owner (Assigned Salesperson)
        lead_owner = doc.lead_owner if doc.lead_owner else None
        
        if lead_owner:
            # Fetch Salesperson Email
            recipient_email = frappe.db.get_value("User", lead_owner, "email")
            
            if recipient_email:
                # Prepare Email Content
                subject = "Lead Status Update: In Progress"
                message = f"""
                <p>Dear {lead_owner},</p>
                <p>The lead <strong>{doc.name}</strong> has been moved to <strong>'In Progress'</strong>.</p>
                <p><strong>Lead Name:</strong> {doc.lead_name}</p>
                <p><strong>Customer Name:</strong> {doc.customer if doc.customer else 'N/A'}</p>
                <p><strong>Next Contact Date:</strong> {doc.custom_next_contact_date if doc.custom_next_contact_date else 'Not Set'}</p>
                <p>Best Regards,<br>Your CRM Team</p>
                """

                # Send Email
                frappe.sendmail(
                    recipients=[recipient_email],
                    subject=subject,
                    message=message
                )

            # Create Notification Log
            notification_doc = frappe.get_doc({
                "doctype": "Notification Log",
                "subject": "Lead Moved to In Progress",
                "email_content": message,
                "for_user": lead_owner,
                "document_type": "Lead",
                "document_name": doc.name
            })
            notification_doc.insert(ignore_permissions=True)

            
        




def update_conversion_date(doc, method):
    """
    Set the lead conversion date when the lead is linked to a Customer or Opportunity.
    """
    if doc.status == "Converted" and not doc.custom_lead_conversion_date:
        doc.custom_lead_conversion_date = nowdate()
        doc.save(ignore_permissions=True)
