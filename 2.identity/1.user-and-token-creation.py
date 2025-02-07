# https://learn.microsoft.com/en-us/python/api/overview/azure/communication-identity-readme?view=azure-python
# You can find your endpoint and access token from your resource in the Azure Portal
import os
from dotenv import load_dotenv
from azure.communication.identity import CommunicationIdentityClient, CommunicationTokenScope
from azure.identity import DefaultAzureCredential
import sys

# Load the environment variables from the .env file
load_dotenv()

connection_str = os.getenv("ACS_CONNECTION_STRING")
endpoint = os.getenv("ACS_ENDPOINT")

# To use Azure Active Directory Authentication (DefaultAzureCredential) make sure to have
# AZURE_TENANT_ID, AZURE_CLIENT_ID and AZURE_CLIENT_SECRET as env variables.
identity_client_managed_identity = CommunicationIdentityClient(endpoint, DefaultAzureCredential())

#You can also authenticate using your connection string
identity_client = CommunicationIdentityClient.from_connection_string(connection_str)

try:
    print("Enter the number of users you want to create: ")
    user_input = input()
    if not user_input.isdigit():
        raise ValueError("The input must be a number.")
    n = int(user_input)
    if n > 5:
        raise ValueError("The number must be at least 5.")


    for i in range(n):
        print("Creating User and Token: " + str(i+1))

        user=identity_client.create_user()
        print("User created with id: " + user.properties['id'])

        tokenresponse = identity_client.get_token(user, scopes=[CommunicationTokenScope.CHAT, CommunicationTokenScope.VOIP])
        print("Token issued with value: " + tokenresponse.token)

        print()


except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)