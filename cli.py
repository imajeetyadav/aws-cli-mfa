import click
from MFA.mfa import MFA


@click.command()
@click.option(
    "--profile", help="Give any name for you local profile. default: mfa-user"
)
@click.option(
    "--arn",
    help="Please input the ARN of your MFA device (e.g. arn:aws:iam::123456789012:mfa/user)",
)
@click.option(
    "--token",
    help="Please input your MFA token code:",
)
def cli(profile, arn, token):
    if profile and arn:
        click.secho("Using profile {} and MFA ARN {}".format(profile, arn), fg="green")
        mfa = MFA(profile_name=profile, mfa_arn=arn)
        token = input("Please input your MFA token code: ")
        mfa.set_mfa_token(token)
        mfa.set_credential(mfa.authenticate())
        validate(mfa.validate_session)

    elif profile and token:
        mfa = MFA(profile_name=profile)
        if mfa.check_mfa_arn_file:
            arn = mfa.get_arn_from_file()
            click.secho(
                "Using profile {} and MFA ARN {}".format(profile, arn), fg="green"
            )
            mfa.set_mfa_token(token)
            mfa.set_credential(mfa.authenticate())
            validate(mfa.validate_session)

    elif arn:
        click.secho(
            'Using Default profile name - "mfa-user" and  MFA ARN {}'.format(arn),
            fg="green",
        )
        mfa = MFA(profile_name="mfa-user", mfa_arn=arn)
        token = input("Please input your MFA token code: ")
        mfa.set_mfa_token(token)
        mfa.set_credential(mfa.authenticate())
        validate(mfa.validate_session)

    elif profile:
        mfa = MFA(profile_name=profile)
        if mfa.check_mfa_arn_file:
            arn = mfa.get_arn_from_file()
            mfa.set_mfa_arn(arn)
            click.secho(
                "Using Profile {} and MFA ARN {}".format(profile, arn), fg="green"
            )
            token = input("Please input your MFA token code: ")
            mfa.set_mfa_token(token)
            mfa.set_credential(mfa.authenticate())
            validate(mfa.validate_session)
        else:
            click.secho("MFA ARN is required", fg="red")
    elif token:
        mfa = MFA(profile_name=profile)
        if mfa.check_mfa_arn_file:
            arn = mfa.get_arn_from_file()
            mfa.set_mfa_arn(arn)
            click.secho(
                "Using Profile {} and MFA ARN {}".format(profile, arn), fg="green"
            )
            token = input("Please input your MFA token code: ")
            mfa.set_mfa_token(token)
            mfa.set_credential(mfa.authenticate())
            validate(mfa.validate_session)

        else:
            click.secho("MFA ARN is required", fg="red")

    else:
        click.secho("MFA ARN is required", fg="red")


def validate(validate_session):
    if validate_session:
        click.secho("Successfully Authenticated", fg="green")
    else:
        click.secho("Authenticated Failed", fg="red")


if __name__ == "__main__":
    cli()
