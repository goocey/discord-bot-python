#!/bin/bash
yum install -y ansible tmux
echo "vagrant:vagrant" | chpasswd
sed -i -e 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
systemctl restart sshd