integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_list = [integer_list, heterogeneous_list, []]

print(list_of_list)

list_length = len(integer_list)
list_sum = sum(integer_list)

x = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a = x[1:5]

first_three = x[5:2:-1]
print(first_three)

1 in [1, 2, 3]
0 in [1, 2, 3]


x = [1, 2, 3]
x.extend([4, 5, 6])

print(x)


x, y = [1, 2]
print(x, y)

_, y = [3, 4]

print(y)

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4

print(my_tuple)
print(other_tuple)

"""
try:
    my_tuple[1]=3
except TypeError:
    print("cannot modify a tuple")
"""


def sum_and_product(x, y):
    return (x+y), (x*y)


sp = sum_and_product(2, 3)
s, p = sum_and_product(5, 10)

print(sp)
print(s, p)


x, y = 1, 2
x, y = y, x


empty_dict = {}
grades = {"Joel": 80, "Tim": 95}

print(grades)

joels_grade = grades["Joel"]

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate")    
    
joel_has_grade = "Joel" in grades
kate_has_grade = "Kate" in grades

print(joel_has_grade)
print(kate_has_grade)  


joels_grade = grades.get("Joel",0)
kates_grade = grades.get("Kate",0)
no_ones_grade = grades.get("No One",1)

print(no_ones_grade)  

grades["Tim"]=99
grades["Kate"]=100
num_students = len(grades)

print(num_students)


tweet = {
    "user":"joelgrug",
    "text":"Data Science is Awesome",
    "retweet_count":100,
    "hashtags": ["#data","#science","#yolo"]
}

tweet_keys = tweet.keys()
print(tweet_keys)
print(tweet.values())
print(tweet.items())

print("user" in tweet)



word_cnt ={}


document = ["abc","abc","abc","abc","a","b"]

for word in document:
    if word in word_cnt:
        word_cnt[word]+=1
    else:     
        word_cnt[word]=1
        
print(word_cnt)        

word_cnt={}
for word in document:
    try:
        word_cnt[word]+=1
    except KeyError:
        word_cnt[word]=1
        
print(word_cnt)            


from collections import defaultdict

word_cnt = defaultdict(int)
for word in document:
    word_cnt[word]+=1
    
    
dd_list = defaultdict(list)
dd_list[2].append(1)
print(dd_list)

dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Seattle"
print(dd_dict)


dd_pair = defaultdict(lambda: [0,0])
print(dd_pair)    

dd_pair[2][1]=1
print(dd_pair) 



from collections import Counter
c = Counter([0,1,2,0]) 
print(c)  

word_cnt = Counter(document)
print(word_cnt)

for word, cnt in word_cnt.most_common(10):
    print(word, cnt)
    
    
primes_set = {2,3,5,7}
    
s = set()
s.add(1)
s.add(3)


item_list = [1,2,3,3,2,1]
print(len(item_list))

item_set=set(item_list)
print(item_set)
print(len(item_set))



if 1>2 :
    message = "if only 1 were greater than two..."
elif 1>3:
    message = "elif stands for"
else:
    message = "gg"
    
parity = "even" if x%2 == 0 else "odd"

            
for x in range(10):
    print(f"{x} is less than 10")
    
    
x=None
def As(x):
    #assert x==False, "this is the not the Pythonic way to check for None"
    assert x is False, "This it the Pythonic way to check for None" 
    
#As(x) 

d={}
As(bool([]))



s = ""
if s:
    first_char=s[0]
else:
    first_char = ""

print(first_char)    

s = "abd"
first_char = s and s[0]
print(first_char)    

x = True
safe_x = x or False
print(safe_x)    

print("--------")
res = all([True, 1,{2}])
print(res)
res = all([True, 1,{}])
print(res)
res = any([])
print(res)

    
        
x = [4,3,2,1]

y=sorted(x)
print(y)
x.sort()
print(x)    
x.sort(reverse=True)
print(x)    
      
wc = sorted(word_cnt.items(),
            key = lambda word_and_cnt: word_and_cnt[0],
            reverse=True)
print(wc)


even_numbers = [x for x in range(5) if x%2==0]
squares = [x*x for x in range(5)]
even_squares = [x*x for x in range(5) if x%2==0]


print(even_numbers)
print(squares)
print(even_squares)

square_dict = {x: x*x for x in range(5)}
print(square_dict)

zeros = [0 for _ in squares] #len만큼 
print(zeros)

pairs = [(x,y)
         for x in range(3)
         for y in range(3)]
print(pairs)


class CountingClicker:
    def __init__(self, count=0):
        self.count=count
    def __repr__(self):
        return f"CountingClicker(count={self.count})"
    
    def click(self, num_times = 1):
        self.count+=num_times
    def read(self):
        return self.count
    def reset(self):
        self.count=0
           
    
    
clicker = CountingClicker()

assert clicker.read()==0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read()==2, "clicker should start with count 2"
clicker.reset()
assert clicker.read()==0, "clicker should start with count 0"

class NoResetClicker(CountingClicker):
    def reset(self):
        pass
    
clicker2 = NoResetClicker()

assert clicker2.read()==0, "clicker should start with count 0"
clicker2.click()
assert clicker2.read()==1, "clicker should start with count 1"
clicker2.reset()
#assert clicker2.read()==0, "reset shouldn't do anything"


print("-----------")

