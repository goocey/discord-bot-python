#!/bin/sh

yum update -y
yum install -y python36 python36-pip memcached memcached-tool
yum install -y postgresql postgresql-devel postgresql-libs python-devel
systemctl start memcached
systemctl enable memcached
/usr/local/bin/pip3 install --upgrade pip
cd /vagrant/mw/
/usr/local/bin/pip3 install -r require.txt