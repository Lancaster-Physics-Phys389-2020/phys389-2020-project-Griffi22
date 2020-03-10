import numpy as np
import math
import copy
import scipy.constants
from Fields import fields
from Field_effect import Field_effect
import timeit

class field_derivitives(Field_effect):
    def E_field_dt1(self):
        i=self.E_plate_index
        