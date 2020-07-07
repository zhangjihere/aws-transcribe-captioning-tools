#!/bin/bash

IFS=$'\n'
na=$(ls -1 ./ | grep -v "\.sh")
for n in $na
do
    echo ${n}
    n_key=$(echo $n | sed 's/\.mp4/.json/g')
    echo ${n_key}
    n_origin=$(echo $n | sed 's/^English_//g' | sed 's/_/ /g' | sed 's/\.mp4/.srt/g')
    echo ${n_origin}
    # mv ${n} ${n2}
    python ~/projects_repo/aws-transcribe-captioning-tools/src/srt.py -tsKey ${n_key} -srtFile ${n_origin}
done

