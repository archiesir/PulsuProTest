from tests.tests import test_root
from tests.tests import test_add
from tests.tests import test_subtract
from tests.tests import test_multiply
from tests.tests import test_division
from tests.tests import test_division_by_zero

if __name__ == '__main__':
    print('Start testing...')
    test_root()
    test_add()
    test_subtract()
    test_multiply()
    test_division()
    test_division_by_zero()
    print('Testing has been done.')
