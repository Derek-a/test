from urllib import request


class HtmlDownloader(object):
    @staticmethod
    def download(url):
        if url is not None:
            try:
                r = request.urlopen(url, timeout=10)
                if r.getcode() == 200:
                    return r.read().decode("UTF-8")
                else:
                    return None
            except Exception as e:
                print(str(e))
        else:
            return None
