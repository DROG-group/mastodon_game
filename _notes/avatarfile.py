"""
Mastodon Avatar API
===================

This API provides endpoints to manage Mastodon avatars through a file service API instead of an Mastodon (throttled) API. 

Systemd Service Setup:
----------------------

1. Create a new systemd service unit file:

    sudo nano /etc/systemd/system/mastodon_avatar_api.service

2. Add the following content:

    [Unit]
    Description=Mastodon Avatar API Service
    After=network.target

    [Service]
    User=your_username
    WorkingDirectory=/path/to/your/flask/app
    ExecStart=/path/to/your/python /path/to/your/flask/app/app.py
    Restart=always

    [Install]
    WantedBy=multi-user.target

3. Replace:
    - 'your_username' with the actual username.
    - '/path/to/your/flask/app' with the directory where this Flask app resides.
    - '/path/to/your/python' with the path to the Python executable.

4. Reload the systemd manager configuration:

    sudo systemctl daemon-reload

5. Enable the service to start on boot:

    sudo systemctl enable mastodon_avatar_api.service

6. Start the service:

    sudo systemctl start mastodon_avatar_api.service

Monitoring:
-----------

1. Check the service status:

    sudo systemctl status mastodon_avatar_api.service

2. View logs:

    sudo journalctl -u mastodon_avatar_api.service

Notes:
------
- Ensure the Flask app has the necessary permissions for Mastodon's avatar directory.
- Use production mode for Flask (`debug=False`) and set the desired IP/port.
- For large-scale deployments, consider Gunicorn and Nginx.

"""
from flask import Flask, request, send_from_directory, jsonify
from flask_restful import Api, Resource
import os

app = Flask(__name__)
api = Api(app)

# Define the base directory for avatars
AVATAR_BASE_DIR = os.path.expanduser('~/mastodon/live/public/system/accounts/avatars/')

class FileUpload(Resource):
    def post(self, account_id, filename):
        if 'file' not in request.files:
            return {'message': 'No file part'}, 400
        file = request.files['file']
        if file.filename == '':
            return {'message': 'No selected file'}, 400
        if file:
            target_directory = os.path.join(AVATAR_BASE_DIR, construct_avatar_path(account_id))
            os.makedirs(target_directory, exist_ok=True)  # Ensure the directory exists
            file_path = os.path.join(target_directory, filename)
            file.save(file_path)
            return {'message': 'File uploaded successfully'}, 200

class FileDownload(Resource):
    def get(self, account_id, filename):
        return send_from_directory(os.path.join(AVATAR_BASE_DIR, construct_avatar_path(account_id)), filename)

api.add_resource(FileUpload, '/upload/<string:account_id>/<string:filename>')
api.add_resource(FileDownload, '/download/<string:account_id>/<string:filename>')

def construct_avatar_path(account_id):
    """Construct the relative path for the avatar based on the account_id."""
    id_str = str(account_id)
    path_components = []
    
    # Split account_id into chunks of 3 digits and add to path components
    for i in range(0, len(id_str), 3):
        path_components.append(id_str[i:i+3])
    
    return os.path.join(*path_components)

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='127.0.0.1')  # You can choose another port if required
