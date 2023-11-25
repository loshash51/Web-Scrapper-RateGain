import scrapy
import json
import os

blog_entries = []

class Projectsamash(scrapy.samash):
    name = "project"
    allowed_domains = ["rategain.com"]
    start_urls = ["https://rategain.com"]

    def start_requests(self):
        base_url = "https://rategain.com/blog/page/{}/"
        for page_number in range(1, 47):
            url = base_url.format(page_number)
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for entry_number in range(1, 10):
            title_selector = f".with-image:nth-child({entry_number}) h6 a"
            product_title = response.css(title_selector).css("::text").extract()

            if not product_title:
                title_selector = f".category-blog:nth-child({entry_number}) h6 a"
                product_title = response.css(title_selector).css("::text").extract()
                date_selector = f".category-blog:nth-child({entry_number}) .material-design-icon-history-clock-button+ span"
                product_date = response.css(date_selector).css("::text").extract()
                like_selector = f".category-blog:nth-child({entry_number}) .zilla-likes"
                product_like = response.css(like_selector).css("::text").extract()

                product_real = product_like[1] if product_like else product_like

                data = {
                    "Product Title": product_title,
                    "Product Date": product_date,
                    "Product Like": product_real
                }
                if all([product_title, product_date, product_real]):
                    blog_entries.append(data)

            else:
                title_selector = f".with-image:nth-child({entry_number}) h6 a"
                product_title = response.css(title_selector).css("::text").extract()
                date_selector = f".with-image:nth-child({entry_number}) .material-design-icon-history-clock-button+ span"
                product_date = response.css(date_selector).css("::text").extract()
                image_selector = f".with-image:nth-child({entry_number}) .rocket-lazyload"
                product_image = response.css(image_selector).css("::attr(data-bg)").extract()
                like_selector = f".with-image:nth-child({entry_number}) .zilla-likes"
                product_like = response.css(like_selector).css("::text").extract()

                product_real = product_like[1] if product_like else product_like

                data = {
                    "Product Title": product_title,
                    "Product Date": product_date,
                    "Product Image": product_image,
                    "Product Like": product_real
                }
                if all([product_title, product_date, product_real, product_image]):
                    blog_entries.append(data)

        output_directory = "D:\\DC++"
        output_path = os.path.join(output_directory, "blog_data.json")
        with open(output_path, "w") as json_file:
            json.dump(blog_entries, json_file, indent=4)
