import os
pairs = []
for root, directories, files in os.walk(r"/Users/liliia.khomyn/Documents"):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        pairs.append((size, file))

# Sort list of tuples by the first element, size.
pairs.sort(key=lambda s: s[0], reverse = True)

# Display 10 largest files
for pair in pairs:
    last_values = pairs[0:10]
print("Top 10 largest files are: ")
print(last_values)