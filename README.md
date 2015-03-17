Ansible Playbook for InfluxDB & Grafana 

This playbook aims to install InfluxDB and Grafana on a Ubuntu 14.10 droplet on DigitalOcean.

The whole process took me 4 minutes from droplet creation to finished installation.

Quick quide
1. install python-devel python-pip with apt-get or yum 
2. sudo pip install ansible --upgrade
3. git clone https://github.com/anton-mishel/influx-grafana-ansible.git
4. cd influx-grafana-ansible 
5. cp hosts.sample hosts
6. Edit:  hosts
7. cp vars/external_vars.yml.sample vars/external_vars.yml
8. Edit:  /vars/external_vars.yml
9. ansible-playbook -i hosts site.yml

Detailed instructions

Grafana will be served via nginx, InfluxDB will be accessible throught it's default webserver.

Install Ansible

Make sure that you have Ansible installed. I wouldn't even bother to create a virtualenv for this because it is quite unlikely that you will ever need several different versions of Ansible on your machine. The latest should always do.

sudo pip install ansible --upgrade

Clone this repository & change variables

Now clone this repository and cd into the cloned folder.

Copy the hosts.example file and enter the IP address of your influx and grafana server 

cp hosts.example hosts

vim hosts

Copy the external_vars.yml.example file and change all usernames and passwords to your liking.

#cp vars/external_vars.yml.sample vars/external_vars.yml
#vim vars/external_vars.yml
#Run the playbook

Execute the playbook:

ansible-playbook -i hosts site.yml

Create awesome dashboards

You can now visit http://<influxdb-ip>:8083 and see your InfluxDB admin. You will see that we have two databases, one for saving grafana dashboards and another for your project's metrics.

You can also visit http://<grafana-ip> to see your grafana dashboard.

Update Grafana

When a new version of Grafana is released, just change the GRAFANA_SOURCE_FILENAME in external_vars.yml and run:

ansible-playbook -i hosts update-grafana.yml# influx-grafana-ansible
