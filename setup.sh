#!/usr/bin/env bash

# Enable powertools repo
sed -i 's/^enabled.*/enabled=1/' /etc/yum.repos.d/*PowerTools.repo

dnf -y install lynx

TRIPLEO_REPOS=$(lynx -dump -hiddenlinks=listonly https://trunk.rdoproject.org/centos8/component/tripleo/current/ | awk '/python3-tripleo-repos.*rpm$/ {print $2}')

dnf install -y ${TRIPLEO_REPOS}

tripleo-repos --stream -b master current-tripleo ceph

dnf install -y zeromq python3 etcd

# development packages
dnf install -y gcc

# Create development workspace
python3 -m venv /opt/director
/opt/director/bin/pip install --upgrade pip setuptools wheel
/opt/director/bin/pip install "$(dirname $(readlink -f ${BASH_SOURCE[0]}))[ui,dev]"

echo -e "\nDirector is setup and installed within [ /opt/director ]"
echo "Activate the venv or run director directly."
echo "Director can be installed as a service using the following command(s):"
echo "director-client-systemd"
echo -e "director-server-systemd\n"
