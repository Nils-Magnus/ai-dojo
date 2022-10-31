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
sudo pip3 install jupyterlab
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

### 7. Starting jupyterhub

```
sudo jupyterhub --ip 0.0.0.0
```

### 8. Setup SSL

#### Get domain ready

Point domain A record to IP (https://www.namecheap.com/support/knowledgebase/article.aspx/9837/46/how-to-connect-a-domain-to-a-server-or-hosting/)

#### Open firewall

Need port 80 (for let's encrypt) and 443 (where we will run jupyterhub later)


#### install lets-encrypt package  and generate certificat

Following https://certbot.eff.org/instructions?ws=other&os=ubuntufocal

```
sudo apt-get install snapd
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot

# stop jupyterhub before running this
sudo certbot certonly --standalone
```

#### start jupyterhub with ssl

```
# obviously replace krasch.dev with your own domain-name
sudo jupyterhub --ip 0.0.0.0 --port 443 --ssl-key /etc/letsencrypt/live/krasch.dev/privkey.pem --ssl-cert /etc/letsencrypt/live/krasch.dev/fullchain.pem
```

You may need to change permissions, here is a quick hack that gives 
the relevant files to the user that starts the jupyterlab (in my case user 'dev')

```
sudo chown dev:dev -R /etc/letsencrypt
```
