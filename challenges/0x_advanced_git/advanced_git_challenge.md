# Class 2 - Active Learning Challenge

In this challenge, you will:

* Modify your local Git settings to use your preferred text editor
* Add collaborators to a Git repository
* Practice dealing with merge conflicts

## Step 1: Updating your local Git settings

## Step 2: Adding collaborators
In order to work with someone else on a GitHub repository, you must grant them write access to the code.

(Note: If you are working on a *public* repository, others will already have access.)

This can be done on GitHub as long as you know the other person's username.

1. Go to your project's settings
<img src="images/01-settings.png" width="500">

2. Select `manage access`
<img src="images/02-manage-access.png" width="500">

3. You may need to confirm your login to GitHub - this is the password you initially used to login.
<img src="images/03-confirm-login.png" width="500">

4. Select `invite collaborator`
<img src="images/04-invite-collab.png" width="500">

5. Find the person you want to collaborate with via their username, and actually send the invite!
<img src="images/05-actual-invite.png" width="500">

Great! Now your collaborator should have full push/pull access to your repository.

in order for your collaborator to start working in your repository, they will need to accept the collaborator invitation. Usually, github will send them an email with a link to follow. If not, they should be able to see the invitation in their [notifications](https://github.com/notifications).

## Step 3: Creating a merge conflict
You can see another example of creating a merge conflict [here.](http://swcarpentry.github.io/git-novice/09-conflict/index.html)

1. Within your new shared repository, we will need to modify a file to use for our merge conflict example.

From terminal, let's create a new file:

```
touch merge-test.txt
```

Test yourself: what would happen if you did a `git status` right now?

In order for these changes to be tracked by Git, you will first need to add the file to what Git is watching. We will do this with `git add merge-test.txt`

What is the next step in making this commit?

2. Now, let's make a change to the file that we just created. You can do this by opening the file in your favorite text editor, adding some text, and saving the file.

Once again, we will need to have Git track the changes we have made in our repository.

```
git add -p
```

The `-p` allows us to add changes to the file in a piecemeal fashion. This option is very helpful when we start making lots of changes to a file.

Sometimes, we will want to break up our changes in separate commit messages and this `-p` option makes this easy to do. It also forces us to think about the changes we are committing by reviewing each change in the file as we add it to our commit.

After we have added all of the elements we want into the commit, we need to write our commit message:

```
git commit -m "A short, but clear message so that our future selves know what we did in this commit"
```

3. If we were actually working on our code, we might choose to make several commits before pushing our changes. (Remember the squirrel with their cheeks full of commit "nuts" we talked about before?) However, to move this example along, we are going to push our changes to the remote.

```
git push
```

4. Alright, now let's be bad collaborators and cause a conflict!
