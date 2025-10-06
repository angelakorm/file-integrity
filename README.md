## Investigating File Integrity in Microsoft OneDrive and Dropbox

### Prerequisites
- Microsoft account
- Microsoft Graph API access
- Python 3.6+
- Dropbox account

### Packages
- .env: `pip install python-dotenv`
- Microsoft Authentication Libraries (MSAL): `pip install msal`
- requests: `pip install requests`
- memory_profiler: `pip install memory-profiler`
- Dropbox: `pip install dropbox`

### Hypothesis
Files uploaded to OneDrive and then downloaded will remain bit-for-bit identical, meaning their SHA-256 hashes should match.

### Result 
The hypothesis was confirmed. Uploaded text and image files of different sizes had matching SHA-256 hashes after download, vefirfying that the Microsoft Graph API preserves file integrity.

### Challenges
- App registration and performance configurations issues
- External and organization access limitations
- Large file uploads
- Performance differences

### Future Experiments
- Large file testing (>250 MB)
- Testing alternate verification and authentication methods
- Different Graph API operations testing
- Graph API beta testing
- Comparing cloud services

### Environment variables
Example .env:

```dotenv
# CLOUD SERVICE
PROVIDER="Microsoft"

# VERIFYING ALGORITHM
VERIFIER="SHA256"

# PATHS
UPLOAD_FOLDER="Folder"
DOWNLOAD_FOLDER_PATH="./files/downloads"
LOCAL_FILE_PATH="./files/uploads/test1.txt"

# MICROSOFT ONEDRIVE
CLIENT_ID=your-client-id
AUTHORITY="https://login.microsoftonline.com/consumers"
GRAPH_API="https://graph.microsoft.com"
VERSION="v1.0"
RESOURCE="me/drive"
SCOPES="Files.ReadWrite.All"

# DROPBOX
DROPBOX_ACCESS_TOKEN="your-token"
```
