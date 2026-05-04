#!/usr/bin/env python3
"""Quick test runner to verify implementation."""

import sys
import unittest

# Run tests
loader = unittest.TestLoader()
suite = loader.discover('tests', pattern='test_*.py')
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Exit with appropriate code
sys.exit(0 if result.wasSuccessful() else 1)
