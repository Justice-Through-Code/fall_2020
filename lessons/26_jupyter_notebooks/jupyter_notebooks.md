# Before class

For this class, you'll want to make sure you have Anaconda installed on your computer beforehand. You'll probably have done this earlier in the course, but if not, here are some [instructions](https://docs.anaconda.com/anaconda/install/)

# Outline of class agenda


During this class you'll: 

1. Learn what jupyter notebooks are and why they're useful
2. Learn how to navigate the jupyter notebook interface
3. Get comfortable with making and working with your own notebooks

# Class 

Note: this lesson design was heavily inspired by https://realpython.com/jupyter-notebook-introduction/

## 1) Jupyter notebooks: what are they, and why use them?

#### What is a jupyter notebook?

So far, we've run python code using **scripts** (i.e. running files ending in '.py' from the command line). Jupyter notebooks are another way to run python code that is a little less like a script and a little more like a literal 'notebook'. The biggest difference with jupyter notebooks compared to python scripts it that they are **interactive** so that you can run single lines or pieces of code and get output right away. 

Here's a summary of what is different about jupyter notebooks from the scripts (i.e. 'pure python') we've worked with so far:

* We run jupyter notebooks interactively from a browser (for example Chrome or Firefox)
* Jupyter notebooks have individual cells that can be run in any order, and give you immediate output right beneath them
* Jupyter notebooks can have cells of formatted text and graphics embedded in them, so you can view them with your code
* Jupyter notebooks can run [over 40 other programming languages](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) too, not just python


#### Why use jupyter notebooks?

In general, jupyter notebooks are great for any coding where you want to *interact* with your code, view outputs, and make quick changes. So, they are particularly good for things like:

* **'rough drafting' your code** -- sketching out and debugging your initial ideas where you can test things out easily and interactively
* **data science** -- when you're working with data, being able to interact with it and quickly view lots of outputs is helpful
* **graphs & figures** -- jupyter notebooks allow graphs and charts to show up inside your notebook file as you're working
* **documents & tutorials** -- the fact that notebooks allow you to integrate graphics and nice Markdown text makes them great for making documents that share combinations of code, text, and graphics with others. In fact, *this lesson* is a jupyter notebook, and most other lessons for this class are as well!

#### What are jupyter notebooks *not* as good for

* **Code that needs to re-used or imported** -- it is much less straightforward to import a jupyter notebook compared to a .py file
* **object-oriented programming (class definitions)** -- it usually works better to define classes in .py scripts, since they are more easily imported
* **code that is run as part of a 'pipeline' or 'code base'** -- it is easier to integrate python scripts with other languages and into a larger code base than jupyter notebooks

## 2) How to navigate jupyter notebooks

### Starting the Jupyter Notebook Server

One **important** thing to do when starting a jupyter notebook is to think about where you want your notebook file to be on your computer. First, figure out what folder you want to put it in (for example `Users/Paul/Documents/Teaching/jtc_class_code/lessons/`), then navigate to that folder using the command line (i.e. with `cd`).

Now, you can start up the jupyter notebook server by running the following from the command line:

```console
$ jupyter notebook
```

It might take a second, but you should see a browser window pop up that looks like this:

<img src="https://files.realpython.com/media/01_initial_notebook_screen.cb2ea87d9679.png" width=600>

Now, you're running the Jupyter Notebook Server. This will allow you to make new notebooks, which we'll do now!

### Creating a Notebook

To make a new notebook, click on the New button (upper right), and it will open up a list of choices. From the dropdown menu, choose Python 3. Then, you should see something like the picture below -- this is a blank jupyter notebook

<img src="https://files.realpython.com/media/02_new_notebook.015b2f84bb60.png" width=600>

By default, the notebook file is called 'Untitled', so the first thing you may want to do is rename it. You can do this by bringing your mouse over the 'Untitled' name, then clicking it to be able to edit. Now you can put in the name of your choice.

<img src="https://files.realpython.com/media/03_hello_jupyter.96024ca79ae6.png" width=600>

Once you've done this, if you look in your computer's finder/file browser, you should see a file in the folder you are in with the name you just chose, with the extension `.ipynb`. You can recognize all files ending in `.ipynb` as jupyter notebooks. 

Remember to save your notebook often as you would with any other files! You can do this by clicking the save icon in the top left next to the `+` sign, or with command + s (Mac) / control + s (PC)

### Code Cells

Jupyter notebooks are made up of chunks called 'cells'. You can see the separate cells as the different blank chunks on the screen that allow you to type into them. The nice thing about jupyter notebooks is that you can interact with them by running **one cell at a time** without running all the others. You can make a new cell by clicking the `+` button at the top left part of the screen. If you click on the scissors, this will delete the cell you currently have slected.

The default cell type is a **code cell**. This is what you can use to write python.

Let's give this first code cell a try by adding 2+2. After you've written the code, you can **run** the cell by typing **shift + enter**


```python
2+2
```




    4



You should see some output like this. Notice that with this notebooks, we didn't need to use `print()` to see output the way we would using a script. The notebook automatically prints out many outputs for us!


Let's try printing some text as well to see how this works:


```python
print('Hi, jupyter notebook!')
```

    Hi, jupyter notebook!


If we don't use the `print()` function, things actually work pretty much the same way, except that by default, only the LAST line in the cell will be printed out. For example:


```python
'Hi, juypter notebook!'
'Time to code'
```




    'Time to code'



Here, we don't get any printout for 'Hi, jupyter notebook!'. So, it is important to remember that even though the last line of the cell can automatically show up, we still have to use `print()` if we want to print multiple things within a cell. For example, we could get both those strings to print with:


```python
print('Hi, juypter notebook!')
print('Time to code')
```

    Hi, juypter notebook!
    Time to code


One other great feature is that we can run code cells multiple times in a row! This helps a lot with debugging, but we also have to be careful with how this works if we're updating variables. To see why, try making a variable called `my_var` in one cell, and assigning it an integer value.


```python
my_var = 4
```

Now, in a new cell, let's add 1 to `my_var`, and save it back into itself. BUT, what happens if you now run this cell a bunch of times?


```python
my_var = my_var + 1
my_var
```




    9



This isn't necessarily a problm, but just something to be aware of! Order that cells are run in **matters** in jupyter notebook. You can use the up and down arrows towards the top panel of the screen to move cells up and down if needed (clicking on those will move the currently selected cell). When we're working with them, it often helps to restart and run code cells all the way from the beginning in order again. We'll get to how to do this soon. 

### Markdown Cells

You can use jupyter notebooks not only for code, but you can add text using Markdown cells too. To make a Markdown cell, click on the `+` at the top left to make a new cell, then select 'Markdown' from the dropdown menu (where it says 'Code') toward the top of the screen.

Markdown allows you to type text that will not be run as python code, but instead in the Markdown format. You can think of this as text with some fancy formatting. 

For example, you can use hashtags (#) to make headers. Just one hastag is the largest text, and the more hashtags, the smaller the header text will be.

<img src="https://files.realpython.com/media/07_headers.dc5aa8999b03.png" width=600>
<img src="https://files.realpython.com/media/08_headers.9cfb98853821.png" width=600>


Try making some markdown cells with headers in them to add a header above each code cell in your notebook.

We won't spend a lot of time on Markdown formatting now, but you can also add lists, bullets, **bold text**, *italics*, and even images or gifs. If you're interested, here is a [guide to using Markdown](https://medium.com/analytics-vidhya/the-ultimate-markdown-guide-for-jupyter-notebook-d5e5abf728fd)

## 3 ) Making and working with jupyter notebooks

The menus at the top of the page can really help your workflow with jupyter notebooks: 

### Using the menus

There are a couple of important things to know how to use from the menu at the top. 

<img src="https://files.realpython.com/media/02_new_notebook.015b2f84bb60.png" width=600>

Here are a few of the menu options that might help you get around:

**File** (generally anything for saving, copying, or making new files here):
* New Notebook
* Make a copy
* Rename
* Download as: this lets you download a viewable version of your document as an html or pdf file (or other formats). By default the downloaded file is in your Downloads folder


**Edit** (generally stuff for editing cells here):
* Cutting, copying, pasting, moving, and deleting cells
* Split cell: splits the cell into 2 cells at your cursor
* Finding & replacing

**Cell** (very useful for running different selections of cells):
* Run Cells: runs **selected** cells only
* Run all: runs all the cells. However, any variables you already have assigned before running all cells will stay in the environment and be used
* Run all above/run all below

**Kernel** (useful for **clean** restarts):
* Interrupt: stops cells from running (good if you're stuck with something taking a long time)
* Restart: this will *clean out* your whole environment -- all variables you have assigned will be deleted. Good if you want to 'reset'
* Restart and run all: This is a *clean run* of the whole notebook, as if you had closed down the server entirely and run it again. This is the best way to make sure your whole notebook runs by itself, in order.

**Logout button**:
* When you're done working, you can click the logout button at the very top right to close down your jupyter notebook server

We'll practice using these menus soon!

## More resources

[Jupyter notebooks documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

[A nice intro to jupyter notebooks](thttps://realpython.com/jupyter-notebook-introduction/) that this lesson borrowed from


[How to share and export jupyter notebooks](https://reproducible-science-curriculum.github.io/publication-RR-Jupyter/02-exporting_the_notebook/index.html) from Data Carpentry

[Project Jupyter](https://jupyter.org/) has info and updates on new things you can do with jupyter notebooks
