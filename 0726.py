from collections import  Iterable
import  os
import functools

def century():

    print ("Please input a year:")
    year = int(input())
    if year>2000 :
        return ("new century")
    else:
        return ("old century")

# str = century()
# print (str)


def loopfor(flag):
    sum = 0
    for x in list(range(101)):
        sum = sum + x
    return sum


def loopwhile():
    sum = 0
    n = 99
    while n > 0:
        sum = sum +n
        n = n-2
    return sum


# sum = loopwhile()
# print (sum)

# L = ["A", "B", "C"]
# for x in L:
#     print ("hello "+x)

def power(x, n):
    s = 1
    i = 1
    while i <= n:
        i = i + 1
        s = s * x
    return s
# sum = power(5,2)
# print sum

def dictionary():
    dict = {"a": 100, "b": 90, "c": 80}
    for key in dict :
        print dict[key]
    for value in dict.itervalues():
        print value
    for key,value in dict.iteritems():
        print key,'=' ,value

   # print (dict.get("b"))
    #return(dict[x])

# name = raw_input()
# print name
#dictionary()

# s = set([1,2,3])
# s.add(3)
# print s
def iterable():
    s = isinstance("abc",Iterable)
    d = isinstance([1,2,3],Iterable)
    f = isinstance(123,Iterable)
    for i,value in enumerate(['A','B','C']):
        print i,value
# iterable()

# list = [d for d in os.listdir("\\.")]
# print list
def change(l):
    return l.capitalize()
# name = ['adam','LISA','barT']
# print map(change, name)

# def prod(l):
#     return reduce(lambda x,y:x*y,l)
# print  prod(range(1,3))

# def sushu(l):
#     for x in range(2,l):
#         if l%x == 0:
#             return True
#     return False
# print filter(sushu,range(1,101))

def sort_word(s1,s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
# print sorted(['bob','Zaza','a'],sort_word)

# print map(lambda x:x*x,range(1,10))
def bulid(x,y):
    return lambda:x*x+y*y
# print bulid(2,3)()
f = bulid
# print bulid.__name__


def log(args):

    desc = 'Just call!'

    def decoration(func):

        @functools.wraps(func)
        def wrapper(*K, **KM):

            print '[+] Function Execute: ' + func.__name__ + ' (' + desc + ')'
            result = func(*K, **KM)
            print '[+] Function Finished: ' + func.__name__ + ' (' + desc + ')'
            return result
        return wrapper

    if hasattr(args, '__call__'):
        return decoration(args)
    else:
        desc = args
        return decoration


@log
def test():
    print 'Hello decoration!'

# test()


def log_1(func):
    def wrapper(*args,**kw):
        print 'call %s():'%func.__name__
        return func(*args,**kw)
    return wrapper


@log_1
def now_1():
    print("2017-07-31")

# now_1()
# print now_1.__name__


def log_2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print  '%s %s()' %(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator


@log_2('execute')
def now():
    print '2017-07-31'

now()
print now.__name__


def log_3(args):
    text = 'just call!'
    def decroate(func):
        def wrapper(*arg,**kw):
            print 'function excute:'+ func.__name__+'('+text+')'
            result = func(*arg,**kw)
            print 'function finish:'+ func.__name__+'('+text+')'
            return result
        return wrapper
    if hasattr(args,'__call__'):
        return decroate(args)
    else:
        text = args
        return decroate


@log_3
def test_1():
    print 'hello decroate!'

test_1()
