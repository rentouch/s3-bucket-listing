#!/usr/bin/env python3
import os

EXPECTED_VARIABLES = (
    "S3BL_IGNORE_PATH", "BUCKET_NAME", "BUCKET_URL", "S3B_ROOT_DIR", "S3B_SORT",
    "EXCLUDE_FILE", "AUTO_TITLE", "S3_REGION", "PAGE_TITLE"
)

with open("index.html", "r") as f:
    template_html = f.read()

# Grab values from environment
env_variables = {}
for env_variable in EXPECTED_VARIABLES:
    env_variables[env_variable] = os.getenv(env_variable, None)

# Set page title
page_title = env_variables["PAGE_TITLE"]
page_title = page_title if page_title is not None else "Directory listing"
new_html = template_html.replace("PAGE_TITLE", page_title)
env_variables.pop("PAGE_TITLE")

# Set js variables
js_variables = ""
for var_name, var_value in env_variables.items():
    if var_value is not None:
        js_variables += f"var {var_name} = {var_value};\n"
new_html = new_html.replace("CONFIGURATION_JS", js_variables)

with open("index.html", "w") as f:
    f.write(new_html)

os.system('nginx -g "daemon off;"')
