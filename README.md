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

## Here's a brief summary of the methods in this class:

- `__init__(self, profile_name="mfa-user", mfa_arn=None)`: Initializes a new `MFA` instance with the specified profile name and MFA ARN (Amazon Resource Name).
- `set_mfa_token(self, token)`: Sets the MFA token for the instance.
- `set_mfa_arn(self, arn)`: Sets the MFA ARN for the instance.
- `authenticate(self)`: Authenticates with AWS using the specified MFA ARN and token, and returns a set of temporary credentials.
- `set_credential(self, credentials)`: Sets the AWS credentials for the specified profile name using the temporary credentials returned by `authenticate()`.
- `check_mfa_arn_file(self)`: Checks if the MFA ARN file exists in the AWS configuration directory.
- `check_mfa_profile_file(self)`: Checks if the profile file exists in the AWS configuration directory.
- `get_arn_from_file(self)`: Reads the MFA ARN from the MFA ARN file in the AWS configuration directory.
- `get_profile_from_file(self)`: Reads the profile name from the profile file in the AWS configuration directory.
- `validate_session(self)`: Validates the session for the specified profile name and prints an error message if any of the AWS access keys are not set.

Here's some documentation for each of the methods in this class:

- `__init__(self, profile_name="mfa-user", mfa_arn=None)`: This is the constructor for the `MFA` class. It initializes a new instance with the specified profile name and MFA ARN. If no profile name is specified, the default profile name is "mfa-user". If no MFA ARN is specified, it is set to `None`.
- `set_mfa_token(self, token)`: This method sets the MFA token for the instance.
- `set_mfa_arn(self, arn)`: This method sets the MFA ARN for the instance.
- `authenticate(self)`: This method authenticates with AWS using the specified MFA ARN and token. It returns a set of temporary credentials that can be used to access AWS resources.
- `set_credential(self, credentials)`: This method sets the AWS credentials for the specified profile name using the temporary credentials returned by `authenticate()`. It writes the credentials to the AWS credentials file in the user's home directory.
- `check_mfa_arn_file(self)`: This method checks if the MFA ARN file exists in the AWS configuration directory. If the file exists, it returns `True`. Otherwise, it returns `False`.
- `check_mfa_profile_file(self)`: This method checks if the profile file exists in the AWS configuration directory. If the file exists, it returns `True`. Otherwise, it returns `False`.
- `get_arn_from_file(self)`: This method reads the MFA ARN from the MFA ARN file in the AWS configuration directory. It returns the MFA ARN as a string.
- `get_profile_from_file(self)`: This method reads the profile name from the profile file in the AWS configuration directory. If the file exists, it returns the profile name as a string. Otherwise, it returns the default profile name ("mfa-user").
- `validate_session(self)`: This method validates the session for the specified profile name. If any of the AWS access keys are not set, it prints an error message. Otherwise, it prints a message