ndtypes
========

Types for array-oriented domain-specific languages embedded in Python. Includes n-dimensional arrays, their scalar elements, and for index expressions: tuples, slices, and None. 

Factored out of Parakeet, excluding function and closure types. 

```
    ScalarType = int8 ... int64 | uint8 ... uint64 | float32 | float64 | bool
    ArrayType = Array(ScalarType, rank), where rank is an integer >= 1
    Type = ScalarType | ArrayType | Tuple(Type+) | Slice | None 
```
