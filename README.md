# DVC-Data-Version
This repository implements the idea of data versioning using DVC.

1. Create git repository <"DVC-Data-Version"> creating only 3 files .gitignore, LICENSE, and README.md files.
2. clone this repository in local. 
```bash
git clone <https://github.com/sgphule/DVC-Data-Version.git>
```  
3. Open this project with PyCharm IDE 
4. Create "DVC Data Version" virtual environment .venv considering Python 3.9 interpreter (usually it has default 3 packages pip, setuptools and wheels).
5. Install "pandas" and "os" packages.
6. Implement data_generate.py and execute to generate and save info.csv file to a "data" directory.
```bash
python data_generate.py
```
7. Create blank requirements.txt file.
8. Fire following commands for code versioning by git.
```bash
git add data_generate.py requirements.txt
```
```bash
git commit -m "generate csv data"
```
```bash
git push
```
```bash
git log --oneline
```

9. Install DVC on terminal. 
```bash
pip install dvc
```
10. Initialize DVC which creates ".dvcignore", ".dvc".
```bash
dvc init
```
11. Create new directory "S3".
12. Inform DVC about remote.
```bash
dvc remote add -d myremote S3
```
13. Track data directory changes with DVC creating data.dvc.
```bash
dvc add data/
```
```bash
dvc commit
```
```bash
dvc push
```
```bash
git status
```
```bash
git add data.dvc .dvc/config .gitignore
```
```bash
git commit -m "Fist version of data"
```
```bash
git push
```
```bash
git log --oneline
```
```bash
dvc status
```
14. Change data_generate.py to append a new row in data & execute changing the data in data directory.
15. verify data changes.
```bash
dvc status
```
```bash
dvc commit
```
```bash
dvc push
```
```bash
dvc status
```

16. mark this second version of data.
```bash
git add data.dvc .\data_generate.py
```
```bash
git commit -m "Second version of data"
```
```bash
git push
```
```bash
git log --oneline
```

17. Now repeat step 14-16 for third version of data followed by.
```bash
cat data/info.csv 
```

18. rollback to first version.
```bash
git checkout 9bb996e 
```
```bash
dvc status
```
19. Status shows mismatch hence get correct version of data.
```bash
dvc pull
```
20.  See info.csv contents.
```bash
cat data/info.csv 
```
21. Once again revert back to latest version of data.
```bash
git checkout main
```
```bash
dvc status
```
22. dvc status show mismatch hence get correct version of data.
```bash
dvc pull
```
23. See info.csv contents
```bash
cat data/info.csv
```
23. Generate requirements.txt file
```bash
pip3 freeze > requirements.txt
```
