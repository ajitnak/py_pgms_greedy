def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

#ps = powerset(['a', 'b', 'c', 'd'])
ps = powerset(['a'])
print "size of power set {}".format(len(ps))
print "power set {}".format(ps)
