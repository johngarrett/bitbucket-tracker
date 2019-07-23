import git
from git_contributions_importer import *

root_repo = git.Repo("/Users/jgarrett/Desktop/CardScan")
# Your mock repo
fake_repo = git.Repo("/Users/jgarrett/Desktop/kabbage-tracking")
importer = Importer([root_repo], fake_repo)

importer.set_author(['jacgarrett18@gmail.com', 'jgarrett@kabbage.com'])
importer.import_repository()
