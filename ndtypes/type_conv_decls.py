import numpy as np
import types 

import scalar_types 
import type_conv

from array_type import make_array_type, ArrayT
from tuple_type import make_tuple_type, TupleT 
from core_types import NoneT, NoneType, TypeValueT

type_conv.register(type(None), NoneT, lambda _: NoneType)

def typeof_dtype(dt):
  return TypeValueT(scalar_types.from_dtype(dt))
type_conv.register([np.dtype], TypeValueT, typeof_dtype) 

def typeof_type(t):
  assert hasattr(t, 'dtype'), "Can only convert numpy types"
  dt = t(0).dtype 
  pt = scalar_types.from_dtype(dt)
  return TypeValueT(pt) 
type_conv.register(types.TypeType, TypeValueT, typeof_type)

def typeof_tuple(python_tuple):
  return make_tuple_type(map(type_conv.typeof, python_tuple))

type_conv.register(types.TupleType, TupleT, typeof_tuple)

def typeof_array(x):
  x = np.asarray(x)
  elt_t = scalar_types.from_dtype(x.dtype)
  rank = len(x.shape)
  return make_array_type(elt_t, rank)

type_conv.register(np.ndarray, ArrayT, typeof_array)
