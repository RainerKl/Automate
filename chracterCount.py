message='It was a bright cold day in April, and the clocks were striking thirteen.'
count={}

for character in message.upper():
    count.setdefault(character,0)
    count[character]=count[character]+1
    
import pprint
pprint.pprint(count)
rjtext=pprint.pformat(count)
print(rjtext)


count.keys()
count.values()
count.items()