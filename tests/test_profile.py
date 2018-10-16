import contextlib
import logging
import os
import shutil
import tempfile
import unittest

from dprofiler import profile


class TestProfile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        temp_dir = tempfile.mkdtemp(prefix='dprofile_test_')
        cls._dir = temp_dir

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls._dir):
            shutil.rmtree(cls._dir)

    def test_profile(self):
        @profile
        def fn():
            pass

        fn()

    @contextlib.contextmanager
    def _get_file_logger(self, path):
        logger = logging.getLogger('TestProfile')
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(path)
        logger.addHandler(fh)

        try:
            yield logger
        finally:
            logger.removeHandler(fh)

    def test_profile_own_logger(self):
        path = os.path.join(self._dir, 'test_profile_own_logger.log')
        prefix = 'start'
        suffix = 'end'

        with self._get_file_logger(path) as logger:
            @profile(
                sort_key='pcalls', prefix=prefix, suffix=suffix, n=2,
                logger=logger)
            def fn():
                pass

            fn()

        with open(path, mode='r') as f:
            out = f.read()
        assert out.startswith(prefix)
        assert 'Ordered by: primitive call count' in out
        assert out.rstrip().endswith(suffix)
