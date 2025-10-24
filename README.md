Meraki NAC License Usage Exporter
=================================

A Python script to retrieve NAC (Network Access Control) license usage data from Cisco Meraki organizations via API, display the results, and optionally export them to an Excel file.

📝 Description
--------------

This script connects to the Meraki Dashboard API using your API key, lists all organizations associated with the key, and allows you to select a target organization.You can specify a date range and retrieve NAC license usage data, which includes daily peak concurrent sessions. The results are displayed in the terminal and can optionally be exported to an Excel file.

The script also handles existing Excel files gracefully:

*   If the default file nac\_license\_usage.xlsx does not exist, it will be created.
    
*   If it already exists, the user is prompted to **overwrite** or **rename** the file.
    

⚙️ Features
-----------

*   Retrieve organizations linked to your Meraki API key
    
*   Fetch NAC license usage data for a selected organization and date range
    
*   Display results in a human-readable JSON format
    
*   Export the data to Excel (date / peakConcurrentSessions)
    
*   Handle existing Excel files with overwrite or rename options
    

🛠️ Prerequisites
-----------------

*   **Python 3.11+** (tested with Python 3.11)
    
*   **Meraki API key** (can be generated in the Meraki Dashboard)
    
*   Python packages:
    
```
pip install pandas openpyxl requests
```

🚀 Usage
--------

**1.  Clone this repository or download the script:**
    
```
git clone https://github.com/MerakiFrance/NAC-license-usage
cd NAC-license-usage
```

**2.  Run the script:**
    
```
python3 get_nac_license_usage_with_export_en.py
```

**3.  Follow the prompts:**
    

*   Enter your **Meraki API key**
    
*   Select the organization from the numbered list
    
*   Enter the **start and end dates** (format: YYYY-MM-DD)
    
*   View the results in the terminal
    
*   Choose whether to **export the data to Excel**
    

**4.  Export behavior**:
    

*   If nac\_license\_usage.xlsx does not exist → created automatically
    
*   If it exists → you are prompted to overwrite or rename
    

🗂️ Output
----------

The Excel file will contain two columns:

The Excel file will contain two columns:

| date       | peakConcurrentSessions |
|------------|----------------------|
| 2025-10-01 | 8                    |
| 2025-10-02 | 1                    |
| 2025-10-03 | 15                   |
| 2025-10-04 | 32                   |
| 2025-10-05 | 6                    |
| 2025-10-06 | 13                   |
| 2025-10-07 | 0                    |
| 2025-10-08 | 4                    |
| 2025-10-09 | 43                   |
| 2025-10-10 | 51                   |
| 2025-10-11 | 12                   |
| ...        | ...                  |

⚠️ Notes
--------

*   The script expects the Meraki API response to contain the usageData field, which is standard for NAC license usage API endpoints.
    
*   The script has been tested on macOS with Python 3.11. Using older Python versions may cause compatibility issues.
