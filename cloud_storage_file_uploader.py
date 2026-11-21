
import boto3
from pathlib import Path

bucket = "your-bucket-name"
folder = Path("reports")
client = boto3.client("s3")
for file_path in folder.iterdir():
    if file_path.is_file():
        client.upload_file(str(file_path), bucket, file_path.name)
        print("Uploaded:", file_path.name)
