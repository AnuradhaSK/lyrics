from scrapy.spiders import SitemapSpider


class LyricsSpider(SitemapSpider):
    name = "lyrics"
    allowed_domains = ['lyricslk.com']
    sitemap_urls = [
        'http://lyricslk.com/sitemap.xml'
    ]
    # crawls links which does not contain artist. But this outputs some links like submit page etc
    sitemap_rules = [('^(?!.*artist).*$', 'parse')]

    # sitemap_follow = ['^((?!artist).)*$']
    def parse(self, response):
        song_lines = response.xpath('//*[@id="lyricsBody"]/text()').getall()
        song = ''
        for line in song_lines:
            song_line = line.split('\n')[1].strip()
            song = song + " " + song_line
        yield {
            'title': response.xpath('//*[@id="lyricsTitle"]/h2/text()')[0].get().split(' - ')[0],
            'singer': response.xpath('//*[@id="lyricsTitle"]/h2/text()')[0].get().split(' - ')[1],
            'song' : song
        }
        # page = response.url.split("/")[-1]
        # filename = 'lyrics-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)


