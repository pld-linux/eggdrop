#!/bin/sh

cd /usr/lib/eggdrop
exec ./eggdrop2 ${1+$@}
