Changelog
=========

## 0.2.0

Test split granularity can now be controlled by setting _distributed_can_split_
at the class or module level. Simply specify `_distributed_can_split = False` on
a module or on a class, and tests contained therein will be forced to run on the
same node.

## 0.1.2

Test selection for Class-based tests no longer groups all methods from the same
class to the same test node. Hashing by module + method name will on average
give a better distribution. For (naughty) folks who tend to make a few huge
TestCase classes, this might make a fairly large difference.
