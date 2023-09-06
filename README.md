# ContosoRetailDW-DockerSetup
This repository provides a streamlined approach to set up the ContosoRetailDW SQL Server in a Docker environment and connect it with Power BI. It also provides scripts and steps for testing the SQL connection and running queries.

## Prerequisites
- Docker
- PowerShell
- Python (if you wish to run the connection test script)

## Setup
1. Clone this repository
```bash
git clone https://github.com/your_username/ContosoRetailDW-DockerSetup.git
cd ContosoRetailDW-DockerSetup
```
Replace your_username with your actual GitHub username.

2. Download and extract the ContosoRetailDW backup
- Download the contosobak.exe file from the source https://www.microsoft.com/en-US/download/details.aspx?id=18279.
- Run the downloaded .exe to extract the ContosoRetailDW.bak file.
- Move or copy the ContosoRetailDW.bak to the root folder of this cloned repository.

3. Running the Scripts
To set up the SQL Server in Docker and restore the database:

```powershell
.\deployContoso.ps1
```
To test the SQL connection using Python:

```bash
python test_connection.py
```

## Usage
With the database set up, you can connect interact with the SQL Server instance running inside the Docker container. Specify your desired credentials in the .secrets.ps1 file.

## Troubleshooting
If you encounter any issues, please check the logs and error messages for details. Most common issues can be resolved by ensuring the ContosoRetailDW.bak file is correctly placed in the root directory or ensuring that Docker is running properly.

## Contributing
Contributions are welcome! Please fork this repository and open a pull request to add more functionalities or fix any issues.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

