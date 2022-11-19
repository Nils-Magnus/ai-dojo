#!/bin/bash

# script for setting up a bunch of users

# bash is very sensitive regarding whitespace. there should be NONE around "="
# and there must be whitespace after "(" and before ")"
USERS=( "user1" "user2" "user3" )

for USER in "${USERS[@]}"; do
  echo "Setting up $USER"

  USERHOME="/home/$USER"
  PASSWORD="$USER"

  # create user without password
  sudo adduser --quiet --disabled-password --shell /bin/bash --home "$USERHOME" --gecos "$USER" "$USER"

  # set password
  echo "$USER:$PASSWORD" | sudo chpasswd

  # clone the necessary files
  cd "$USERHOME" || exit
  sudo touch test.txt # todo replace with git clone

  # since files were created by root, need to change permissions so that user owns them
  sudo chown "$USER" -R "$USERHOME"
  sudo chgrp "$USER" -R "$USERHOME"
done