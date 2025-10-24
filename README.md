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
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install pandas openpyxl requests   `

🚀 Usage
--------

1.  Clone this repository or download the script:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`git clone   cd` 

1.  Run the script:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python3 get_nac_license_usage_with_export_en_v2.py   `

1.  Follow the prompts:
    

*   Enter your **Meraki API key**
    
*   Select the organization from the numbered list
    
*   Enter the **start and end dates** (format: YYYY-MM-DD)
    
*   View the results in the terminal
    
*   Choose whether to **export the data to Excel**
    

1.  **Export behavior**:
    

*   If nac\_license\_usage.xlsx does not exist → created automatically
    
*   If it exists → you are prompted to overwrite or rename
    

🗂️ Output
----------

The Excel file will contain two columns:

datepeakConcurrentSessions2025-10-0102025-10-021......

⚠️ Notes
--------

*   The script expects the Meraki API response to contain the usageData field, which is standard for NAC license usage API endpoints.
    
*   The script has been tested on macOS with Python 3.11. Using older Python versions may cause compatibility issues.
