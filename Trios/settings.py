# Scrapy settings for shash project

BOT_NAME = "shash"

# Spider modules
SPIDER_MODULES = ["shash.samash"]
NEWSPIDER_MODULE = "shash.samash"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Download settings
CONCURRENT_REQUESTS = 16
# DOWNLOAD_DELAY = 3
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Cookies and Telnet Console
# COOKIES_ENABLED = False
# TELNETCONSOLE_ENABLED = False

# Request headers
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Middleware settings
# samash_MIDDLEWARES = {
#    "shash.middlewares.shashsamashMiddleware": 543,
# }
# DOWNLOADER_MIDDLEWARES = {
#    "shash.middlewares.shashDownloaderMiddleware": 543,
# }

# Extensions settings
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Item pipelines
# ITEM_PIPELINES = {
#    "shash.pipelines.shashPipeline": 300,
# }

# AutoThrottle extension
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# AUTOTHROTTLE_DEBUG = False

# HTTP caching
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Autoconfigure deprecated settings
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
