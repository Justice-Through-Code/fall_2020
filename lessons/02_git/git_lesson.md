# Before class

  * Make sure you have git installed on your computer before class. 
      * This can be checked by running `git --version` from the command line. 
      * If you see something like "git version 1.7.7.3" (or any other version of git) pop up, you're all set. If you see something like "command not found", you'll need to install
      * If you need to need to install it -- use the [Mac installer](https://sourceforge.net/projects/git-osx-installer/) or [Windows](https://git-scm.com/download/win)
  * If you don't have a Github account, [sign up for a free account on Github](https://github.com/join). We'll be using these accounts in class.
    

# Outline of class agenda

During this class, you will:

1. Learn what Git & Github are, and why they're useful
2. Set up Git on your computer
3. Use Git for version control
4. Sync your work to the cloud with Github
 

# Class 

Note: this lesson borrows heavily from the Software Carpentry Git Curriculum, all of which can be found free online [here](https://swcarpentry.github.io/git-novice/). 

## 1. What are Git and Github?

### Git

Git is a tool for implementing something called "version control", which tracks changes you've made to your files, and stores the history of your changes. 

Have you ever had a situation like this?

<img src="https://thedataarealright.files.wordpress.com/2018/11/screen-shot-2012-09-12-at-08-38-56.png" width="500">

This kind of system, where we have to save a file with a new name everytime we update it (so we don't lose previous work) can be really confusing! Git, by using version control, can make this much simpler.

With Git, you can make your changes and save to just one filename, while still having your change history tracked so you could return to an older version of you'd like. You'll get to try this out soon.

### Github 

<img src="https://miro.medium.com/max/2560/1*JLYlSLSK8-AZo8gt9UdYqA.jpeg" width="200">

Github is a little bit different from Git. While Git is the version control system that helps track your files, Github is a platform for hosting file folders (or 'repositories' or 'repos') on the cloud. Github provides some really useful tools to collaborate with others and share your work publicly. As one example, all the lessons for this course are [stored as a Github repository here](https://github.com/Justice-Through-Code/fall_2020). 

By the end of this lesson, you'll also be setting up your own Github repository!

## 2. Setting up Git on your computer

Git is most often used from the command line (just like how we've been running python scripts), although there are other ways to use it. For the most part, all of the ways we'll use Git today will be from the command line. When you first set up Git on your computer, you'll need to do a few extra things to configure it. These are setup steps you have to do **once only**

#### Git Config

Using the command line, you'll first need to tell Git what your user name is:

```console
$ git config --global user.name "Paul Bloom"
```

Then, you'll want to set up an email address to associate with your Git activity. Here, you should make sure to use the **same email address attached to your Github account**:

```console
$ git config --global user.email "paul.bloom@columbia.edu"
```

Now you should be all set up to start using Git on your computer!

## 3. Using Git for version control

### Initializing a folder with git version control

First, you can set up a new folder on your computer. A git-controlled folder starts out in basically the same way as any other folder. Let's make a directory called 'example_git' in your class folder, then navigate into it


```console
$ mkdir example_git`
$ cd example_git`
```

When you run `ls` in this folder you'll see that there are no files.

Now, we can initialize this folder as a git repository by running the following:

```console
$ git init
```

Now, if you run `ls -a` you'll notice that there is a hidden file called .git in the repository. This is what will track all other files' histories.

### Adding (staging) files

First, we'll make a text file to start tracking using Git version control. 

```console
$ touch file1.txt
```

You can add whatever text you like to this file. Now, if we run the following:

```console
$ git status
```

You'll see something like this:

<img src="images/git_status_1.png" width="500">

This is indicating that while we don't yet have any changes to commit, we do have an untracked file, file1.txt. "Untracked" means git has not yet tracked changes to this file. 

So, let's start tracking file1.txt. This is also called 'staging' your changes. Staging tells Git which files we want to capture a version of in our history.

```console
$ git add file1.txt
```

Now, if you run `git status`, you should see something like:

<img src="images/git_status_2.png" width="500">

This indicates that file1.txt is now being tracked by Git! It is staged. 

### Committing files

Now that you have a tracked file, you can do what is called a 'commit'. This is basically taking a snapshot of *all the staged files at this point in time*, and saving it in the .git file. Crucially, every time we commit, we have to include a commit message (as indicated by the -m flag), which should be a short but useful message describing what changes you've made since the last time.

Here we add the message 'adding file1.txt' 

```console
$ git commit -m 'adding file1.txt' 
```

Great! Now you've made a snapshot of your work at this point in time! Even as we edit file1.txt in the future, we'll be able to use git to return to this version if we need to.

If you run `git status` again now, you'll see a message like 'On branch master nothing to commit, working tree clean'. This might be surprising, but it actually means that **since the last commit**, there are no new changes. 

### Getting the workflow down

<img src="https://miro.medium.com/max/686/1*diRLm1S5hkVoh5qeArND0Q.png" width="500">

For the most part, we run `git add ...` before every `git commit ...`. Why do we need to add before committing?

  * This is helpful when we want to commit changes to some files, but not others. (i.e. we only use `git add` for the specific files we want)
  * Git is not meant for very large files. Being able to stage only some files using `git add ...` means we can leave out large files that might crash Git. 



##### So, now let's practice this a few more times:

**A: Updating file1.txt:**

  * Open up file1.txt and make an edit. Run `git status` -- what do you see?
  * Now, *stage* file1.txt. Which command is used to do this?
  * Run `git status` again to check whether you have staged file1.txt. How can you tell whether it is staged or not?
  * Now, *commit* file1.txt. Remember to include a commit message!


**B: Adding script1.py:**

  * Make a new file in your repository called `script1.py`. Put a line or two with the python code of your choice in it.
  * Now, stage script1.py and commit your changes! Use `git status` wherever you like to see if this worked.

**C: Committing multiple changes::**

  * First, make an change to script1.py. Then, make a new file called script2.py. What happens when you run `git status` now?
  * Let's now stage **all** changes. You can do this by running `git add .`   The dot means 'add all files'. 
  * Try running `git status` again. Which files have been staged? Why?
  * Now, commit your changes, remembering to include a commit message. 


Great! You've now had some practice with the Git workflow. You'll use this same general workflow a LOT throughout the rest of the course when saving version history for your files. 


## 4. Syncing your work to the cloud with Github

So far, you've only been working with version control with files on your computer. Now, we'll learn how to sync them to the cloud using Github!

#### Making a new Github repo

The first step is to make a new repository on Github to sync with the one on your computer. Log into your Github account online, then look for the '+' button near the top right to make a new repo.

<img src="https://swcarpentry.github.io/git-novice/fig/github-create-repo-01.png" width="800">

Choose 'new repository' from the dropdown menu. You should see the below menu pop up next. Use 'example git' for the repository name, add whatever description you like, and set it to private. Don't initialize with a Readme file now -- we'll handle that later. 

<img src="https://swcarpentry.github.io/git-novice/fig/github-create-repo-02.png" width="800">



After confirming, you'll see your new Github repo. It's empty so far. 

#### Syncing your local repository with the online Github repository

What you'll want to do next is follow the instructions to push an existing repository from the command line.

<img src="images/git_push_1.png">

As shown, run these lines from the command line inside the Git repository on your computer, replacing the web address with the address of your Github repository (it should end in '.git') 

```console
$ git remote add origin https://github.com/pab2163/example_git.git
$ git push -u origin master
```

After running the second line, you should see something like this, indicating that you sucessfully 'pushed' your updates to the online (or 'remote') Github repo:

<img src="images/git_push_2.png" width="500">


Then, if you refresh the page for your online Github repo, you should see your files there, something like this:


<img src="images/git_push_3.png">

Great! Your files are now online!

#### Adding a readme file for your Github file repo & pushing more changes to Github

Many Github repositories have 'README' files, which give users a description about what is in the repository, and sometimes a guide for how to use the code. To add a readme file, go back to the command line inside the repository on your computer and make a file called 'README.md'

```console
$ touch README.md
```

Then, you can use the text editor of your choice (for example sublime) to edit your README.md file. This file is in Markdown format, which uses '#' to indicate big title text, and double asterisks surrounding text to make it bold. Try making a title, author, and description of your repository similar to below:

<img src="images/readme_md.png">

When your repository is synced with Github, you can continue to use `git add` and `git commit` in the same way to store changes on your computer. Then, when you want to push those changes to your online Github repository, you can run:

```console
$ git push
```

This will **push** what's on your local computer to the online repo. Try staging the new README.md file, commiting that change, and pushing your changes now. When you refresh your Github repository online, now your README.md will show up in a nice format:

<img src="images/readme_2.png">

Great! Now you've added a README with info about your repository, and learned how to push more changes to Github. In the future, you'll use a similar process for updating other files. 


#### Workflows using Github

Now, in addition to `git add`, and `git commit`, we integrate `git push` into our workflow to sync our online repository with work on our local computer. Check out the diagram below for a good schematic of this:

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--M_fHUEqA--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/128hsgntnsu9bww0y8sz.png" width='600'>

We haven't covered `git pull` and `git checkout` for today, so don't worry about them yet! We will revisit these later in the course when we move to working collaboratively using these tools. 

## Examples of existing Github repositories:

There are TONS of Github repositories on the internet for lots of different kinds of projects for software, research, informatics, education, and more. Here is [one list of interesting repositories](https://www.freecodecamp.org/news/the-10-github-repos-people-mention-the-most-in-freecodecamps-main-chat-room-189750600fa4/). 

Some additional repos that might be interesting:

  * [A repo for coronavirus data from Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)
  * [A repo from the Vera Institute of Justice with incarceration data from 1970-2017](https://github.com/vera-institute/incarceration_trends)
  * [A repo for the Spotipy python API](https://github.com/plamere/spotipy) (a way of accessing Spotify data with python)

# Beyond...

There are many more useful things you can do with Github beyond what we've learned today. You can find more info in the [Software Carpentry Git Lesson](https://swcarpentry.github.io/git-novice/), but later on in the course we'll also come back to a few more Git/Github tools, especially for using Github in a collaborative way.

