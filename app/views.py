from flask import render_template
from app import app
from github import Github
import base64
import os

@app.route("/")
def index():
    content = gitFileGetContent(os.environ.get('GITSPEAKER_GH_REPOSITORYNAME'), os.environ.get('GITSPEAKER_GH_FIRSTFILENAME'))
    return render_template('index.html', content = content)


def gitFileGetContent(repositoryName, filename):
    return 'Delermando'
    github = Github(os.environ.get('GITSPEAKER_GH_USERNAME'), os.environ.get('GITSPEAKER_GH_PASSWORD'))
    user = github.get_user()
    repository = user.get_repo( repositoryName )
    gitFile = repository.get_contents( filename )
    return base64.b64decode(gitFile.content)
