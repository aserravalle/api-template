# apprentice-minder
Forecasting, Retraining, and API components of the Apprentice Minder Project for the NSWBC

# How to use GitHub
Check out my command [line cheat sheet](https://github.com/aserravalle/command-line-cheat-sheet/blob/main/README.md)

**Clone repo and open master in VS Code**
```
cd "C:\Users\Ariel\Google Drive\Work\kuse\Finder Minder Phase 1\"
git clone https://github.com/aserravalle/apprentice-minder
cd apprentice-minder
code .
```
**Checkout (download) existing branch, open in VS Code**

Requires cloned repo
```
cd "C:\Users\Ariel\Google Drive\Work\kuse\Finder Minder Phase 1\apprentice-minder"
git checkout Ariel/BranchName
code .
```
**Checkout (download) new branch, open in VS Code**

Requires cloned repo
```
cd "C:\Users\Ariel\Google Drive\Work\kuse\Finder Minder Phase 1\apprentice-minder"
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
set FLASK_APP="C:\Users\Ariel\Google Drive\Work\kuse\Finder Minder Phase 1\apprentice-minder\app.py"
flask run
```
**Run tests**
```
set PYTHONPATH="C:\Users\Ariel\Google Drive\Work\kuse\Finder Minder Phase 1\apprentice-minder"
python -m unittest .
```
**Push changes to git**
```
git add .
git ls-files
git commit -m "message"
git push
```
