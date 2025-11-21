# group_data/all.py

import os

# This applies to all groups/hosts

## import os 
##
## my_dir = os.getcwd()
## print(f"Current dir is {my_dir}")

# Working dir shoud be top level 
# ssh_config_file = "./config/use_this_config"

ssh_config_file = os.environ.get("SSH_CONFIG_FILE")

# Common MySQL version and passwords — overrideable per group/host
mysql_version = "8.4"
mysql_root_password = "changeme123"
cluster_admin_user = "clusterAdmin"
cluster_admin_password = "ClusterPass123!"
cluster_name = "myCluster"
