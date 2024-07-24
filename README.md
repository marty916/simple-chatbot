# Chatbot Setup with FastAPI and OpenAI

This guide will walk you through setting up a chatbot using FastAPI and the OpenAI API. 

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)

## Steps to Set Up the Chatbot

### Step 1: Create a New Folder for Your Chatbot

Create a new folder on your computer where you will store your chatbot project.

### Step 2: Open the New Folder with VS Code

Open Visual Studio Code and use the `Open Folder` option to open the newly created folder.

### Step 3: Open the Terminal in VS Code

In the VS Code command bar, select `Terminal`. If you don't see it, click on the `...` menu to find the terminal option.

### Step 4: Create a New Terminal

Click `New Terminal`. A terminal window will open at the bottom of VS Code.

### Step 5: Create and Activate a Python Virtual Environment

Run the following commands one at a time in the terminal to create and activate a virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

# Activate the virtual environment
source venv/bin/activate
```
### Step 6: Install required libraries
```bash
pip install fastapi uvicorn openai websockets
```

## Getting a copy of the code
- [simple-chabot](https://github.com/marty916/simple-chatbot)

### Option 1: Using Git (Recommended)
1. Open Terminal/Command Prompts
2. Navigate to desired directly (don't create the simple-chatbot directory git clone will do it for you)
3. Use the git clone command (copy this command)
```bash
git clone https://github.com/marty916/simple-chatbot.git
```
4. After cloning, navigate into the newly created directory
```bash
cd simple-chatbot
```

### Option 2: Downloading the ZIP file


