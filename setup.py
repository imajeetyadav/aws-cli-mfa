from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.9"
DESCRIPTION = "AWS CLI MFA - Easily Manage Session Token"
LONG_DESCRIPTION = "Use MFA to increase the security of your AWS environment. Signing in with MFA requires an authentication code from an MFA device."

# Setting up
setup(
    name="cli-aws-mfa",
    version=VERSION,
    author="imajeetyadav (Ajeet Yadav)",
    author_email="<hello@codingprotocols.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=["MFA"],
    keywords=["aws", "mfa", "virtual"],
    py_modules=["cli"],
    entry_points={
        "console_scripts": [
            "cli-aws-mfa = cli:mfa",
        ]
    },
    install_requires=["click", "boto3"],
)
