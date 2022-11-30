"""
CME
---

Starts the NGAC cme server.
"""

from exec_runner import ExecRunner


class CME(ExecRunner):
    def __init__(self, path="./cme", args="") -> None:
        """
        Initialize the CME class.
        """
        self.path = path
        self.args = args
        super().__init__(path, args)


def test_cme():
    cme = CME()
    cme.start()
    # Try to connect to the CME
    import subprocess
    import time

    time.sleep(1)
    cme.stop()
