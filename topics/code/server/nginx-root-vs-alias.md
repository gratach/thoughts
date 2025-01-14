# Nginx root vs alias

[stackoverflow discussion](https://stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias)

Configuration A:

```
location /suburl/ {
	root /var/www/folder/;
}
```

Configuration B:

```
location /suburl/ {
	alias /var/www/folder/;
}
```

In both configurations the url `mywebsite.de/suburl/mypath/index.html` will be translated to different paths on the server:

Configuration A:

`/var/www/folder/suburl/mypath/index.html` 

Configuration B:

`/var/www/suburl/mypath/index.html` 