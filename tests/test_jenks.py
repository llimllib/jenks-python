from jenks import jenks

def eq(got, want, msg=''):
    if not want == got:
        raise AssertionError("expected %s but got %s\n%s" % (want, got, msg))

def test_jenks():
    eq(jenks([1,2,3],2),       [[1], [2,3]])
    eq(jenks([1,2,9,10,11],2), [[1,2], [9,10,11]])
    eq(jenks([1,2,3,10,11],2), [[1,2,3], [10,11]])

#write a long-running test? Maybe make a quicker, but still non-trivial, test
#def test_long_jenks
#    pp(jenks(json.load(open('test.json')), 5))
