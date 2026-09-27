# Installing a text editor

Guide for: *MA in AI for Art and Design / MA in Human Interaction and AI, Elisava*

**In this guide**

1. [Installing text editor](#step-1-installing-our-code-editor)
2. [Setting up the editor](#step-2-set-up-vscode-for-python-development)

### Step 1: Installing our code editor

Firstly, we're going to need a program to edit our `python` code with. We'll use VSCode/VSCodium, which is easy to use and free. VSCode is the editor by Microsoft, while  VSCodium is an open source version without telemetry.

Both are easy to download, just choose one of your liking and go to:

- [https://code.visualstudio.com](https://code.visualstudio.com)
- [https://vscodium.com](https://vscodium.com)

Download and install.

### Step 2: Set up VSCode for python development

We're now ready to make sure that VSCode, can use the `python` interpreter we just installed. That way, for the rest of the course, we'll be able to work on your own laptops, exclusively in VSCode itself, which will be far simpler for all of us, and you'll be able to continue using it in future projects.

#### *Create a folder to store our code in and open it in VSCode*

1. First, click the “_files_” section in the left-hand sidebar (with this icon ![](/assets/image1.png)), and choose “_Open folder_”.
2. In the box that pops up, you can make a new folder called “_Code_”, wherever you want to keep your `python` code and select it. It'll ask you if you want to trust this folder, just choose “yes” - it's on your own computer and only you have access to it so it's no problem.

Your “code” folder should now be open in the left-hand sidebar, and we'll add our first python file to it in a sec.

#### *Install some useful extension for working with python*

We can add all sorts of add-ons to VSCode that do all sorts of extra things, something I'm trying to avoid as much as possible at the start of this course, so that you're all working in more or less the same environment, and to avoid introducing extra complexity we don't need. However, there are two extensions that will be very useful to us that we're going to install now. First, click the “extensions” tab in the sidebar, which has an icon like this:

![](/assets/image2.png)

Then, in the sidebar, search for `python`, and find the following two extensions in the list:

- The first, helpfully, is called just `python`. Clikck install:

  ![](/assets/image3.png)

  We'll see what the `python` extension does in just a second.

- The second is called “_Python Indent_”. Click “install” next to this one as well:

  ![](/assets/image4.png)

  You might be asked to trust the “_Python indent_” extension. Again, this is fine to do.

**Why this?** The “python indent” one solves a very annoying problem with python which we will explain imminently in class (briefly, in some situations it matters A LOT how much each line of code is indented from the edge of the page, and when we get it wrong the error message we get is singularly unhelpful. Installing this extension all but stops that from happening, which is handy).