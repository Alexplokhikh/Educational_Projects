# =========================================================================
# 1. LISTS [] — Ordered, Mutable, Allows Duplicates
# Best for: Sequential data, log lines, arrays of servers where order matters.
# =========================================================================
print("--- 1. WORKING WITH LISTS ---")

# Lists can be changed (mutable) and keep their insertion order
my_list = ["abc", "xyz", 123, "abc"] # allows duplicates
print("Original List: ", my_list)

# Common manipulations (In-place mutation)
my_list.append("hello")
my_list.remove(123)
print("Mutated List: ", my_list)

# Slicing and indexing work exactly like in my previous guide
print("First item: ", my_list[0])
print("Last item: ", my_list[-1])
print("\n")


# =========================================================================
# 2. TUPLES () — Ordered, Immutable, Allows Duplicates
# Best for: Read-only data, fixed configurations (e.g., Database host and port).
# Data cannot be changed after creation, making it safer and faster than lists.
# =========================================================================
print("--- 2. WORKING WITH TUPLES ---")

# Defining a tuple (often used for constant config pairs)
my_tuple = ("abc", 321, "hey")
print("Original tuple: ", my_tuple)

# Accessing elements works via indices just like lists
print("first item: ", my_tuple[0])
print("Last item: ", my_tuple[-1])

### THE IMMUTABILITY TEST:
print("Can we change a tuple element like a list? Let's check:")
my_tuple[0] = "something" #⛔ Delete/Comment this line to make code run correctly
print(f"this line wont be printed: {my_tuple}") #⛔ we can Delete/Comment this too.

# Unpacking tuples (A very popular Python feature used in loops and functions)
first_item, second_item, third_item = my_tuple
print(f"Unpacked variables -> 1st: {first_item}, 2nd: {second_item}, 3rd: {third_item}")
print("\n")


# =========================================================================
# 3. SETS {} — Unordered, Mutable, NO Duplicates Allowed
# Best for: Finding unique items, deduplicating lists, and membership testing.
# Membership test (`item in set`) is O(1) - instantly fast even with millions of items!
# =========================================================================
print("--- 3. WORKING WITH SETS ---")

# Creating a set with duplicate values intentionally
my_set = {"abc", "def", "xyz", "abc", "xyz"}
# Sets automatically strip out duplicates and don't maintain order!
print("Unique IPs Set (Duplicates automatically removed): ", my_set)

# Adding and removing from a set
my_set.add("hello")
my_set.remove("def")
print("Set after add/remove: ", my_set)

# Real DevOps Scenario: Set Math (Intersections and Differences)
my_local_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.99"}
all_network_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4", "10.0.0.99"}

# Intersection: What IPs are in BOTH sets?
print("IPs present in both sets (Intersection): ", my_local_ips.intersection(all_network_ips))

# Difference: What network IPs have NOT been scanned yet?
unscanned_ips = all_network_ips.difference(my_local_ips)
print("Unscanned target IPs (Difference): ", unscanned_ips)

# Deduplicating a list using a set:
duplicate_list = ["app", "web", "app", "db", "web"]
unique_list = list(set(duplicate_list)) # Cast to set to clean, then back to list
print("Duplicated cleared set after casting: ", unique_list)
print("\n")


# =========================================================================
# 4. DICTIONARIES {"key": "value"} — Unordered/Ordered, Mutable, Unique Keys
# Use Cases: Key-Value structural mappings, parsing JSON payload, YAML configuration profiles.
# =========================================================================
print("--- 4. WORKING WITH DICTIONARIES ---")

# Defining a dictionary representing a server state
server_settings = {
    "hostname": "Ubuntu-64-host",
    "ip": "192.168.80.100",
    "cpu_cores": 4,
    "active": True,
    "tags": ["Testing", "Virtual"]
}
print("Original Dictionary Profile: ", server_settings)

# Accessing values safely using .get() vs direct brackets []
print("Accessing via bracket key: ", server_settings["hostname"])
# Bracket access fails with KeyError if key doesn't exist: .get() returns None safely!
print("Safe access via .get() (Existing key): ", server_settings.get("ip"))
print("Safe access via .get() (Non-existing key): ", server_settings.get("uptime", "Key Not Found"))

# Modifying and Adding structural key-values
server_settings["cpu_cores"] = 8           # Updates existing key
server_settings["memory_gb"] = 64          # Creates brand new key
del server_settings["active"]              # Deletes a key
print("Modified Dictionary Profile: ", server_settings)

# Slicing doesn't work on dicts, but we iterate using keys(), values(), or items()
print("\nLooping through dictionary structure:")
for key, value in server_settings.items():
    print(f"Key: {key:12} | Assigned Value: {value}")
print("\n")


# =========================================================================
# DEVOPS SUMMARY CARD: WHEN TO USE WHAT?
# =========================================================================
print("--- QUICK RECAP TABLE ---")
print("1. LISTS        -> Ordered & Mutable   -> Use for sequence/arrays arrays: [a, b, c]")
print("2. TUPLES       -> Ordered & Immutable -> Use for constant records/configs: (a, b, c)")
print("3. SETS         -> Unordered & Unique  -> Use for deduplication & filters: {a, b, c}")
print("4. DICTIONARIES -> Key-Value Pairs     -> Use for structured metadata/JSON: {k: v}")