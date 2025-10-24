import requests
import json
import pandas as pd
import os

def get_meraki_organizations(api_key):
    """Retrieve the list of organizations associated with the Meraki API key"""
    url = "https://api.meraki.com/api/v1/organizations"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_nac_license_usage(api_key, org_id, start_date, end_date):
    """Retrieve NAC license usage data for a given organization"""
    url = f"https://api.meraki.com/api/v1/organizations/{org_id}/nac/license/usage"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }
    params = {
        "startDate": start_date,
        "endDate": end_date
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def export_to_excel(data):
    """Export the result to an Excel file (date / peakConcurrentSessions) with overwrite check"""
    # Extract usageData list if present
    usage_list = data.get("usageData") if isinstance(data, dict) else data

    if not isinstance(usage_list, list):
        print("⚠️ The returned data is not in the expected list format.")
        return

    # Extract relevant fields
    rows = []
    for item in usage_list:
        date = item.get("date")
        peak = item.get("peakConcurrentSessions")
        if date is not None and peak is not None:
            rows.append({"date": date, "peakConcurrentSessions": peak})

    if not rows:
        print("⚠️ No valid records found for export.")
        return

    df = pd.DataFrame(rows)
    default_filename = "nac_license_usage.xlsx"

    # Check if file exists
    if os.path.exists(default_filename):
        print(f"⚠️ The file '{default_filename}' already exists.")
        choice = input("Do you want to overwrite it (o) or rename (r)? [o/r]: ").strip().lower()
        if choice == "r":
            new_name = input("Enter the new filename (with .xlsx extension): ").strip()
            if not new_name.lower().endswith(".xlsx"):
                new_name += ".xlsx"
            filename = new_name
        else:
            filename = default_filename
            print(f"✅ The file '{filename}' will be overwritten.")
    else:
        filename = default_filename

    df.to_excel(filename, index=False)
    print(f"✅ Data exported to the file: {filename}")

def main():
    print("=== Meraki NAC License Usage ===\n")

    # 1️⃣ Ask for the API key
    api_key = input("👉 Enter your Meraki API key: ").strip()

    # 2️⃣ Retrieve organizations
    try:
        orgs = get_meraki_organizations(api_key)
    except requests.exceptions.RequestException as e:
        print(f"❌ Error retrieving organizations: {e}")
        return

    if not orgs:
        print("⚠️ No organizations found for this API key.")
        return

    # 3️⃣ Display the list and select the organization
    print("\nAvailable organizations:")
    for i, org in enumerate(orgs, start=1):
        print(f"{i}. {org['name']} (ID: {org['id']})")

    while True:
        try:
            choice = int(input("\nSelect the number of the target organization: "))
            if 1 <= choice <= len(orgs):
                org_id = orgs[choice - 1]["id"]
                org_name = orgs[choice - 1]["name"]
                break
            else:
                print("❌ Invalid number, try again.")
        except ValueError:
            print("❌ Please enter a valid number.")

    # 4️⃣ Enter dates
    print("\nExpected format: YYYY-MM-DD (e.g., 2025-10-01)")
    start_date = input("📅 Start date: ").strip()
    end_date = input("📅 End date: ").strip()

    # 5️⃣ Call the NAC license usage API
    try:
        result = get_nac_license_usage(api_key, org_id, start_date, end_date)
        print(f"\n=== Results for {org_name} ({org_id}) ===")
        print(json.dumps(result, indent=2))
    except requests.exceptions.RequestException as e:
        print(f"❌ Error calling NAC License Usage API: {e}")
        return

    # 6️⃣ Optionally export to Excel
    choice = input("\nDo you want to export the result to Excel? (y/n): ").strip().lower()
    if choice == "y":
        export_to_excel(result)
    else:
        print("⏭️ Export skipped.")

if __name__ == "__main__":
    main()
