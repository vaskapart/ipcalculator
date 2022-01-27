import pytest
from ipcalc import ipcalculator


def test_24():
    assert(ipcalculator('192.168.1.5/24')==('192.168.1.0', '255.255.255.0', '0.0.0.255', '192.168.1.255', '192.168.1.1', '192.168.1.254'))

if __name__ == '__main__':
    pytest.main()

