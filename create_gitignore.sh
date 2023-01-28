#!/bin/bash
FILE=".gitignore_test"

echo "Test if $FILE file exists"
if test -f "$FILE"; then
	echo "$FILE File exists"
	exit 1; fi

if test -d .git; then
	echo "Checkout to the branch"
	git flow feature start create-gitignore-file

	echo "Creating $FILE file"
	echo "________________________"
	echo "log_worker.yaml" > "$FILE"
	echo "config.ini" >> "$FILE"
	echo "log_migrate_db.yaml" >> "$FILE"
	echo "log/*.log" >> "$FILE"
	echo "log/*log.*" >> "$FILE"
	echo "$FILE created"

	echo "Commiting changes"
	git add "$FILE"
	git commit -m "Created $FILE"
	git flow feature finish create-gitignore-file
	echo "Pushing changes"
	git push
else
	echo "Create GIT repository first"
	exit 1; fi


