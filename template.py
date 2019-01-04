from cffi import FFI

# The C-equivalent of the Rust struct and function types.
header_apple = """
    typedef struct {
        float       f_num;
        int         i_num;
    } apple;

    apple new_apple();
    void free_apple(apple);

    void set_f(apple, float);
    float get_f(apple);
"""

class RustLib():
    def __init__(self, lib_in, headers_in):
        self.ffi = FFI()
        self.lib = self.ffi.dlopen(lib_in)
        self.ffi.cdef(headers_in)
    def fn(self):
        return self.lib

    # Rust structures exposed by the library
    #def build_apple(self):
    #    ptr = self.ffi.new("apple *")#self.lib.new_apple()
    #    print("ptr = " + str(ptr))
    #    sa = apple(self.lib, ptr)
    #     return sa

    # additional structs here...

#   ============
#   Load Library
#   ============

# Path to the library file:
#   Windows: *.dll
#   Linux: *.so
win_lib = "target/debug/rusty_python.dll"
#headers = header_apple # add additional headers here...
rust = RustLib(win_lib, header_apple)

#   =================
#   Application Logic
#   =================

sa = rust.fn().new_apple()
print("new_apple() = " + str(sa))

# Check initial value
f = rust.fn().get_f(sa)
print("sa.float = (" + str(f) +") <- initial value")
# Change, confirm it changed
rust.fn().set_f(sa, 8)
f = rust.fn().get_f(sa)
print("sa.float = (" + str(f) + ") <- should be 5.1")


#sa = rust_lib.build_apple();
#print("sa = " + str(sa.ptr))
#sa.display()

#sa.set_float(6.66)
#f = sa.get_float()
#print("sa.float = " + str(f))

#sa.set_float(6.66)
#i = sa.get_int()
#print("sa.int = " + str(i))

#sa.set_float(6.66)
#u = sa.get_uint()
#print("sa.uint = " + str(u))
