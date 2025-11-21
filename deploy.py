
# deploy.py
from pyinfra.api.deploy import deploy
from pyinfra.api import DeployError
from pyinfra import host
from pyinfra.operations import server

REQUIRED_ENV_VARIABLES = [
    "ssh_config_file",
]

@deploy("Check required environment variables")
def check_required_environment(state, host):
    missing = []
    for var in REQUIRED_ENV_VARIABLES:
        if not getattr(host.data, var):
            missing.append(var)

    if missing:
        raise DeployError(
            f"Missing required environment variables: {', '.join(missing)}"
        )


# Register the check as an operation (no parentheses!)
check_required_environment

# Example real operation (MySQL install, firewall, etc.)
server.shell(
    name="Just a placeholder operation",
    commands=["echo All environment variables OK!"],
)
