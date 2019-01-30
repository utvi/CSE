states = {
    "CA": "California",
          "VA": "Virginia",
          "MD": "Maryland",
          "RI": "Rhode Island",
          "NV": "Nevada"
}

# print(states["CA"])
# print(states["NV"])

nested_dictionary = {
          "CA": {
              "NAME": "California",
              "POPULATION": 39540000    # 39,540,000
          },
          "VA": {
              "NAME": "Virginia",
              "POPULATION": 8500000     # 8,517,685
          },
          "MD": {
              "NAME": "Maryland",
              "POPULATION": 6042718     # 6,042,718
          },
          "RI": {
              "NAME": "Rhode Island",
              "POPULATION": 1057318     # 1,057,318
          },
          "NV": {
              "NAME": "Nevada",
              "POPULATION": 3034392     # 3,034,392
          }
}

# print(nested_dictionary["NV"]["POPULATION"])
print(nested_dictionary["RI"]["NAME"])

complex_dictionary = {
          "CA": {
              "NAME": "California",
              "POPULATION": 39540000,    # 39,540,000
              "CITIES": [
                  "Fresno",
                  "San Francisco",
                  "Los Angeles",
              ]
          },
          "VA": {
              "NAME": "Virginia",
              "POPULATION": 8500000,     # 8,517,685
              "CITIES": [
                  "Richmond",
                  "Norfolk",
                  "Alexandria"
              ]
          },
          "MD": {
              "NAME": "Maryland",
              "POPULATION": 6042718,     # 6,042,718
              "CITIES": [
                  "Bethesda",
                  "Baltimore",
                  "Annapolis"
              ]
          },
          "RI": {
              "NAME": "Rhode Island",
              "POPULATION": 1057318,     # 1,057,318
              "CITIES": [
                  "Providence",
                  "Newport",
                  "Warwick"
              ]
          },
          "NV": {
              "NAME": "Nevada",
              "POPULATION": 3034392,     # 3,034,392
              "CITIES": [
                  "Las Vegas",
                  "Reno",
                  "Carson City"
              ]
          }
}
print(complex_dictionary["RI"]["CITIES"][2])

print(complex_dictionary["VA"]["NAME"])
print(complex_dictionary["MD"]["CITIES"][0])

print(complex_dictionary.keys())
print(nested_dictionary.items())

print()
for key,value in complex_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)


for state, facts in complex_dictionary.items():
    for attr, value in facts.items():
        print(attr)
        print(value)
        print("-" * 20)
    print("=" * 20)