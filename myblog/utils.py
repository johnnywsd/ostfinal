import re
from myblog import constant
def linkstr2url_match(m):
    plain_text_url = m.group('url')
    plain_text_url = plain_text_url.lower()
    dot_last_index = plain_text_url.rfind('.')
    if dot_last_index == -1:
        format = '<a href="%(url)s">%(url)s</a>'
    else:
        ext = plain_text_url[dot_last_index+1:]
        #if ext in ['jpg', 'png', 'jpeg']:
        if ext in constant.IMG_EXTS:
            format = '<img src="%(url)s">'
        else:
            format = '<a href="%(url)s">%(url)s</a>'

    return format % {'url': plain_text_url} 

def plain2link(text):
    pattern = r'(?<!["|(>)])(?P<url>https?://\S*)'
    p = re.compile(pattern, re.IGNORECASE)
    return p.sub(linkstr2url_match, text)


if __name__ == '__main__':

    st = '<a href="http://www.baidu.com">http://www.baidu.com</a> http://www.google.com https://www.douban.com/a.jpeg https://developers.google.com/edu/python/images/hello.png'
    print plain2link(st)
