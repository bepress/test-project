#!/bin/bash

PyCodeStyle_output=`mktemp -t preflight_PyCodeStyle.XXXXXXXXX`
pyflakes_output=`mktemp -t preflight_pyflakes.XXXXXXXXX`

echo ''
echo ''
echo 'Python PyCodeStyle check output:'
echo ''
find . -type f -name \*.py \! -iregex '.*/versions.*' \! -iregex '.*/.env.*' \! -iregex '.*/migrations.*' \! -iregex '.*/docs.*' \! -iregex '.*/.docs_env.*' -print0 | xargs -P 4 -n 100 -0 \
    pycodestyle --max-line-length=132  2>&1 > "$PyCodeStyle_output"
cat "$PyCodeStyle_output"
if ! [ -s "$PyCodeStyle_output" ]; then
    echo "No PyCodeStyle errors found."
fi

echo ''
echo 'Python pyflakes check output:'
echo ''
find . -name \*.py \! -iregex '.*/versions.*' \! -iregex '.*/.env.*' \! -iregex '.*/migrations.*' \! -iregex '.*/docs.*' \! -iregex '.*/.docs_env.*' -print0 | xargs -P 4 -n 100 -0 pyflakes \
    | grep -v "unable to detect undefined names" 2>&1 > "$pyflakes_output"
cat "$pyflakes_output"
if ! [ -s "$pyflake_output" ]; then
    echo "No pyflakes errors found."
fi

errors=""

if [ -s "$PyCodeStyle_output" ] || [ -s "$pyflakes_output" ]; then
    errors=true
fi

rm -f "$PyCodeStyle_output"
rm -f "$pyflakes_output"

if [ "$errors" == true ]; then
    echo "Errors detected! See the above output."
    exit 1
else
    printf "\nSummary:\nScript is completed. No lint errors found with either pep8 or pyflakes. Horray!"
fi
