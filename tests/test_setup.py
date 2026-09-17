"""The template's one green test. It checks that the numerical libraries import and agree with each other.

Keep this file. Add your own tests in new files: tests/test_solow.py for M0, tests/test_household.py for M1.
"""
import numpy as np
import scipy.linalg


def test_environment_works():
    A = np.array([[2.0, 1.0], [1.0, 3.0]])
    b = np.array([3.0, 5.0])
    x = scipy.linalg.solve(A, b)
    assert np.allclose(A @ x, b)
