git init
git remote add
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git commit -m "message"
asdawdwa
1. Generate a Personal Access Token (PAT)

If you’re using GitHub:

    Go to GitHub.com > Settings > Developer settings > Personal access tokens.
    Click Generate new token.
    Select the scopes/permissions you need (e.g., repo for full control of private repositories).
    Generate the token and copy it. You won’t be able to see it again!

2. Set Up Git to Use the Token

Option B: Cache the Token in Git Configuration

    Set the remote URL with the token (not recommended for shared or insecure environments):

git remote set-url origin https://<TOKEN>@github.com/username/repository.git

Replace <TOKEN>, username, and repository with your information.


