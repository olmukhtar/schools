from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Student"),
			"items": [
				
				{
					"type": "doctype",
					"name": "Student"
				},
				{
					"type": "doctype",
					"name": "Student Group"
				},
				{
					"type": "doctype",
					"name": "Student Applicant"
				},
				{
					"type": "doctype",
					"name": "Program Enrollment"
				},
				{
					"type": "doctype",
					"name": "Program Enrollment Tool"
				},
				{
					"type": "doctype",
					"name": "Student Group Creation Tool"
				}
			]
		},
		{
			"label": _("Schedule"),
			"items": [
				{
					"type": "doctype",
					"name": "Course Schedule",
					"route": "Calendar/Course Schedule"
				},
				{
					"type": "doctype",
					"name": "Student Attendance"
				},
				{
					"type": "doctype",
					"name": "Scheduling Tool"
				},
				{
					"type": "doctype",
					"name": "Examination"
				}
			]
		},
		{
			"label": _("Fees"),
			"items": [
				{
					"type": "doctype",
					"name": "Fees"
				},
				{
					"type": "doctype",
					"name": "Fee Structure"
				},
				{
					"type": "doctype",
					"name": "Fee Category"
				},
				{
					"type": "report",
					"name": "Student Fee Collection",
					"doctype": "Fees",
					"is_query_report": True
				}
			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Course"
				},
				{
					"type": "doctype",
					"name": "Program"
				},
				{
					"type": "doctype",
					"name": "Instructor"
				},
				{
					"type": "doctype",
					"name": "Room"
				},
				{
					"type": "doctype",
					"name": "Academic Term"
				},
				{
					"type": "doctype",
					"name": "Academic Year"
				}
			]
		},
	]
	