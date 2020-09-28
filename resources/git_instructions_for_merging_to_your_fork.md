# How to pull the master branch to your own fork

You might remember that you 'forked' the `jtc_class_code` repository from the one we created a while ago. Anytime you want to get updates from this 'master' repo (from `Justice-Through-Code/jtc_class_code`) to your own (`your_username/jtc_class_code`), you'll have to get these changes using these steps. Here are the instructions

### 1. Add the repo as 'upstream'

The master repo that we created is called the 'upstream' one here

```console
$ git remote add upstream https://github.com/Justice-Through-Code/jtc_class_code.git
```

### 2. 'Fetch' the upstream content
```console
$ git fetch upstream
```

### 3. Pull from the upstream master

```console
$ git pull upstream master
```

### 4. Push to your own forked version

You know this one already! Now that we have the updated version on our own local copy, we push to our online version of the forked repo (i.e. `your_username/jtc_class_code`)

```console
$ git push origin master
```

This should pull the newest updates to your fork!
