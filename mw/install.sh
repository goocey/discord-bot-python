#!/bin/sh

yum update -y
yum install python36 python36-pip
/usr/local/bin/pip3 install --upgrade pip
/usr/local/bin/pip3 install discord