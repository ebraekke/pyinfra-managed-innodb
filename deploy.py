
# deploy.py
from pyinfra.api.deploy import deploy
from pyinfra.api import DeployError
from pyinfra import host
from pyinfra.operations import dnf, yum, server, files
from pyinfra.facts import server as server_facts

MYSQL_VERSION = host.data.mysql_version

from pyinfra.operations import server

"""
One liner, note back-quote around el8, cannot cut and paste into terminal and run.
"""
server.shell(
    name="Disable mysql dnf module on el8",
    commands=[
        "if [ $(uname -r | sed 's/^.*\(el[0-9]\+\).*$/\1/') == \"el8\" ]; then  dnf -y module disable mysql; fi"
    ],
    _sudo=True
)

server.shell(
    name="Import MySQL key",
    commands=[
        "rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2023",
    ],
    _sudo=True
)

# Define the local path to your script and the remote destination
script_local_path = "scripts/linux/rpm_install.sh"
script_remote_path = "/tmp/rpm_install.sh"

# 1. Upload the script to the target host
files.put(
    name="Upload script to target host",
    src=script_local_path,
    dest=script_remote_path,
    mode="644",  # don't need to be executable
)

# 2. Execute the uploaded script on the target host
server.shell(
    name="Execute script on target host",
    commands=[
        f"sh {script_remote_path}",  # Or python, sh, etc., depending on your script
    ],
    _sudo=True
)
"""

yum.rpm(
    name="Install MySQL Community repo",
    src="https://dev.mysql.com/get/mysql84-community-release-el8-2.noarch.rpm",
#    src="https://dev.mysql.com/get/mysql84-community-release-$(uname -r | sed 's/^.*\(el[0-9]\+\).*$/\1/')-1.noarch.rpm",
    present=True, 
    _sudo=True
)


# For RHEL/CentOS systems using 'yum' (typically RHEL 7 and older)
server.shell(
    name="Clean Yum metadata cache to force refresh",
    commands=["yum clean metadata", "yum makecache"],
    _Sudo=True
)


yum.packages(
    name="Ensure mysql and mysqlsh are present",
    packages=["mysql-shell=8.4.7", "mysql-community-server=8.4.7"],
    present=True,
    _sudo=True,
)

"""
