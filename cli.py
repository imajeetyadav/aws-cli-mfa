import click
from MFA.mfa import MFA


@click.group()
def mfa():
    click.secho("Setup the ARN and Profile")
    pass


@mfa.command()
def init():
    profile = input("Give any name for your profile: ")
    arn = input(
        "Please input the ARN of your MFA device (e.g. arn: aws: iam: : 123456789012: mfa/user): "
    )
    click.secho("Using profile {} and MFA ARN {}".format(
        profile, arn), fg="green")
    mfa = MFA(profile_name=profile, mfa_arn=arn)
    token = input("Please input your MFA token code: ")
    mfa.set_mfa_token(token)
    try:
        mfa.set_credential(mfa.authenticate())
    except:
        click.secho(
            'Authenication Failed ( Invalid Token/ARN or Access Denied )', fg='red')
    validate(mfa.validate_session)


@mfa.command()
def refresh():
    mfa = MFA()
    if mfa.check_mfa_arn_file:
        try:
            arn = mfa.get_arn_from_file()
            profile = mfa.get_profile_from_file()
        except:
            click.secho('Please use "cli-aws-mfa init" command', fg="yellow")
            exit(1)
        mfa.set_mfa_arn(arn)
        click.secho("Using Profile {} and MFA ARN {}".format(
            profile, arn), fg="green")
        token = input("Please input your MFA token code: ")
        mfa.set_mfa_token(token)
        mfa.set_credential(mfa.authenticate())
        validate(mfa.validate_session)

    else:
        click.secho("MFA ARN is required", fg="red")


def validate(validate_session):
    if validate_session:
        click.secho("Successfully Authenticated", fg="green")
    else:
        click.secho("Authentication Failed", fg="red")


if __name__ == "__main__":
    mfa()
