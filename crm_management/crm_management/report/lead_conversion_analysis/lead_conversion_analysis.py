# Copyright (c) 2025, nidhi-boghara and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    if not filters:
        filters = {}

    # Get columns for the report
    columns = get_columns()
    # Fetch data based on the applied filters
    data = get_data(filters)

    return columns, data

def get_columns():
    return [
        {"fieldname": "lead_name", "label": "Lead Name", "fieldtype": "Data", "width": 200},
        {"fieldname": "customer", "label": "Customer Name", "fieldtype": "Data", "width": 200},
        {"fieldname": "sales_person", "label": "Salesperson", "fieldtype": "Data", "width": 150},
        {"fieldname": "lead_status", "label": "Lead Status", "fieldtype": "Data", "width": 120},
        {"fieldname": "custom_lead_conversion_date", "label": "Conversion Date", "fieldtype": "Date", "width": 120}
    ]

def get_data(filters):
    conditions = {}

    # Apply filter for Salesperson
    if filters.get("sales_person"):
        conditions["lead_owner"] = filters["sales_person"]

    # Apply filter for Customer Name
    if filters.get("customer_name"):
        conditions["customer"] = filters["customer_name"]

    # Apply date range filter for conversion date
    if filters.get("conversion_date_from") and filters.get("conversion_date_to"):
        conditions["custom_lead_conversion_date"] = ["between", [filters["conversion_date_from"], filters["conversion_date_to"]]]

    # Fetch filtered leads from the "Lead" doctype
    leads = frappe.get_all(
        "Lead",
        filters=conditions,
        fields=["name as lead_name", "customer", "lead_owner as sales_person", "status as lead_status", "custom_lead_conversion_date"],
        order_by="custom_lead_conversion_date DESC"
    )

    return leads
