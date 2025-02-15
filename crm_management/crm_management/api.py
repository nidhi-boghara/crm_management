import frappe
from frappe import _

@frappe.whitelist(allow_guest=True,methods='GET')
def get_lead_details(lead_status=None, sales_person=None):
    """Fetch lead details based on lead status and salesperson filters."""
    filters = {}

    # Apply filter for Lead Status if provided
    if lead_status:
        filters["status"] = lead_status
    # Apply filter for Salesperson if provided
    if sales_person:
        filters["lead_owner"] = sales_person  # Assuming lead_owner is the salesperson

    # Fetch lead records from the "Lead" doctype based on the applied filters
    leads = frappe.get_all(
        "Lead",
        filters=filters,
        fields=["name as lead_name", "company_name as customer_name", "lead_owner as salesperson", "status", "custom_next_contact_date"],
    )
    # If no leads are found, return a 204 No Content response
    if not leads:
        frappe.local.response.http_status_code = 204
        return {"status": "no_content", "message": "No leads found"}

    return {"status": "success", "data": leads}
