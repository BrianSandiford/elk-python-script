# CSV Report Downloader

This is a Python script that generates and downloads a CSV report from a remote server.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`

## Installation

1. Clone the repository or download the script file.
2. Install the required Python packages by running the following command:
   ```shell
   pip install requests
   ```
3. Create a virtual environment: `python3 -m venv myenv`
4. Activate the virtual environment:
   - For Windows: `myenv\Scripts\activate`
   - For macOS/Linux: `source myenv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`

Usage

1. Open the script file in a text editor.
2. Modify the following variables according to your requirements:

- `base_url`: The base URL of the remote server.
- `headers`: Headers to be included in the requests.
- `params` : Parameters to be sent along with the POST request.

3. Save the modifications.
4. Run the script using the following command:

`python script_name.py`

Please note that you should replace `script_name.py` with the actual name of your Python script file. Also, make sure to include the necessary license information by providing a LICENSE file or specifying the appropriate license in the README.
