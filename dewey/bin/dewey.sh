#!/usr/bin/env bash
eval $(hey_dewey --pre $@)
hey_dewey $@
eval $(hey_dewey --post $@)