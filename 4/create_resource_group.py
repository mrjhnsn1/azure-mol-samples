# This script sample is part of "Learn Azure in a Month of Lunches" (Manning
# Publications) by Iain Foulds.
#
# This sample script covers the exercises from chapter 4 of the book. For more
# information and context to these commands, read a sample of the book and
# purchase at https://www.manning.com/books/learn-azure-in-a-month-of-lunches
#
# This script sample is released under the MIT license. For more information,
# see https://github.com/fouldsy/azure-mol-samples/blob/master/LICENSE

import string,random,time,azurerm,json,subprocess,os

from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

tenant_id = os.environ['TENANT_ID']
app_id = os.environ['APP_ID']
app_secret = os.environ['APP_SECRET']
subscription_id = os.environ['SUBSCRIPTION_ID']

# Define variables to handle Azure authentication
#get_token_cli = subprocess.Popen(['az account get-access-token | jq  -r .accessToken'], stdout=subprocess.PIPE, shell=True)
auth_token = azurerm.get_access_token(tenant_id, app_id, app_secret)

print('auth token ' + auth_token)

#auth_token = str(get_token_cli.communicate()[0]).rstrip()
#subscription_id = azurerm.get_subscription_from_cli()

# Define variables with random resource group and storage account names
resourcegroup_name = 'azuremol'+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
storageaccount_name = 'azuremol'+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
location = 'eastus'

print('resourcegroup_name ' + resourcegroup_name)
print('storageaccount_name ' + storageaccount_name)


###
# Create the a resource group for our demo
# We need a resource group and a storage account. A random name is generated, as each storage account name must be globally unique.
###
response = azurerm.create_resource_group(auth_token, subscription_id, resourcegroup_name, location)
if response.status_code == 200 or response.status_code == 201:
    print('Resource group: ' + resourcegroup_name + ' created successfully.')
else:
    print('Error creating resource group ' + str(response.status_code) )

response = azurerm.delete_resource_group(auth_token, subscription_id, resourcegroup_name)
if response.status_code == 202:
    print('Resource group: ' + resourcegroup_name + ' deleted successfully.')
else:
    print('Error deleting resource group.')
