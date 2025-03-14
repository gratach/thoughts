# Debian i3 PC setup

A set of instructions how to set up a [debian](https://www.debian.org/) PC with [i3](https://i3wm.org/)

Download the image from the Debian website

Put it on a USB stick

...

... TODO

...

### Configure the .bashrc file

Add the following content to the .bashrc file to define some commands and configure some settings

```
cat >> ~/.bashrc << 'EOF'
```
```
#custom

export HISTSIZE=-1
export HISTFILESIZE=-1
export PROMPT_COMMAND=" history -a; history -c; history -r;"
export HISTTIMEFORMAT="%Y.%m.%d-%H:%M:%S "


# o stands for "open"
# Opens a file with the standard application
function o(){
        if [ -d $1 ]; then
                bash -c "nohup thunar $1 < /dev/null 1> /dev/null 2> /dev/null &"
        elif [ -f $1 ]; then
                # xdg-open buggt bei ausführbaren python files
                bash -c "nohup gio open $1 < /dev/null 1> /dev/null 2> /dev/null &"
        else
                echo "'$1' ist no valid file path"
        fi
}

# o-r stands for "open replace"
# opens a file with the standard application and close the current terminal
function o-r(){
        o $@
        kill -s 9 $$
}

# s stands for "start"
# Starts a command as a independent process
function s(){
        bash -c "nohup $@ < /dev/null 1> /dev/null 2> /dev/null &"
}

# s-r stands for "start replace"
# Starts a command and closes the current terminal
function s-r(){
        s $@
        kill -s 9 $$
}

# b stands for "bash"
# Creates a new bash window
# The current working directory of the new terminal will be the first argument if given or else the working directory of the old terminal
function b(){
        if [ $# -eq 1 ]; then
                davordir=$(pwd)
                cd $1
                bash -c "nohup i3-sensible-terminal < /dev/null 1> /dev/null 2> /dev/null &"
                cd $davordir
        else
                bash -c "nohup i3-sensible-terminal < /dev/null 1> /dev/null 2> /dev/null &"
        fi
}

# s-b stands for "start bash"
# Starts a command running in a new bash terminal
function s-b(){
        echo $@ > ~/.AUTOSTART_TEMP
        bash -c "nohup i3-sensible-terminal < /dev/null 1> /dev/null 2> /dev/null &"
}

# h-l stands for "history less"
# It opens the history in a reading editor
alias h-l="history|less"

# 3i and 3p stands for "ipython3" and "python3"
alias 3i="ipython3"
alias 3p="python3"

# g-g stands for "git graph"
# It opens a graph view of the git history
alias g-g="git log --all --graph --oneline --decorate"

# g-c stands for "git commit"
# It adds all changes and commits them 
alias g-c="git add .; git commit -am "

# g-s stands for "git status"
# It adds all files and shows the git status
alias g-s="git add .; git status"

# ls-s stands for list size
# It lists the content of the current directory ordered by size
alias ls-s="ls -A|xargs -I {} du -sh {}| sort -rh"


# Add more custom configuration here


# If any script should be started automatically start it
# This code is neaded by the s-b command
if [ -f ~/.AUTOSTART_TEMP ]; then
        what_i_do_next="$(cat ~/.AUTOSTART_TEMP)"
        rm ~/.AUTOSTART_TEMP
        bash -c "$what_i_do_next"
fi
```
```
EOF
```