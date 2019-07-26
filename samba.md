# system-config-samba
  build samba server in ubuntu

## install samba
    sudo apt-get install system-config-samba
    sudo touch /etc/libuser.conf
    
## samba configuration
    
  sudo system-config-samba
    
  perference -> samba users -> add user
    
    unix username : pre-created linux user account
    window username : same as unix username
    samba password : create password
    confirm samba password : password
  
  add ->  create samba share
    
    Directory : /
    share name : same as unix username
    check writable, visible box.
    
  sudo service smbd restart
  
    
        
