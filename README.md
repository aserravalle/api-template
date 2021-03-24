# Flask API Template
start here

# How to use GitHub
Check out my command [line cheat sheet](https://github.com/aserravalle/command-line-cheat-sheet/blob/main/README.md)

**Clone repo and open master in VS Code**
```
git clone https://github.com/aserravalle/apprentice-minder
cd apprentice-minder
code .
```
**Checkout (download) existing branch, open in VS Code**

Requires cloned repo
```
git checkout Ariel/BranchName
code .
```
**Checkout (download) new branch, open in VS Code**

Requires cloned repo
```
git checkout -b Ariel/BranchName
code .
```
**Run python virtual environment, install requirements**
```
python -m venv .
Scripts\activate
pip install -r requirements.txt
```
**Run flask**
```
set FLASK_APP="C:\Users\repo\app.py"
flask run
```
**Run tests**
```
set PYTHONPATH="C:\Users\repo"
python -m unittest .
```
**Push changes to git**
```
git add .
git ls-files
git commit -m "message"
git push
```
