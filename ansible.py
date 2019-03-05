#Ansible Code (exploring options on how to use ansible)

name: "installing additional software"
apt: pkg={ { item } } state=installed
with_items:
dnsutils
git
vim
ntp
at
lvm2

name: "adding bashrc"
copy:src=../file/bash.bashrc dest=/etc/bash.bashrc owner=root group=root mode=0644

name: "removing ray's bashrc"
shell:creats=/home/rm/.bashrc_backup mv /home/rm/.bashrc /home/rm/.bashrc_backup

name:"root's bashrc"
shell:creats=/root/.bashrc_backup mv /home/rm/.bashrc /home/rm/.bashrc_backup
