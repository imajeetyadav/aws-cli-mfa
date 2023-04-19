# AWS CLI MFA

Developed by Ajeet Yadav

## Example of How To Use

```
# Setup ARN and profile name
cli-aws-mfa init

# Refresh Session Token
cli-aws-mfa refresh 

```

## Policy Used for CLI MFA

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "MustBeSignedInWithMFA",
            "Effect": "Deny",
            "NotAction": [
                "iam:CreateVirtualMFADevice",
                "iam:DeleteVirtualMFADevice",
                "iam:ListVirtualMFADevices",
                "iam:EnableMFADevice",
                "iam:ResyncMFADevice",
                "iam:ListAccountAliases",
                "iam:ListUsers",
                "iam:ListSSHPublicKeys",
                "iam:ListAccessKeys",
                "iam:ListServiceSpecificCredentials",
                "iam:ListMFADevices",
                "iam:GetAccountSummary",
                "sts:GetSessionToken"
            ],
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "aws:MultiFactorAuthPresent": "false"
                }
            }
        }
    ]
}
```