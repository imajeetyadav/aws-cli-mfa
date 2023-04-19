import boto3
import os


class MFA:
    def __init__(self, profile_name, mfa_arn=None):
        self.profile_name = profile_name
        self.mfa_arn = mfa_arn
        self.mfa_token = None
        self.session = boto3.Session()

    def set_mfa_token(self, token):
        self.mfa_token = token

    def set_mfa_arn(self, arn):
        self.mfa_arn = arn

    def authenticate(self):
        if not self.mfa_arn:
            raise ValueError("MFA ARN is not set")

        client = self.session.client("sts")
        response = client.get_session_token(
            DurationSeconds=3600, SerialNumber=self.mfa_arn, TokenCode=self.mfa_token
        )

        return response["Credentials"]

    def set_credential(self, credentials):
        aws_access_key_id = credentials["AccessKeyId"]
        aws_secret_access_key = credentials["SecretAccessKey"]
        aws_session_token = credentials["SessionToken"]

        aws_config_dir = os.path.join(os.path.expanduser("~"), ".aws")
        if not os.path.exists(aws_config_dir):
            os.makedirs(aws_config_dir)
            credentials_path = os.path.join(aws_config_dir, "credentials")
            with open(credentials_path, "a") as f:
                f.write(f"\n[{self.profile_name}]\n")
                f.write(f"aws_access_key_id = {aws_access_key_id}\n")
                f.write(f"aws_secret_access_key = {aws_secret_access_key}\n")
                f.write(f"aws_session_token = {aws_session_token}\n")
                f.close()

            mfa_arn_file = os.path.join(aws_config_dir, ".mfa_arn")
            with open(mfa_arn_file, "a") as f:
                f.write(self.mfa_arn)
                f.close()

    def check_mfa_arn_file(self):
        if os.path.exists(os.path.join(os.path.expanduser("~"), ".aws", ".mfa_arn")):
            return True
        else:
            return False

    def get_arn_from_file(self):
        aws_config_dir = os.path.join(os.path.expanduser("~"), ".aws")
        mfa_arn_file = os.path.join(aws_config_dir, ".mfa_arn")
        self.mfa_arn = open(mfa_arn_file, "r").read().strip()
        return self.mfa_arn

    def validate_session(self):
        session = boto3.Session(profile_name=self.profile_name)
        if session.get_credentials().access_key is None:
            print("Error: AWS access key is not set")
        elif session.get_credentials().secret_key is None:
            print("Error: AWS secret key is not set")
        elif session.get_credentials().token is None:
            print("Error: AWS session token is not set")
        else:
            print("AWS session is valid")
            return True
        return False
