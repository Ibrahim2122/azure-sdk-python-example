from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters, Sku, Kind

# Your Azure subscription ID and resource group and storage account details
subscription_id = "b3a62fbb-a23e-48e3-9ca5-2d6f10e799fa"
resource_group_name = "my-sdk-rg"
location = "eastus"
storage_account_name = "sdkstorageaccount2122io"

# Create the Azure Resource Management client
resource_client = ResourceManagementClient(DefaultAzureCredential(), subscription_id)

# Create the resource group
resource_client.resource_groups.create_or_update(resource_group_name, {"location": location})

# Create the Azure Storage Management client
storage_client = StorageManagementClient(DefaultAzureCredential(), subscription_id)

# Define storage account parameters
storage_account_params = StorageAccountCreateParameters(
    sku=Sku(name="Standard_LRS"),
    kind=Kind.storage,
    location=location
)

# Create the storage account
# storage_client.storage_accounts.create_or_update(
#     resource_group_name,
#     storage_account_name,
#     storage_account_params
# )

storage_client.storage_accounts.begin_create(resource_group_name, storage_account_name, storage_account_params).result()

print("Storage account deployed successfully!")