def generate_range(n):
    i=0
    while i<n:
        yield i #yield가 호출될 때마다 제너레이터레 해당 값을 생성
        i +=1
        
def natural_numbers():
    n=1
    while True:
        yield n
        n+=1
        
for i in generate_range(10):
    print(f"i: {i}")

#for i in natural_numbers():
#    print(f"i: {i}")

even = (i for i in generate_range(20) if i % 2 ==0)

        
for i in even:
    print(f"i: {i}")

print("++++++++++++++")
data = natural_numbers()
evens = (x for x in data if x%2==0)
even_squares = (x**2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x%10==6)


names = ["Alice","Bo","Ch","De"] 

for i, name in enumerate(names):
    print(f"name {i} is {name}")       


import random

random.seed(10)

four_uniform_randoms =[random.random() for _ in range(4)]

print(four_uniform_randoms)


print("============")
four_uniform_randoms =[random.randrange(1,3) for _ in range(4)]

print(four_uniform_randoms)


up_to_ten = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(up_to_ten)
print(up_to_ten)


my_best_f = random.choice(names)
print(my_best_f)


lottery_num = range(60)

print(lottery_num)

winning_num = random.sample(lottery_num,6)
print(winning_num)
four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)


import re

re_examples = [
    not re.match("a","cat"),
    re.search("a","cat"),
    not re.search("c","dog"),
    3==len(re.split("[abs]","carbs")),
    "R-D-" == re.sub("[0-9]","-","R2D2")
]

print(re.split("[abs]","carbs"))
#assert all(re_examples), "all the regex examples should be True"


list1 = ['a','b','c']
list2 = [1,2,3,4,5]

pairs = [pair for pair in zip(list1, list2)]

letters, numbers = zip(*pairs)
print(letters, numbers)




def add(a,b): return a+b

add(1,2)

try:
    add([1,2])
except TypeError:
    print("ds")
    
print(add(*[1,2]))

print("*********")

def doubler(f):
    def g(x):
        return 2*f(x)
    return g

def f1(x):
    return x+1

g=doubler(f1)

print(g(2))


def f2(x,y):
    return x+y

def doubler1(f):
    def g(x,y):
        return 2*f(x,y)
    return g

g=doubler1(f2)
try:
    print(g(3,2))
except TypeError:
    print("nono")   
    
    
def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:",kwargs)
     
magic(1,2,3,key="word",key2="word2",key3="dsa")       

def other_way_magic(x,y,z):
    print("z here")
    print(z)
    return x+y+z

x_y_list = [1,2]
z_dict = {"z":3}
print("here")
print(other_way_magic(*x_y_list, **z_dict))

print("**z_dict")


print("++++++++++++")
"""def doubler_correct(f):
    def g(*args, **kwargs):
        return 2*f(*args, **kwargs)
    return g
""" 

"""
def doubler_correct(f):
    def g(x,y,z):
        return 2*f(x,y,z)
    return g

def f3(x,y,z):
    print("here f3")
    print(x)
    print(y)
    print(z)
    return x+y+z
    
g = doubler_correct(f3)

print(g(*[1,2],**z_dict))
"""
"""
def doubler_correct(f):
    def g(*args, **kwargs):
        return 2*f(*args,**kwargs)
    return g

def f3(x,y):
    print("here f3")
    print(x)
    print(y)
    return x+y
    
g = doubler_correct(f3)

#print(g(*[1,2])#,**z_dict))

def magic1(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)
    
magic1(1,2,key="word")

print("other way magic")

print("before")


def other_way_magic1(x,y,z):
    print("z here")
    print(z)
    return x+y+z

x_y_list = [1,2]
z_dict = {"z":3}
print(other_way_magic1(*x_y_list, **z_dict))

"""
"""
print("after")

def doubler_correct1(f):
    def g1(*args, **kwargs):
        return 2*f(*args, **kwargs)
    return g1

def f4(x,y,z):
    return x+y+z

g1 = doubler_correct1(f4)

print(g(*[1,2],**{"z":3}))

"""

print("--------------")


def add(a,b):
    return a+b

add(10,5)==15
add([1,2],[3])==[1,2,3]
add("hi ","there") == "hi there"

try: 
    add(10, "five")
except TypeError:
    print("cannot add an int to a string")
    

def add(a: int , b: int ) -> int:
    return a+b

print(add(10,5))
print(add("hi", "there"))


def avg(a,b):
    return (a+b)/2

print(avg(1,2))

def total(xs: list) -> float:
    return sum(total)

from typing import List

def total(xs: List[float]) -> float:
    return sum(xs)

print(total([1,2,3,4]))


x: int =5

from typing import Optional

values: List[int] = []
best_so_far: Optional[float] = None

from typing import Dict, Iterable, Tuple

counts: Dict[str, int] = {'data':1, 'science':2}

lazy=0

if lazy:
    evens: Iterable[int] = (x for x in range(10) if x % 2 == 0)
    
else:
    evens = [0,2,4,6,8]
    
tuple: Tuple[int, float, int] = (10, 2.3, 5)    

    
from typing import Callable

def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s,2)

def comma_repeater(s: str, n: int)-> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

assert twice(comma_repeater, "type hints") == "type hints, type hints"   


Number = int
Numbers = List[Number]

def total(xs: Numbers) -> Number:
    return sum(xs)






