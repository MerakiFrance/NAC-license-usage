# Meraki NAC License Usage Exporter

A Python script to retrieve NAC (Network Access Control) license usage data from Cisco Meraki organizations via API, display the results, and optionally export them to an Excel file.

---

## Description

This script connects to the Meraki Dashboard API using your API key, lists all organizations associated with the key, and allows you to select a target organization.  

You can specify a date range and retrieve NAC license usage data, which includes daily peak concurrent sessions. The results are displayed in the terminal and can optionally be exported to an Excel file.

The script also handles existing Excel files gracefully:

- If the default file `nac_license_usage.xlsx` does not exist, it will be created.
- If it already exists, the user is prompted to **overwrite** or **rename** the file.

---

## Features

- Retrieve organizations linked to your Meraki API key  
- Fetch NAC license usage data for a selected organization and date range  
- Display results in a human-readable JSON format  
- Export the data to Excel (`date` / `peakConcurrentSessions`)  
- Handle existing Excel files with overwrite or rename options  

---

## Prerequisites

- **Python 3.11+** (tested with Python 3.11)  
- **Meraki API key** (can be generated in the Meraki Dashboard)  
- Python packages:

```bash
pip install pandas openpyxl requests
