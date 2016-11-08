class Test:
    def __init__(self, value):
        self.value = value

test_object = Test(4)
test2_object = Test(5)

print "format string is {.value} and {.value}".format(test_object, test2_object)

print "format string is {1.value} and {0.value}".format(test_object, test2_object)



my_dict = {'key1':1, 'key2':2}

print "Format string is {key2} and {key1}".format(**my_dict)

print "Format string is {key2} and {key1}".format(key1 = 1, key2 =2)


# padding and other tricks

# center a string

print "{:^20}".format("mid")

print "{:.^20}".format("mid")


#pad zero to the left of a number

print "{:0>10}".format(123)


#pad zero after the decimal 

print "{:0<10}".format(3.22)

print round(3.221115,4)


print format(3.22, '.6f')
