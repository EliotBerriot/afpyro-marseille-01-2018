import afpyro
import os
import unittest
import tempfile


class TestLog(unittest.TestCase):
    def setUp(self):
        _, self.program_file = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.program_file)

    def test_write_afpyro_program(self):
        event = 'Introduction to pytest'
        afpyro.write_program(
            event,
            self.program_file)
        with open(self.program_file) as f:
            self.assertEqual(f.read(), event)
