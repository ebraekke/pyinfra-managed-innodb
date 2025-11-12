# pyinfra-managed-innodb
Manage InnoDB Cluster configurations using PyInfra


```
pyinfra --debug @all inventory.py exec -- "hostname"
```

Regenerate this before run
```
Host db-node-10
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
