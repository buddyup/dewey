hey_dewey --pre $@ > /tmp/dewey_pre && source /tmp/dewey_pre && rm /tmp/dewey_pre
hey_dewey $@
hey_dewey --post $@ > /tmp/dewey_post && source /tmp/dewey_post && rm /tmp/dewey_post