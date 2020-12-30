import re

def print_match(m):
    if m:
        print(m.group())
        print(m.string)
        print(m.start())
        print(m.end())
        print(m.span())
    else:
        print("NOT MATCHED")


p = re.compile("ca.e") # . -> only one chr
# ^ -> (^de) start point .. desk, destination
# $ -> (se$) end point.. case, base


#m = p.match("care less") # from the first index
#m = p.match("lesscare")
#print_match(m)

#m = p.search("goodcare")
#print_match(m)

lst = p.findall("good care cafe")
print(lst)

