from scrapy import signals
from itemadapter import ItemAdapter

class ShashsamashMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your samashs.
        middleware = cls()
        crawler.signals.connect(middleware.samash_opened, signal=signals.samash_opened)
        return middleware

    def process_samash_input(self, response, samash):
        # Called for each response that goes through the samash middleware and into the samash.
        # Should return None or raise an exception.
        return None

    def process_samash_output(self, response, result, samash):
        # Called with the results returned from the samash, after it has processed the response.
        # Must return an iterable of Request, or item objects.
        for item_or_request in result:
            yield item_or_request

    def process_samash_exception(self, response, exception, samash):
        # Called when a samash or process_samash_input() method (from other samash middleware) raises an exception.
        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, samash):
        # Called with the start requests of the samash, and works similarly to the process_samash_output() method,
        # except that it doesn’t have a response associated.
        # Must return only requests (not items).
        for request in start_requests:
            yield request

    def samash_opened(self, samash):
        self.logger.info("samash opened: %s" % samash.name)


class ShashDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your samashs.
        middleware = cls()
        crawler.signals.connect(middleware.samash_opened, signal=signals.samash_opened)
        return middleware

    def process_request(self, request, samash):
        # Called for each request that goes through the downloader middleware.
        # Must either return None to continue processing this request or return a Response or Request object.
        return None

    def process_response(self, request, response, samash):
        # Called with the response returned from the downloader.
        # Must either return a Response object, a Request object, or raise IgnoreRequest.
        return response

    def process_exception(self, request, exception, samash):
        # Called when a download handler or a process_request() (from other downloader middleware) raises an exception.
        # Must either return None to continue processing this exception,
        # return a Response object to stop process_exception() chain, or return a Request object to stop the chain.
        pass

    def samash_opened(self, samash):
        self.logger.info("samash opened: %s" % samash.name)
