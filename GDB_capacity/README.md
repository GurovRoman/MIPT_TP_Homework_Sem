Запустим код, где v - объект типа vector<int>, в gdb.

```
(gdb) p v
$1 = {<std::_Vector_base<int, std::allocator<int> >> = {_M_impl = {<std::allocator<int>> = {<__gnu_cxx::new_allocator<int>> = {<No data fields>}, <No data fields>}, _M_start = 0x366e40, _M_finish = 0x366e50, _M_end_of_storage = 0x366e50}}, <No data fields>}
(gdb) x/4 &v
0x28fef8:       0x00366e40      0x00366e50      0x00366e50      0xb4749876
```

Оффсеты получаются 0, 1 и 2 соответственно.