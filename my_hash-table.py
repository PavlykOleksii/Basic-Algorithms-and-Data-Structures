# my_dict = {}

# my_dict["key1"] = "value1"
# my_dict["key2"] = "value2"
# print(my_dict)
# print(my_dict["key2"])
# del my_dict["key2"]
# print(my_dict)

# my_dict["key2"] = "value2"
# my_dict["key3"] = "value3"

# value = my_dict.get("key2")
# print(value)  

# my_dict["key2"] = "new value"
# print(my_dict) 

# key1 = "example"
# hash_value1 = hash(key1)
# print(hash_value1) 

# key2 = "another example"
# hash_value2 = hash(key2)
# print(hash_value2)

import hashlib

data = "example data"

# Використання SHA-256
hashed_data = hashlib.sha256(data.encode())
print(hashed_data.hexdigest())  # 44752f37272e944fd2c913a35342eaccdd1aaf189bae50676b301ab213fc5061
