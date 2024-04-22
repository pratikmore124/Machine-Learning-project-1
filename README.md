## Git Machine-Learning-project-1

### Software and account Requirement 

1. [Git hub](https://github.com/)
2. [Heroku Account](https://www.heroku.com/)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)

Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```
To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

Setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = pratikmore124@gmail.com
2.HEROKU_API_KEY = HRKU-ba4219ca-dbb3-42e6-8a92-bba6563793b2
3. HEROKU_APP_NAME = git status


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tag_name> .
```
To list Docker image
```
docker images
```

Run Docker image
```
docker run -p 5000:5000 -e PORT=5000 <image id>
```

CHECK Running container in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```