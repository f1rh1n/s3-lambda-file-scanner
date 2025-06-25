import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(f"Scanning file: {key} in bucket: {bucket}")

    # Simulate a scan result
    scan_result = "Clean"

    # Add tag to file
    s3.put_object_tagging(
        Bucket=bucket,
        Key=key,
        Tagging={
            'TagSet': [
                {
                    'Key': 'ScanStatus',
                    'Value': scan_result
                }
            ]
        }
    )

    print(f"Tagging completed: ScanStatus = {scan_result}")

    return {
        'statusCode': 200,
        'body': json.dumps(f"Scan complete. Status: {scan_result}")
    }
