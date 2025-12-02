
# deploy.py
from pyinfra.api.deploy import deploy
from pyinfra.api import DeployError
from pyinfra import host
from pyinfra.operations import dnf, yum, server, files

MYSQL_VERSION = host.data.mysql_version

dnf.packages(
    name="Remove builtin MySQL",
    packages=["mysql", "mysql-shell"],
    present=False,
    _sudo=True,
)

yum.key(
    name="Import MySQL key",
    src="https://repo.mysql.com/RPM-GPG-KEY-mysql-2023",
    _sudo=True
)

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

#yum.packages(
#    name="Install mysql",
#    packages=["mysql-shell=8.4.7", "mysql-server=8.4.7"],
#    update=True,
#    _sudo=True,
#)

