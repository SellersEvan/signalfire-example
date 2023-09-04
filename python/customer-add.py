# - Success
# - Failure
# - Faulure w/ Code

import sys

print("name          : " + sys.argv[1])
print("founded       : " + sys.argv[2])
print("industry      : " + sys.argv[3])
print("description   : " + sys.argv[4])
print("ceo           : " + sys.argv[5])
print("force_outcome : " + sys.argv[6])

print("\n")
print("============== Preparing ==============");
print("Checking for duplicated name...")
print("No duplicated name found")
print("Validating founding year...")
print("Validating industry...")

print("\n")
print("============== Uploading ==============");
print("Scanning for additional company details...")
print("Uploading company to database...")
print("Scanning for products...")
print("Uploading products to database...")

if sys.argv[6] == "SUCCESS":
    print("Successfully Updated")
    sys.exit()
elif sys.argv[6] == "EXCEPTION":
    raise Exception("WTF IS GOING ON!!!!")
elif sys.argv[6] == "FAILED":
    print("SF-STATUS=FAILED")
elif sys.argv[6] == "EXIT_1":
    sys.exit(1)
elif sys.argv[6] == "EXIT_2":
    sys.exit(2)
elif sys.argv[6] == "EXIT_STR":
    sys.exit("EXIT STRING")


# New Line