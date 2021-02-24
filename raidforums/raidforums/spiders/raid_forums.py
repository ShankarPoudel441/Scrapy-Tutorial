import scrapy
from scrapy import  Request
import re
from ..items import RaidforumsItem


class Quotespider(scrapy.Spider):
    name = 'database_posts'
    # allowed_domains = ["https://raidforums.com"]
    start_urls = [
        'https://raidforums.com/Forum-Databases'
    ]
    base_url = 'https://raidforums.com/'

    def parse(self, response):
        items = RaidforumsItem()

        post_div = response.xpath('/html/body/div[1]/main/section[2]/table[3]//tr')
        length = len(post_div)

        counter=0

        for post in post_div[9:length-1]:
            counter += 1
            print("counter", counter)
            items["post_name"] = post.css(".forum-display__thread-subject::text").extract()
            items["post_by"] = post.css(".author span::text").extract()

            try:
                post_date = post.xpath('.//div/span[2]/span::attr(title)').extract
                print(post_date)
                possibility = post.css('.forum-display__thread-date::text').extract()
                if (re.search("ago$", str(possibility)) == None):
                    items["post_date"] = post_date + possibility[-12:]
            except:
                items["post_date"] = post.css('.forum-display__thread-date::text').extract()

            items["post_views_no"] = post.css(".hidden-sm:nth-child(4)::text").extract()
            items["post_replies_no"] = post.css(".hidden-sm > a::text").extract()

            try:
                next_page = post.xpath("td[2]/div/div[1]/span[2]/a/@href").extract()
            except:
                next_page = post.xpath("td[2]/div/div[1]/span[2]/a/@href").extract()

            items["link_to_post"] = self.base_url + str(next_page)
            print("next page", items["link_to_post"])

            yield items

            # yield Request(items['link_to_post'],
            #                 meta={'items': items},
            #                 callback=self.parse_post)


    def parse_post(self,response):
        items = response.request.meta['items']
        items['actual_post'] = response.css('#pid_437190::text').extrract()
        items['user_name'] = response.css('.rf_god::text').extract()
        items['user_status'] = response.css('.post__user-title::text').extract()
        items['user_posts'] = response.css('.group:nth-child(1) .float_right ::text').extract()
        items['user_threads'] = response.css('.group:nth-child(2) .float_right ::text').extract()
        items['user_joined'] = response.css('.group:nth-child(3) .float_right ::text').extract()
        items['user_reputation'] = response.css('.group:nth-child(4) .float_right ::text').extract()
        try:
            items['user_service'] = response.css('.user_service::text').extract()
        except:
            items['user_service'] = "less than a year"

        print(items)

        yield items







        # / html / body / div[1] / main / section[2] / table[3] / tbody / tr[9]


        # print("length", len(post_div))
        # print(post_div)
        # # items["post_name"] = post_div.css(".forum-display__thread-subject::text").extract()
        # names = post_div.css(".forum-display__thread-subject::text").extract()
        # print("title-length",len(names))
        # print("post_names", names)
        #
        # counter = 0
        # for post in post_div:
        #     counter = counter +1
        #     name = post.css(".forum-display__thread-subject::text").extract()
        #
        #     yield {
        #         "name" : name,
        #         "counter" : counter
        #     }





        # for post in post_div:
            # items["post_name"] = post.css(".forum-display__thread-subject::text").extract()
            # items["post_by"] = post.css(".rf_i rf_vip::text").extract()
            # # items["post_date"] = post.css(".forum-display__thread-date::text").extract()
            # try:
            #     post_date = post_div.xpath('.//div/span[2]/span::attr(title)').extract
            #     possibility = post_div.css('.forum-display__thread-date::text').extract()
            #     if (re.search("ago$", str(possibility)) == None):
            #         items["post_date"] = post_date + possibility[-12:]
            # except:
            #     items["post_date"] = post.css('.forum-display__thread-date::text').extract()
            # items["post_views"] = post.css(".hidden-sm > a::text").extract()
            # items["post_replies"] = post.css(".trow2 forumdisplay_regular hidden-sm selectorgadget_suggested::text").extract()
            #
            # yield








# # items["post_by"] = post_div.css(".rf_i rf_vip::text").extract()
        # print("post_by", post_div.css(".author span::text").extract())
        # # items["post_date"] = post_div.css(".forum-display__thread-date::text").extract()
        # print("post_names", post_div.css(".forum-display__thread-date::text").extract())
        # # items["post_views"] = post_div.css(".hidden-sm > a::text").extract()
        # print("post_names", post_div.css(".hidden-sm > a::text").extract())
        # # items["post_replies"] = post_div.css(".hidden-sm > a::text").extract()
        # print("post_names", post_div.css(".hidden-sm > a::text").extract())
        # # yield items
