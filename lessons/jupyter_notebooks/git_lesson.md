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

## 1. What are Git and Github?

### Git

Git is a tool for implementing something called "version control", which tracks changes you've made to your files, and stores the history of your changes. 

Have you ever had a situation like this?

<img src="https://thedataarealright.files.wordpress.com/2018/11/screen-shot-2012-09-12-at-08-38-56.png" width="500">

This kind of system, where we have to save a file with a new name everytime we update it (so we don't lose previous work) can be really confusing! Git, by using version control, can make this much simpler.

With Git, you can make your changes and save to just one filename, while still having your change history tracked so you could return to an older version of you'd like. You'll get to try this out soon.

### Github <img src="https://miro.medium.com/max/2560/1*JLYlSLSK8-AZo8gt9UdYqA.jpeg" width="200">

Github is a little bit different from Git. While Git is the version control system that helps track your files, Github is a platform for hosting file folders (or 'repositories' or 'repos') on the cloud. Github provides some really useful tools to collaborate with others and share your work publicly.

By the end of this lesson, you'll also be setting up your own Github repository!

## 2. Setting up Git on your computer

Git is most often used from the command line (just like how we've been running python scripts), although there are other ways to use it. For the most part, all of the ways we'll use Git today will be from the command line. When you first set up Git on your computer, you'll need to do a few extra things to configure it. These are setup steps you have to to **once only**

#### Git Config

Using the command line, you'll first need to tell Git what your user name is:

```console
$ git config --global user.name "Paul Bloom"
```

Then, you'll want to set up an email address to associate with your Git activity. Here, you should make sure to use the **same email address attached to your Github account**:

`git config --global user.email "paul.bloom@columbia.edu"`

Now you should be all set up to start using Git on your computer!

## 3. Using Git for version control

### Initializing a folder with git version control

First, you can set up a new folder on your computer. A git-controlled folder starts out in basically the same way as any other folder. Let's make a directory called 'example_git' in your class folder, then navigate into it

`mkdir example_git`

`cd example_git`

When you run `ls` in this folder, you'll notice that there are no files.

Now, we can initialize this folder as a git repository by running the following:

`git init`

## 4. Syncing your work to the cloud with Github

# Challenge

For this challenge in this class, make an awesome python function!


```python

```

## Topic 2


Here is a great sentence with some text for the lesson, as well as inline code like `print('hello world)` or `git status`


```python
# here is some python code for topic 1
def my_cool_function(user_input):
    return(2*user_input)
```
