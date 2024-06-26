# Copyright 2024 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This file stores input parameters for the app."""

THUMBNAIL = "assets/dwave_logo.svg"

# Sets Dash debug. Set to True if developing and False if
# demoing. App should be restarted to see change.
DEBUG = False

APP_TITLE = "Employee Scheduling Demo"
MAIN_HEADER = "Employee Scheduling"
DESCRIPTION = """\
Employee scheduling is a common industry problem that often becomes complex
due to real-world constraints. This example demonstrates a scheduling
scenario with a variety of employees and rules.
"""


#######################################
# Sliders, buttons and option entries #
#######################################
# which month to use for employee scheduling (0 uses current month)
MONTH = 0

# min/max number of shifts per employee range slider (value means default)
MIN_MAX_SHIFTS = {
    "min": 1,
    "max": 31,
    "step": 1,
    "value": [10, 20],
}

# min/max number of employees per shift range slider (value means default)
MIN_MAX_EMPLOYEES = {
    "min": 1,
    "max": 100,
    "step": 1,
    "value": [3, 6],
}

# number of employees slider (value means default)
NUM_EMPLOYEES = {
    "min": 4,
    "max": 80,
    "step": 1,
    "value": 12,
}

# max consecutive shifts slider (value means default)
MAX_CONSECUTIVE_SHIFTS = {
    "min": 1,
    "max": 80,
    "step": 1,
    "value": 5,
}

# default scenarios (don't change order of items)
SMALL_SCENARIO = {
    "num_employees": 12,
    "consecutive_shifts": 5,
    "shifts_per_employee": [10, 20],
    "employees_per_shift": [3, 6],
    "random_seed": "",
}

MEDIUM_SCENARIO = {
    "num_employees": 20,
    "consecutive_shifts": 5,
    "shifts_per_employee": [8, 16],
    "employees_per_shift": [6, 10],
    "random_seed": "",
}

LARGE_SCENARIO = {
    "num_employees": 40,
    "consecutive_shifts": 5,
    "shifts_per_employee": [4, 16],
    "employees_per_shift": [6, 10],
    "random_seed": "",
}
