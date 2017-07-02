import urllib2, cookielib, sys

output_file = "collected_cookies.txt"
f = open(output_file, 'w')
index_url = 0
index_cookie_name = 1
index_cookie_count = 2
debug_on = False


def show_usage_and_exit():
    print "Usage: python bycc-index.py <url> <cookie name> <cookie count>"
    sys.exit(1)


def main(argv):
    if not (len(argv) == 3 and type(argv[2]) == int):
        show_usage_and_exit()

    target_url = argv[index_url]
    target_cookie = argv[index_cookie_name]
    target_cookie_count = int(argv[index_cookie_count])

    while target_cookie_count > 0:
        retrieve_cookies(target_url,target_cookie)
        target_cookie_count = target_cookie_count - 1

    print "Script has been executed successfully. Check the output file named " + output_file + "."

def debug_response(res):
    if debug_on:
        print res.info()

def retrieve_cookies(url,cname):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    # to disguise as browser
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib2.install_opener(opener)
    response = urllib2.urlopen(url)

    debug_response(response)

    for cookie in cj:
        if cookie.name == cname:
            f.write(cookie.value + "\n")

if __name__ == "__main__":
    main(sys.argv)

