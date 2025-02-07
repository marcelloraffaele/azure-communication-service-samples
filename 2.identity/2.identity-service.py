from flask import Flask, request, jsonify
from azure.communication.identity import CommunicationIdentityClient, CommunicationTokenScope,CommunicationUserIdentifier
from azure.identity import DefaultAzureCredential
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

connection_str = os.getenv("ACS_CONNECTION_STRING")
endpoint = os.getenv("ACS_ENDPOINT")

identity_client_managed_identity = CommunicationIdentityClient(endpoint, DefaultAzureCredential())
identity_client = CommunicationIdentityClient.from_connection_string(connection_str)


app = Flask(__name__)

@app.route('/user-and-token', methods=['POST'])
def create_user_and_token():
    try:
        # Create a user and token
        user = identity_client.create_user()
        token_response = identity_client.get_token(user, scopes=[CommunicationTokenScope.CHAT, CommunicationTokenScope.VOIP])
        return jsonify({
            'user_id': user.properties['id'],
            'token': token_response.token,
            'expires_on': token_response.expires_on
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/user-and-token', methods=['DELETE'])
def delete_user_and_token():
    try:
        user_id = request.json.get('user_id')
        if not user_id:
            return jsonify({'error': 'user_id is required'}), 400
        user= CommunicationUserIdentifier(user_id)
        # Revoke token and delete user        
        identity_client.revoke_tokens(user)
        identity_client.delete_user(user)

        return jsonify({'message': 'User and token deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)