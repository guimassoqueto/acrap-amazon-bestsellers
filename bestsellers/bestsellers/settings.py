from os import getenv
from dotenv import load_dotenv
load_dotenv()

POSTGRES_PORT = getenv("POSTGRES_PORT") or 5432
POSTGRES_DB = getenv("POSTGRES_DB") or "postgres"
POSTGRES_USER = getenv("POSTGRES_USER") or "postgres"
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD") or "password"
POSTGRES_HOST = getenv("POSTGRES_HOST") or "0.0.0.0"

POSTGRES_TABLE_NAME = getenv("POSTGRES_TABLE_NAME") or "executions"
RABBITMQ_DEFAULT_USER = getenv("RABBITMQ_DEFAULT_USER") or "user"
RABBITMQ_DEFAULT_PASS = getenv("RABBITMQ_DEFAULT_PASS") or "password"
RABBITMQ_DEFAULT_HOST = getenv("RABBITMQ_DEFAULT_HOST") or "localhost"
RABBITMQ_PUBLISHER_QUEUE = getenv("RABBITMQ_PUBLISHER_QUEUE") or "amazon-colly"

BOT_NAME = "bestsellers"

ROBOTSTXT_OBEY = False

SPIDER_MODULES = ["bestsellers.spiders"]
NEWSPIDER_MODULE = "bestsellers.spiders"

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

CONCURRENT_REQUESTS = int(getenv("MAX_CONCURRENCY")) or 16

DOWNLOAD_HANDLERS = {
  "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
  "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

PLAYWRIGHT_BROWSER_TYPE = "firefox"

PLAYWRIGHT_LAUNCH_OPTIONS = {
  "headless": True,
  "timeout": 20 * 1000,  # 20 seconds
}

PLAYWRIGHT_CONTEXTS = {
    "default": {
        "viewport": {
            "width": 1920,
            "height": 15000,
        },
    },
}

ITEM_PIPELINES = {
  "bestsellers.pipelines.BestsellersPipeline": 300,
  "bestsellers.pipelines.SendMessagePipeline": 400,
}

RETRY_TIMES = 20

DATA_FILE = "bestsellers.csv"
FEEDS = {DATA_FILE: {"format": "csv"}}