from . import __version__ as app_version
from route import routes

app_name = "estateapp"
app_title = "Estateapp"
app_publisher = "test"
app_description = "Estate App manager"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "test@test.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/estateapp/css/estateapp.css"
# app_include_js = "/assets/estateapp/js/estateapp.js"

# include js, css files in header of web template
# web_include_css = "/assets/estateapp/css/estateapp.css"
# web_include_js = "/assets/estateapp/js/estateapp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "estateapp/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"Property" : "public/js/doctype_plugins/claim.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

website_route_rules = routes

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "estateapp.install.before_install"
# after_install = "estateapp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "estateapp.uninstall.before_uninstall"
# after_uninstall = "estateapp.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "estateapp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
	"Property": {
	"on_update":"estateapp.estateapp.doctype.property.event.on_update",
	"after_insert":"estateapp.estateapp.doctype.property.event.after_insert"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"estateapp.tasks.all"
# 	],
# 	"daily": [
# 		"estateapp.tasks.daily"
# 	],
# 	"hourly": [
# 		"estateapp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"estateapp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"estateapp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "estateapp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "estateapp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "estateapp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"estateapp.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
