#! /bin/sh
listText="buchanj-midwinter-00-t.txt charlesworth-scene-00-t.txt colby-champlain-00-t.txt delamare-lucy-00-t.txt delamare-penny-00-t.txt carman-farhorizons-00-t.txt cheyneyp-darkbahama-00-t.txt delamare-bumps-00-t.txt delamare-myfanwy-00-t.txt"

mkdir -p LinuxWordCount
cd LinuxWordCount

for i in $listText
do
    cat ../Data/$i | tr ' ' '\n' | sort | uniq -c > 1$i.txt
    cat ../Data/$i | tr ' ' '\n' | sort | uniq -c > 2$i.txt
    cat ../Data/$i | tr ' ' '\n' | sort | uniq -c > 3$i.txt
done