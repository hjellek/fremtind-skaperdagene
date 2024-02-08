For å ha skrivetilgang til git er det enkleste å bruke HTTPS når man sjekker ut repo, og lagre passordet i environment på maskinen.

Lag filen `$HOME/git_password.sh` med innholdet:
```shell
#!/bin/sh
exec echo "$GIT_PASSWORD"
```

Lag en [Personal Access Token](https://github.com/settings/tokens) på GitHub (og sett kort levetid) og legg den i `$HOME/.bash_profile`:

`echo "export GIT_PASSWORD=<personal access token>" >> $HOME/.bash_profile`

`echo "export GIT_ASKPASS=$HOME/git_password.sh" >> $HOME/.bash_profile`

`source $HOME/.bash_profile`

Da skal du kunne bruke git clone og andre git-kommandoer som trenger passord uten å skrive det inn hver gang. 
