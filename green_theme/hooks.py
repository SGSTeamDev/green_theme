app_name = "green_theme"
app_title = "Green Theme"
app_publisher = "Special Man Solution"
app_description = "Custom styling for ERPNext v16"
app_email = "engineering@specialmansolution.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "green_theme",
# 		"logo": "/assets/green_theme/logo.png",
# 		"title": "Green Theme",
# 		"route": "/green_theme",
# 		"has_permission": "green_theme.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/green_theme/css/green_theme.css"
# app_include_js = "/assets/green_theme/js/green_theme.js"

app_include_css = [
    "/assets/green_theme/css/green_theme.css",
    "/assets/green_theme/css/sidebar-green.css"  # New sidebar styles
]

app_include_js = [
    "/assets/green_theme/js/botpress_init.js",
    "/assets/green_theme/js/workspace_logo.js"
]

# Web (portal) CSS - applies to customer/supplier portal
web_include_css = [
    "/assets/green_theme/css/green_theme.css",
    "/assets/green_theme/css/login_style.css"
]

# Specify required Frappe version
required_apps = ["frappe"]

# Version information
__version__ = "0.0.1"

# include js, css files in header of web template
# web_include_css = "/assets/green_theme/css/green_theme.css"
# web_include_js = "/assets/green_theme/js/green_theme.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "green_theme/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "green_theme/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "green_theme.utils.jinja_methods",
# 	"filters": "green_theme.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "green_theme.install.before_install"
# after_install = "green_theme.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "green_theme.uninstall.before_uninstall"
# after_uninstall = "green_theme.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "green_theme.utils.before_app_install"
# after_app_install = "green_theme.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "green_theme.utils.before_app_uninstall"
# after_app_uninstall = "green_theme.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "green_theme.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"green_theme.tasks.all"
# 	],
# 	"daily": [
# 		"green_theme.tasks.daily"
# 	],
# 	"hourly": [
# 		"green_theme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"green_theme.tasks.weekly"
# 	],
# 	"monthly": [
# 		"green_theme.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "green_theme.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "green_theme.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "green_theme.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "green_theme.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["green_theme.utils.before_request"]
# after_request = ["green_theme.utils.after_request"]

# Job Events
# ----------
# before_job = ["green_theme.utils.before_job"]
# after_job = ["green_theme.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"green_theme.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

