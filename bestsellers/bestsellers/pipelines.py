# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from csv import DictReader
import os
from bestsellers.infra.rabbitmq_publisher import RabbitMQPublisher
from bestsellers.settings import DATA_FILE, RABBITMQ_PUBLISHER_QUEUE


class BestsellersPipeline:
    def process_item(self, item, spider):
        return item


class SendMessagePipeline:
    def close_spider(self, spider):
        pids = get_pids(DATA_FILE)
        rabbitmq = RabbitMQPublisher()
        rabbitmq.publish_pids(pids)
        delete_files()


def get_pids(csv_file: str) -> dict:
    pids = set()
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = DictReader(f)
        for row in reader:
            pids.add(row["id"])
    return {
        RABBITMQ_PUBLISHER_QUEUE: list(pids)
    }  # TODO: usar pydantic para definir o formato do objeto


def delete_files() -> None:
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)