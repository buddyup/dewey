
docopt-completion hey_dewey --manual-bash > /dev/null
mv hey_dewey.sh .dewey_autocomplete.sh

echo "" >> .dewey_autocomplete.sh
echo "complete -F _hey_dewey hey_dewey" >> .dewey_autocomplete.sh
echo "complete -F _hey_dewey dewey" >> .dewey_autocomplete.sh
echo "complete -F _hey_dewey d" >> .dewey_autocomplete.sh

source .dewey_autocomplete.sh

function _run_dewey() {
    `hey_dewey --pre $@`;
    hey_dewey $@;
    `hey_dewey --post $@`;
}

alias d="_run_dewey"
alias dewey="_run_dewey"