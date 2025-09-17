## Investigating File Integrity in Microsoft OneDrive Using the Graph API

### Prerequisites
- An Azure account with an active subscription.
- Python 3.6+.

### Packages
- .env: `pip install python-dotenv`
- Microsoft Authentication Libraries (MSAL): `pip install msal`
- requests: `pip install requests`
- memory_profiler: `pip install memory-profiler`

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
