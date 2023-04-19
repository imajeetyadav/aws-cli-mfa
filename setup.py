from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.1"
DESCRIPTION = "AWS CLI MFA"
LONG_DESCRIPTION = "Use MFA to increase the security of your AWS environment. Signing in with MFA requires an authentication code from an MFA device. Each user can have a maximum of 8 MFA devices assigned"

# Setting up
setup(
    name="aws-mfa",
    version=VERSION,
    author="imajeetyadav (Ajeet Yadav)",
    author_email="<hello@codingprotocols.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=["aws-mfa"],
    keywords=["aws", "mfa", "virtual"],
    entry_points={
        "console_scripts": [
            "aws-mfa = aws-mfa:cli",
        ]
    },
    install_requires=["click", "boto3"],
)
