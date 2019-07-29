# setting command

## Set ROS alias command

    alias cw='cd ~/catkin_ws'
    alias cs='cd ~/catkin_ws/src'
    alias cm='cd ~/catkin_ws && catkin_make'

## apt-get

    sudo apt-get -y install vim git cmake tmux

## tmux setting

    cd ~
    vim tmux.conf
    setw -g mouse on

## vim setting
    
    cd ~/.vimrc
    
    // add the following
    set autoindent
    set cindent
    set nu
    set ts=4
    set shiftwidth=4
    set showmatch
    set ruler
    
    if has("syntax")
        syntax on
    endif
