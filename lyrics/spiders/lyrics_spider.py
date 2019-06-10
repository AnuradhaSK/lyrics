from scrapy.spiders import SitemapSpider

class LyricsSpider(SitemapSpider):
    name = "lyrics"
    allowed_domains = ['lyricslk.com']
    sitemap_urls = [
        'http://lyricslk.com/sitemap.xml'
    ]
    sitemap_rules = [('/lyrics/artist/', 'parse')]
    sitemap_follow = ['/amaradewa-w-d']
    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'lyrics-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

