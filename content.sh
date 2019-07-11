 git filter-branch -f --env-filter '
    WRONG_EMAIL="jgarrett@kabbage.com"
NEW_NAME="John Garrett"
NEW_EMAIL="jacgarrett18@gmail.com"

if [ "$GIT_COMMITTER_EMAIL" = "$WRONG_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$NEW_NAME"
    export GIT_COMMITTER_EMAIL="$NEW_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$WRONG_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$NEW_NAME"
    export GIT_AUTHOR_EMAIL="$NEW_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
echo "pwdfw"
echo "cmjne"
echo "aiqwr"
