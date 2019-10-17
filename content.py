import git
import os
from git_contributions_importer import *

root_repo = git.Repo(input('Path to the repo to track: ').strip())
fake_repo = git.Repo(os.getcwd())
importer = Importer([root_repo], fake_repo)

importer.set_author(['jacgarrett18@gmail.com', 'jgarrett@kabbage.com'])
importer.import_repository()

os.system('./script.sh')
