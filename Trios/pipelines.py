# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class ShashPipeline:
    def process_item(self, item, samash):
        try:
            # Your processing logic goes here

            # Example: Log the item data
            samash.logger.info("Processing item: %s" % item)

            # Example: Perform additional processing on the item

            # Return the processed item
            return item

        except Exception as e:
            # Log and handle exceptions if needed
            samash.logger.error("Error processing item: %s. Error: %s" % (item, e))
            # You can also raise DropItem to discard the item in case of an error
            # raise DropItem(f"Error processing item: {item}")

