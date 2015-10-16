# i-Aor@Dict
i-Aor@Dict an English => Thai dictionary for Kindle E-Book

# How to create

1) Make word dictionary file with tab delimiter.

`$ python makeWord.py`

you will get output file `dict.txt`

2) Create `.opf` file for aggregate `.mobi` dictionary.

`$ python tab2opf.py -utf dict.txt`

3) convert to `.mobi`. (using Windows OS).

`$ ./mobigen ./dict.opf`

and then install `dict.mobi` on your kindle.
