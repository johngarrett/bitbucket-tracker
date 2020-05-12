import git
import os
from git_contributions_importer import *

root_repo = git.Repo(input('Path to the repo to track: ').strip())
original_author = input('who was the original author?')
new_author = input('who is the newauthor?')

fake_repo = git.Repo(os.getcwd())
importer = Importer([root_repo], fake_repo)

importer.set_author([new_author, original_author])
importer.import_repository()

os.system(f'./script.sh {original_author} {new_author}')
