# 🛡️ S3 Lambda File Scanner

This AWS Lambda project scans files uploaded to an S3 bucket and tags them with a scan result (`ScanStatus=Clean`).

## 💻 Tech Stack
- AWS Lambda (Python)
- Amazon S3
- IAM Roles
- CloudWatch Logs

## ⚙️ How It Works
1. Upload file to S3 bucket
2. Lambda function triggers automatically
3. File is "scanned" (simulated)
4. Scan result is added as a tag to the file in S3

## 📁 Files
- `lambda_function.py`: Main Lambda handler

## 📸 Sample Log
