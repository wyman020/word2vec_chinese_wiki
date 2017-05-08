#!/bin/bash

# preprocess 1. language transform 2. splitting words 3. encoding transform

# Traditional Chinese to Simplified Chinese
echo "opencc: Traditional Chinese to Simplified Chinese..."
#time opencc -i wiki.zh.txt -o wiki.zh.chs.txt -c zht2zhs.ini
time opencc -i wiki.zh.txt -o wiki.zh.chs.txt -c t2s.json

# Cut words
echo "jieba: Cut words..."
time python -m jieba -d ' ' wiki.zh.chs.txt > wiki.zh.seg.txt

# Change encode
echo "iconv: ascii to utf-8..."
time iconv -c -t UTF-8 < wiki.zh.seg.txt > wiki.zh.seg.utf.txt
