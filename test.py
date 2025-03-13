# def hex_of_negative_integer(n):
#   if n >= 0:
#     return hex(n)[2:].upper().zfill(16)  # Ensure 64-bit padding
#
#   num_bits = 32  # 64-bit representation
#   max_val = 2 ** num_bits  # 2^64
#   twos_complement = n + max_val  # Compute two's complement
#
#   return hex(twos_complement)[2:].upper().zfill(16)  # Convert to uppercase and pad to 16 hex digits
#
#
# number = -2131965835
# # number = 307815036
# hex_value = hex_of_negative_integer(number)
# print(hex_value)

# 80ECC8752CEE2BC4


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, format_string

# Initialize Spark session
spark = SparkSession.builder.appName("HexConversion").getOrCreate()

# Sample DataFrame with integer column `KEY`
data = [(-2131965835,), (307815036,), (-1,)]
df = spark.createDataFrame(data, ["KEY"])

# Convert negative numbers to 64-bit two's complement hex representation
df = df.withColumn(
    "HEX_KEY",
    expr("""
        CASE
            WHEN KEY >= 0 THEN lpad(upper(hex(KEY)), 16, '0')
            ELSE lpad(upper(hex(KEY + POWER(2, 64))), 16, '0')
        END
    """)
)

# Show results
df.show(truncate=False)
