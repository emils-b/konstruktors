from migrate_db import *

print("Migrate DB test")
print("-----")
print("Testing function \"mysql_check_if_table_exists\"")
# Testing that table do not exist
assert mysql_check_if_table_exists("Test") == []
print("OK")
print("-----")

print("Testing function \"mysql_exec_any_sql\"")
# Creating table using \"mysql_exec_any_sql\""
print("Creating table")
print("-----")
QUERY = "CREATE TABLE Test(ID int);"
mysql_exec_any_sql(QUERY)
print("OK")
print("-----")

# Testing that table  exist
print("Testing that table exists")
assert mysql_check_if_table_exists("Test") != []
print("OK")
print("-----")

# Dropping table using \"mysql_exec_any_sql\""
print("Dropping table")
print("-----")
QUERY = "DROP TABLE Test;"
mysql_exec_any_sql(QUERY)
print("OK")
print("-----")

# Testing that table do not exist
print("Testing that table do not exist anymore")
print("-----")
assert mysql_check_if_table_exists("Test") == []
print("OK")
print("-----")

