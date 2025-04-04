from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from io import BytesIO

SCOPES = ['https://www.googleapis.com/auth/drive']

def create_service():
    flow = InstalledAppFlow.from_client_secrets_file('C:/Users/lucky/Documents/key.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return build('drive', 'v3', credentials=creds)


def download_file(service, file_id, file_name):
    request = service.files().get_media(fileId=file_id)
    fh = BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print("Download Progress: {0}".format(int(status.progress() * 100)))
    
    fh.seek(0)
    with open(file_name, 'wb') as f:
        f.write(fh.read())
        f.close()



service = create_service()

file_id = 'FILE_ID'  # Replace with the actual file ID

file_name = 'FILE_NAME'  # Replace with the desired file name

download_file(service, file_id, file_name)