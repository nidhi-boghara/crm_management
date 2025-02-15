frappe.ui.form.on("Lead", {
    refresh: function (frm) {
        // Check if the 'custom_next_contact_date' field exists in the Lead document
        if (frm.doc.custom_next_contact_date) {
            // Convert the 'custom_next_contact_date' field value to a JavaScript Date object
            let next_contact_date = new Date(frm.doc.custom_next_contact_date);
            
            // Get the current date
            let today = new Date();
            
            // Calculate the time difference (in milliseconds) between today and the next contact date
            let diffTime = today - next_contact_date;
            
            // Convert the time difference from milliseconds to days
            let diffDays = diffTime / (1000 * 3600 * 24);

            // Check if the difference is more than 7 days and the Lead status is not "Converted"
            if (diffDays > 7 && frm.doc.status !== "Converted") {
                // Display a warning message to the user
                frappe.msgprint({
                    title: __("Warning"),  // Set the title of the message
                    message: __("Lead Status is not updated within 7 days after the Next Contact Date!"),  // Message content
                    indicator: "red"  // Display a red indicator for warning
                });
            }
        }
    },
});
