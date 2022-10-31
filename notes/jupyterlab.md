### 0. Start any ubuntu-based instance

might want to pick one with a faster harddisk than the default
one, I ended up waiting ages for my apt-get upgrade

### 1. Basic setup
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip

python3 --version
pip3 --version
```

### 2. Installing node (needed by jupyterhub)

Following https://github.com/nodesource/distributions/blob/master/README.md

```
# disgusting...
curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash - &&\
sudo apt-get install -y nodejs
```
### 3. Installing jupyterhub

Following https://github.com/jupyterhub/jupyterhub

```
sudo npm install -g configurable-http-proxy
sudo pip3 install jupyterhub
sudo pip3 install notebook
```

### 4. Open port

In GCP (or whatever cloud you are using) open port 8000

### 5. Create local users

sudo adduser user1 (and follow the prompts)

### 6. Install requirements

```
sudo pip3 install pandas
etc
```

### 6. Starting jupyterhub

```
sudo jupyterhub --ip 0.0.0.0
```

