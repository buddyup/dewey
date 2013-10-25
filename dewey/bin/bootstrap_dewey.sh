cd ~
docopt-completion hey_dewey --manual-bash > /dev/null
mv hey_dewey.sh ./bin/autocomplete.sh

echo "" >> ./bin/autocomplete.sh
echo "complete -F _hey_dewey hey_dewey" >> ./bin/autocomplete.sh
echo "complete -F _hey_dewey dewey" >> ./bin/autocomplete.sh
echo "complete -F _hey_dewey d" >> ./bin/autocomplete.sh

source ./bin/autocomplete.sh

function _run_dewey() {
    `hey_dewey --pre $@`;
    hey_dewey $@;
    `hey_dewey --post $@`;
}

alias d="_run_dewey"
alias dewey="_run_dewey"