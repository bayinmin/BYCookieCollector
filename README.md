# BYCookieCollector
Python script to collect defined number of target cookies from a website.

Sometimes, one might need to collect variable amount of session id cookie to perform analysis on the randomness of the session id cookie.

This script help to collect target cookie and output to a file.

Example
=======
The following example shows how to retrieve 10 JSESSIONID from WebGoat landing page hosted locally. The 10 session id retrieved were written into collected_cookies.txt. 

![Hello](https://github.com/bayinmin/BYResources/blob/master/BYCookieCollector/pic-bycookiecollector-usage.png)


Usage
=====
1. Open command prompt and navigate to bycc-index.py folder
2. Run the script with the following format --> python bycc-index.py \<url\> \<cookie name\> \<cookie count\>
3. Check the output file for collected cookies





