# import lib
from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("DataFrame_Test") \
    .getOrCreate()

# creating dataframe for products
product = [(i, f'product{i}') for i in range(10)]
product = spark.createDataFrame(
    product,
    ["id", "product_name"]
)
product.show()

# creating dataframe for categories
category = [(i, f'category{i}') for i in range(10)]
category = spark.createDataFrame(
    category,
    ["id", "category_name"]
)
category.show()

# creating connections between products and categories
product_category = [
    (1, 1),
    (1, 3),
    (2, 8),
    (3, 1),
    (3, 2),
    (3, 3),
    (4, 9),
    (4, 6),
    ]
product_category = spark.createDataFrame(
    product_category,
    ["product", "category"]
)
product_category.show()


def get_all_products_and_their_categories(product_category):
  return product_category \
  .join(category, product_category.category ==  category.id, "leftouter") \
  .join(product, product_category.product ==  product.id, "rightouter") \
  .select(product.product_name.alias('product'), \
          category.category_name.alias('category'))
  

get_all_products_and_their_categories(product_category).show(truncate=False)
spark.stop()
