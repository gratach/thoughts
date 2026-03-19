# Create linux user


To create a new linux user type:

```
adduser <name_of_the_user>
```

Enter all user information + password
## No password login

If you want to create a user where it is not possible to log in with any password type:
```
adduser --disabled-password <name_of_the_user>
```
Login is still possible starting from the root user with:
```
su <name_of_the_user> -
```
## Create sudo user

You can add a existing user to the sudo group with:
```
usermod -aG sudo <name_of_the_user>
```
