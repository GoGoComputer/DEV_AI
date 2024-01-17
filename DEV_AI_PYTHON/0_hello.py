print ("hello world")


# 1. Install Python3: https://www.python.org/downloads/
# 2. vscode download: https://code.visualstudio.com/
# 3. vscode extension: Python3
# 4. vscode extension: Code Runner

# crate a new venv
    # terminal: python3 -m venv myvenv # my env name: myvenv
    # activate myvenv
    # terminal: source myvenv/bin/activate
    
    # will deactivate the virtual environment
    # terminal: deactivate


# create a new file: 0_hello.py
    # print ("hello world") and save file
    # check python3 version terminal: python3 --version
    # teminal: sudo apt install
    # teminal: cd to the file path in terminal
    # Run Python File in VSCODE  (0_hello.py)
    
# open ai package
    # 1. activate myvenv
    # terminal: pip3 install openai
    
# openai API call
    # 1. make file .env
    # 2. add API key to .env file
    # 3. in .env file write: OPENAI_API_KEY= sk-xxxxxxx
    
# gitignore [very very important!!!]
    # 1. make file .gitignore
    # 2. add myvenv to .gitignore file
    # 3. add .env to .gitignore file
    # 4. add myvenv to .gitignore file
    
    
# git setup
    # will deactivate the virtual environment (myvenv)
    # terminal: deactivate
    # cd to the file path in terminal (DEV_AI)
    # 1. git init
    # terminal: git init
    # 2. check git version
    # terminal: git --version
    # 3. update git
    # terminal: sudo apt-get update
    
    
    # 4 Setting up a Git configuration file
         #To set up a Git configuration file,
         # open the command line of the distribution 
         # you're working with and set the name with 
         # the following command (replacing "Your Name" 
         # with your preferred username).
    # terminal: git config --global user.name "Your Name"
    # teminal: git config --global user.email "youremail@domain.com"
    # 5. check git config
    # terminal: git config --list
    

    # 6. add files to git
    # terminal: git add .
    # 7. commit files to git
    # terminal: git commit -m "first commit"
    
    # push to github
    # 1. create a new repository in github
    # 2. copy the HTTPS or SSH URL
    # 3. add remote repository
    # terminal: git branch -M main
    # terminal: git remote add [origin or etc] [HTTPS or SSH URL] (delete => [])
    # terminal: git push -u origin main
    
# git commit
    # terminal: git add .
    # terminal: git commit -m "first commit"
    
# git push
    
    # terminal: git push -u origin main
    
    # end 0_hello.py
    # Path: DEV_AI_PYTHON/0_hello.py
    
    
    