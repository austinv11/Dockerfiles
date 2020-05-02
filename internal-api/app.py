import os

from flask import Flask, jsonify
from github import Github

app = Flask(__name__)

github = Github(os.environ.get('ACCESS_TOKEN'))


@app.route("/versions", methods=["GET"])
def handle():
    repo = github.get_repo("Discord4J/Discord4J")
    releases = list()
    for release in repo.get_releases():
        releases.append({
            "tag": release.tag_name,
            "title": release.title,
            "prerelease": release.prerelease,
            "url": release.url
        })

    return jsonify(releases)


@app.route("/")
def home():
    return "Hello World"


if __name__ == '__main__':
    app.run('0.0.0.0')
