import frappe

@frappe.whitelist()
def get_sales_charges(doc):
    additional_charges = frappe.db.get_all("Sales Charges Details", {'parent': doc.name}, ['charge', 'amount'])

    return additional_charges


@frappe.whitelist()
def get_total_payable(doc):
    invoice_amount = frappe.db.get_value("Sales Invoice", {'name': doc.name}, ['grand_total'])

    additional_charges = frappe.db.get_all("Sales Charges Details", {'parent': doc.name}, ['amount'])

    total_additional_charges = 0
    for new_charge in additional_charges:
        total_additional_charges = total_additional_charges + new_charge['amount']

    return total_additional_charges