# Working with background processes in bash

[More details](https://www.baeldung.com/linux/detach-process-from-terminal)

A simple clock program that shows the time is used to test the background processes

```
echo > clock.sh << EOF
	while sleep 5
	do
		echo $(date)
	done
EOF
```
### Run a program in the background

Use nohup to make the programm ignore the signals used to close the terminal
Redirect the output to /dev/null to avoid the creation of a nohup.out file
Use & to run the prompt in the background
```
nohup bash clock.sh > /dev/null 2>&1 &
```
The PID is returned by the command above

It can also be found out by running
```
ps -f -u <NAMEOFTHEUSER>
```
where `<NAMEOFTHEUSER>`has to be replaced by the users name
or
```
ps -aux
```
Interesting to note:
[Linux processes can be seen by any user](https://unix.stackexchange.com/questions/244353/why-can-i-list-other-users-processes-without-root-permission)

The process can than be stopped by
```
kill <PID>
```
Where ```<PID>``` has to be replaced by the PID



