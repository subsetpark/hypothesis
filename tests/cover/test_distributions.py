# coding=utf-8

# Copyright (C) 2013-2015 David R. MacIver (david@drmaciver.com)

# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

# END HEADER

from __future__ import division, print_function, absolute_import, \
    unicode_literals

import random

import pytest
import hypothesis.internal.distributions as dist


def test_non_empty_of_empty_errors():
    with pytest.raises(ValueError):
        dist.non_empty_subset(random, [])


def test_non_empty_of_one_always_returns_it():
    assert dist.non_empty_subset(random, [1]) == [1]
    assert dist.non_empty_subset(random, [2]) == [2]


def test_non_empty_of_three():
    assert dist.non_empty_subset(random, [1, 2, 3])


def test_non_empty_of_10():
    assert dist.non_empty_subset(random, range(10))


def test_non_empty_with_explicit_activation_chance():
    assert len(dist.non_empty_subset(
        random, range(100), activation_chance=0.99)) > 2
