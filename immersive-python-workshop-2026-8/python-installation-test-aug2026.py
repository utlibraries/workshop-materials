# Step 1 / Question 1: define your name
user = input("Please enter your name (e.g., 'Adam Smith'): ").strip()  # <-------- User enters their name at the terminal prompt

############################################################

## Validate name
alnum_count = sum(1 for c in user if c.isalnum())
if alnum_count < 2:
    print("\n❌❌❌ Error: Please enter a valid name (at least two letters, e.g., 'Adam Smith') and re-run the script.❌❌❌\n")
    exit(1)
else:
    print(f"\n✅ Thanks, {user}! Beginning the analysis...\n")

# Step 2 / Question 2: loading pre-packaged library
try:
    import sys
    python_version = sys.version.split()[0]
    base_package = "Python is working on my computer."
    print(f"✅ {base_package} I am running Python version {python_version}.\n")
except ImportError:
    python_version = "No Python detected.\n"
    base_package = "Python is not working on my computer."
    print(f"❌ {base_package} Please reach out to Anna McGilvray at annamcgilvray@austin.utexas.edu or come prepared to stick around at the end of Day 1 and/or 2 for assistance.\n")

# Step 3 / Question 3: loading non-pre-packaged library
## requests needs to be installed and called to write to the Google Form
try:
    import requests
    requests_message = "requests module successfully called."
    print(f"✅ {requests_message}\n")
except ImportError:
    requests_message = "Python is working but does not seem to be able to find the requests module."
    print(requests_message)
    print(f"❌ {requests_message} Please reach out to Anna McGilvray at annamcgilvray@austin.utexas.edu or come prepared to stick around at the end of Day 1 and/or 2 for assistance.\n")
    sys.exit(1)

# Step 4 / Question 4: writing OS information
## platforms is part of base Python, so it should always work if previous steps worked
try:
    import platform
    os_info = platform.platform()
    print(f"✅ Successfully identified OS info: {os_info}.\n")
except ImportError:
    os_info = "OS info not successfully retrieved.\n"
    print(f"❌ {os_info} Please reach out to Anna McGilvray at annamcgilvray@austin.utexas.edu or come prepared to stick around at the end of Day 1 and/or 2 for assistance.\n")

# Step 5 / Question 5: testing whether pandas can be imported
## if you want to test another package, use one that you know is not installed on your computer (I tested with 'idigbio')
try:
    import pandas as pd
    pandas_status = "pandas module successfully called."
    print(f"✅ {pandas_status}\n")
except ImportError:
    pandas_status = "Python is working but does not seem to be able to find the pandas module."
    print(f"❌ {pandas_status} Please reach out to Anna McGilvray at annamcgilvray@austin.utexas.edu or come prepared to stick around at the end of Day 1 and/or 2 for assistance.\n")

# Step 6 / Question 6: getting timestamp
try:
    from datetime import datetime
    timestamp = datetime.now().isoformat()
    print(f"✅ datetime module successfully loaded. The time is {timestamp}.\n")
except ImportError:
    timestamp = "Could not import datetime module.\n"
    print(f"❌ {timestamp} Please reach out to Anna McGilvray at annamcgilvray@austin.utexas.edu or come prepared to stick around at the end of Day 1 and/or 2 for assistance.\n")

#Step 7: check if virtual environment active or if running in global environment
if sys.prefix == sys.base_prefix:
    venv_status = "virtual environment NOT active!"
    print(f"❌ {venv_status}\n")
else:
    venv_status = "virtual environment active!"
    print(f"✅ {venv_status}\n")

# Step 8: full check
all_checks_passed = (
    base_package == "Python is working on my computer." and
    requests_message == "requests module successfully called." and
    not os_info.startswith("OS info not successfully retrieved") and
    pandas_status == "pandas module successfully called." and
    venv_status == "virtual environment active!" and
    not str(timestamp).startswith("Could not import")
)

if all_checks_passed:
    final_status = "Your Python setup is ready to go!"
    print(f"🎉🎉🎉 {final_status} 🎉🎉🎉\n")
else:
    final_status = "One or more checks was unsuccessful. Please review the messages above and reach out to Anna McGilvray at annamcgilvray@austin.utexas.edu for help or come prepared to stick around at the end of Day 1 and/or 2 for assistance."
    print(f"⚠️⚠️⚠️ {final_status} ⚠️⚠️⚠️\n")

# Step 9: writing to Google Form
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdOwbGqQp_P-UHJV6zHWv5NzagaE2i1-HahHZxt1Sy7EyPeqw/formResponse'
## identifying the entry IDs can be done either by inspecting the HTML source in preview mode or by submitting a manual response and checking the Network tab in developer tools (look for 'formResponse' under File and then 'Request' in the right panel)
form_data = {
    "entry.1816174390": user,
    "entry.1430887170": python_version,
    "entry.752018830": os_info,
    "entry.434521018": base_package,
    "entry.1597103528": requests_message,
    "entry.1336782561": pandas_status,
    "entry.543245770": venv_status,
    "entry.2106462429": final_status,
    "entry.754423696": timestamp
}
response = requests.post(form_url, data=form_data)
if response.status_code == 200:
    print("✅ Form submission successful.\n")
else:
    print("❌ Form submission failed.\n", response.status_code)