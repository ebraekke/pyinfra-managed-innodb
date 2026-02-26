# pyinfra-managed-innodb
Create (and manage) InnoDB Cluster configurations using PyInfra

No SSH config
```powershell
pyinfra --data ssh_key=.config/db.key --data ssh_config_file=.config/ssh_config 10.0.1.62 deploy.py
```

```powershell
$env:SSH_CONFIG_FILE="./.config/ssh_config"

pyinfra --data ssh_key=.config/db.key 10.0.1.62 exec -- hostname
```

```
pyinfra  inventory.py deploy.py    
```

```
pyinfra  inventory.py exec -- "hostname"  
>>
--> Loading config...
--> Loading inventory...
--> Connecting to hosts...
    No host key for 10.0.1.202 found in known_hosts, accepting & adding to host keys file
    Added host key for 10.0.1.202 to known_hosts
    No host key for 10.0.1.123 found in known_hosts, accepting & adding to host keys file
    Added host key for 10.0.1.123 to known_hosts
    No host key for 10.0.1.238 found in known_hosts, accepting & adding to host keys file
    Added host key for 10.0.1.238 to known_hosts
    [db1] Connected
    [db3] Connected
    [db2] Connected

--> Preparing exec operation...
    [db1] Ready: shell
    [db3] Ready: shell
    [db2] Ready: shell

--> Beginning operation run...
--> Starting operation: server.shell (hostname)
[db1] db1
    [db1] Success
[db3] db3
    [db3] Success
[db2] db2
    [db2] Success

--> Results:
    Operation                 Hosts   Success   Error   No Change   
    server.shell (hostname)   3       3         -       -           
    Grand total               3       3         -       -           

--> Disconnecting from hosts...
```

TODO: Reference to `oci-posh-utils` 

Regenerate this before run 
```
Host db1
  HostName 10.0.1.54
  User opc
  IdentityFile /tmp/db-10610
  UserKnownHostsFile /dev/null
  ProxyCommand ssh -i /tmp/bastionkey-2025_11_06_17_32_31-9061 -W %h:%p -p 22 ocid1.bastionsession.oc1.eu-frankfurt-1.amaaaaaa3gkdkiaa7oiz4i564dystyxjbkzgteq5iwalkzzoiyzztsb2i6ea@host.bastion.eu-frankfurt-1.oci.oraclecloud.com
```

These settings should be set on server to allow for longer runnin gsession: 

https://docs.oracle.com/en-us/iaas/Content/Security/Reference/bastion_security.htm#hardening

>Configure the SSH server on target compute instances for maximum security.
>
>We recommend that you update the default values for these settings in /etc/ssh/sshd_config.
>
>Setting	/ Description
>MaxAuthTries	Specifies the maximum number of authentication attempts permitted per connection. After the number of failures reaches half this value, failures are logged.
>
> ClientAliveCountMax	Sets the number of client alive messages which can be sent without receiving any messages back from the client. If this threshold is reached while client alive messages are being sent, the server disconnects the client, terminating the session.
>
>ClientAliveInterval	Sets a timeout interval in seconds after which if no data has been received from the client, the server will send a message through the encrypted channel to request a response from the client.
