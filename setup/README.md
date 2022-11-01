# Setup with Ansible


1. install Ansible on your local machine
2. create your VM and add it under the hostname `ai-training` to your `~/.ssh/config` file
3. run `ansible-playbook setup/minimal-playbook.yaml -i setup/inventory.yaml`   