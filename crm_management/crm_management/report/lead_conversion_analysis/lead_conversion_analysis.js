// Copyright (c) 2025, nidhi-boghara and contributors
// For license information, please see license.txt

// Add filters of Reports
frappe.query_reports["Lead Conversion Analysis"] = {
	"filters": [
		
				{
					"fieldname": "sales_person",
					"label": "Salesperson",
					"fieldtype": "Link",
					"options": "User"
				},
				{
					"fieldname": "customer_name",
					"label": "Customer Name",
					"fieldtype": "Link",
					"options":"Customer"
				},
				{
					"fieldname": "conversion_date_from",
					"label": "Conversion Date From",
					"fieldtype": "Date"
				},
				{
					"fieldname": "conversion_date_to",
					"label": "Conversion Date To",
					"fieldtype": "Date"
				}
			]
}
