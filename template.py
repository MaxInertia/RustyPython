from cffi import FFI

# The C-equivalent of the Rust struct and function types.
header_apple = """
    typedef struct {
        float       f;
        int         i;
    } apple;

    apple new_apple();
    void free_apple(apple);

    void display(apple);

    void set_f(apple, float);
    float get_f(apple);

    void set_i(apple, int);
    int get_i(apple);
"""

class RustLib():
    def __init__(self, lib_in, headers_in):
        self.ffi = FFI()
        self.lib = self.ffi.dlopen(lib_in)
        self.ffi.cdef(headers_in)

    # Access function from lib, ex: _.fn().somefunction()
    def fn(self):
        return self.lib

    # Rust structures exposed by the library

    # For when initialization code is defined in Rust
    def build_apple(self):
        ptr = self.lib.new_apple()
        return Apple(lib_in = self.lib, ptr_in = ptr)

    # For when initialization code is defined in Python
    def new_apple(self):
        ptr = self.ffi.new("apple *")
        assert(ptr != self.ffi.NULL)
        return Apple(lib_in = self.lib, ptr_in = ptr)

    # additional structs here...

'''Example Rust Struct Wrapper'''
class Apple():
    def __init__(self, lib_in, ptr_in):
        self.ptr = ptr_in  # Store pointer being wrapped and
        self._lib = lib_in # library for access to functions

    def display(self):
        self._lib.display(self.ptr)

    def free(self):
        self._lib.free(self.ptr)

    # Convenience methods for accessing rust functions
    def get_float(self):
        return self._lib.get_f(self.ptr)

    def set_float(self, v):
        self._lib.set_f(self.ptr, v)

    def get_int(self):
        return self._lib.get_i(self.ptr)

    def set_int(self, v):
        self._lib.set_i(self.ptr, v)

#   ============
#   Load Library
#   ============

# Path to the library file:
#   Windows: *.dll
#   Linux: *.so
win_lib = "target/debug/rusty_python.dll"
#headers = header_apple # add additional headers here...
rust = RustLib(lib_in = win_lib, headers_in = header_apple)

#   =================
#   Application Logic
#   =================

# To identify which language a print
# statement was written at runtime
def printPy(msg):
    print("Python: " + msg)

def unwrapped():
    sa = rust.fn().new_apple()
    printPy("ptr = " + str(sa))

    # Check initial value
    f = rust.fn().get_f(sa)
    printPy("ptr.f = (" + str(f) +") <- initial value")
    # Change, confirm it changed
    rust.fn().set_f(sa, 0.25)
    f = rust.fn().get_f(sa)
    assert(f == 0.25)
    printPy("ptr.f = (" + str(f) + ") <- should be 0.25")

    # Check initial value
    i = rust.fn().get_i(sa)
    printPy("ptr.i = (" + str(i) +") <- initial value")
    # Change, confirm it changed
    rust.fn().set_i(sa, 9)
    i = rust.fn().get_i(sa)
    assert(i == 9)
    printPy("ptr.i = (" + str(i) + ") <- should be 9")

    rust.fn().display(sa)

def wrapped():
    sa = rust.build_apple();
    #sa = rust.new_apple();
    printPy("sa = " + str(sa))
    printPy("sa.ptr = " + str(sa.ptr))

    f = sa.get_float()
    printPy("sa.f = " + str(f) + " <- initial value")
    sa.set_float(0.25)
    f = sa.get_float()
    printPy("sa.f = " + str(f) + " <- should be 0.25")
    assert(f == 0.25)

    i = sa.get_int()
    printPy("sa.i = " + str(i) + " <- initial value")
    sa.set_int(9)
    i = sa.get_int()
    printPy("sa.i = " + str(i) + " <- should be 9")
    assert(i == 9)

    sa.display()

print("\nUN-WRAPPED:")
unwrapped()

print("\nWRAPPED:")
wrapped()
