#!/usr/bin/env pwsh

# Source the secrets from .secrets.ps1
$secrets = Invoke-Expression -Command ./.secrets.ps1 | ConvertFrom-Json

# Variables from secrets
$RESTOREDB = $secrets.RESTOREDB
$USER = $secrets.USER
$PASSWORD = $secrets.PASSWORD
$DB = $secrets.DB
$QUERY = $secrets.QUERY

# Step 1: Deploy the SQL Server Container
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=$PASSWORD" -p 1433:1433 --name sql_server_container -d mcr.microsoft.com/mssql/server:2022-latest

# Sleep for a few moments to ensure the SQL Server is fully initialized
Start-Sleep -Seconds 5

# Step 2: Copy the Backup File to the Container
docker cp .\ContosoRetailDW.bak sql_server_container:/var/opt/mssql/data/ContosoRetailDW.bak

# Sleep for a few moments to ensure the file has been copied over completely
Start-Sleep -Seconds 10

# Step 3: Restore the ContosoRetailDW Database
docker exec -it sql_server_container /opt/mssql-tools/bin/sqlcmd -S localhost -U $USER -P $PASSWORD -Q $RESTOREDB

# Sleep for a few moments to ensure the database restoration process is complete
Start-Sleep -Seconds 10

# Step 4: Use the ContosoRetailDW Database and Query FactSales Table
docker exec -it sql_server_container /opt/mssql-tools/bin/sqlcmd -S localhost -U $USER -P $PASSWORD -d $DB -Q $QUERY
