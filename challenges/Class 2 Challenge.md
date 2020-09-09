# Class 2 - Active Learning Challenge

In this challenge, you will: 

* Fork the class GitHub repository
* Customize your own README
* Push your changes to GitHub

## Step 1: Forking the repository

Go to the [GitHub repository containing the class code](https://github.com/Justice-Through-Code/jtc_class_code). In the top left, you will see the owner and name of the repository: `'Justice-Through-Code/jtc_class_code'`. Click the button that says `Fork` in the top right corner. You will be redirected to your forked repository. You can see that you own this copy of the repository by looking at the top left corner, where the owner and name will now show: `'{your_username}/jtc_class_code'`.  

## Step 2: Customizing your own README

README files tell users what the purpose of a repository is, and pretty much every repository you'll see will have a README file. We will now create a README file for the repository you just forked.  

First, create a directory called `jtc_class_code`. Next, open up an empty file in your text editor of choice (Atom, Sublime, etc). Save this file with the name `README.md` in the `jtc_class_code` directory. By saving it with the ending '.md', you have designated the file as a Markdown file. Markdown allows you to easily customize the appearance of your text files with just a few shortcuts. This document is also written in Markdown!

In your README file, write whatever you would like. For now, you don't need to worry about formatting the Markdown in special ways, but you can find tips and tricks for using Markdown [here](https://www.markdownguide.org/cheat-sheet/). Make sure to save any changes you make to this file!

## Step 3: Pushing your changes to the repository

After you have customized your `README.md` file, you are ready to push it to the repository you forked. 

First, open up the terminal. Navigate to the `jtc_class_code` directory where you saved your README. Once you are in the correct directory, you need to set this up as a git repository. 

### *** If you have already connected your GitHub account to your computer, you can skip this step. ***
To connect your GitHub account, run the commands:
```
$ git config --global user.name "your_username"
$ git config --global user.email "your_email@columbia.edu"
```
Next, we need to initialize this directory as a git repository. Run the command:
```
$ git init
```
This directory is now a git repository, but it's not connected to the repository you forked. To connect the local and remote repositories, run the command and replace `{your_username}` with your GitHub username:

```
$ git remote add origin https://github.com/{your_username}/jtc_class_code.git
```

Since the forked repository already has content, you must retrieve that content by pulling it. Run the command:
```
$ git pull origin master
```

Now, you can see the existing content as well as your new README by checking the status of the repository. This command will show you whether each file is untracked, tracked and unstaged, or tracked and staged. Run the command:
```
$  git status
```
You can see that your README is untracked. To track and stage it, run the command:
```
$ git add README.md
```
You can check the status again to see that the file is now tracked and staged. Next, we want to commit the changes to git history. To do so, run the command:
```
$ git commit -m 'Created README`
```

The last step is to push your changes! Run the command:
```
$ git push -u origin master
```
If you go back to GitHub and look at the forked repository, you can now see the updated README in the repository!
