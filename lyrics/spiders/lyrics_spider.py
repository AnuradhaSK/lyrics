from scrapy.spiders import SitemapSpider

class LyricsSpider(SitemapSpider):
    name = "lyrics"
    allowed_domains = ['lyricslk.com']
    sitemap_urls = [
        'http://lyricslk.com/sitemap.xml'
    ]
    # crawls links which does not contain artist. But this outputs some links like submit page etc
    sitemap_rules = [('^(?!.*artist).*', 'parse')]
    # sitemap_follow = ['^((?!artist).)*$']
    def parse(self, response):
        yield {
            'title': response.xpath('//*[@id="lyricsTitle"]/h2/text()')[0].get().split('- ')[0],
            'singer': response.xpath('//*[@id="lyricsTitle"]/h2/text()')[0].get().split('- ')[1],
        }
        # page = response.url.split("/")[-1]
        # filename = 'lyrics-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

