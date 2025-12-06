# Run install of rpms -- too much magic for PyInfra ...
# Utilizes yum localinstall to avoid error -- thanks gemeni!

yum localinstall https://dev.mysql.com/get/mysql84-community-release-$(uname -r | sed 's/^.*\(el[0-9]\+\).*$/\1/')-2.noarch.rpm
