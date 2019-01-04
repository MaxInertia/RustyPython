from cffi import FFI

# The C-equivalent of the Rust function types.
header_PySync = """
    typedef void* PySync;

    PySync new_PySync();
    void free_PySync(PySync);

    void display(PySync);

    void set_d(PySync, double);
    double get_d(PySync);

    void set_f(PySync, float);
    float get_f(PySync);

    void set_i(PySync, int);
    int get_i(PySync);

    void set_u(PySync, uint32_t);
    uint32_t get_u(PySync);
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
    def build_PySync(self):
        ptr = self.lib.new_PySync()
        return PySync(lib_in = self.lib, ptr_in = ptr)

    # For when initialization code is defined in Python
    # NOT WORKING. See description in function: wrapped
    #def new_PySync(self):
    #    ptr = self.ffi.new("PySync")
    #    assert(ptr != self.ffi.NULL)
    #    return PySync(lib_in = self.lib, ptr_in = ptr)

'''Example Rust Struct Wrapper'''
class PySync():
    def __init__(self, lib_in, ptr_in):
        self.ptr = ptr_in  # Store pointer being wrapped and
        self._lib = lib_in # library for access to functions

    def display(self):
        self._lib.display(self.ptr)

    def free(self):
        self._lib.free(self.ptr)

    # Convenience methods for accessing rust functions

    def get_d(self):
        return self._lib.get_d(self.ptr)

    def set_d(self, v):
        self._lib.set_d(self.ptr, v)

    def get_f(self):
        return self._lib.get_f(self.ptr)

    def set_f(self, v):
        self._lib.set_f(self.ptr, v)

    def get_i(self):
        return self._lib.get_i(self.ptr)

    def set_i(self, v):
        self._lib.set_i(self.ptr, v)

    def get_u(self):
        return self._lib.get_u(self.ptr)

    def set_u(self, v):
        self._lib.set_u(self.ptr, v)

#   ============
#   Load Library
#   ============

# Path to the library file:
#   Windows: *.dll
#   Linux: *.so
win_lib = "target/debug/rusty_python.dll"
#headers = header_PySync # add additional headers here...
rust = RustLib(lib_in = win_lib, headers_in = header_PySync)

#   =================
#   Application Logic
#   =================

# To identify which language a print
# statement was written at runtime
def printPy(msg):
    print("Py: " + msg)

def unwrapped():
    sa = rust.fn().new_PySync()
    printPy("ptr = " + str(sa))

    def test_set_and_get(getter, setter, field, num):
        setter(sa, num)
        x = getter(sa)
        printPy("ptr." + field + " = (" + str(x) + ") <- should be " + str(num))
        assert(x == num)

    test_set_and_get(rust.fn().get_d, rust.fn().set_d, "f2", 3.25)
    test_set_and_get(rust.fn().get_f, rust.fn().set_f, "f", 3.25)
    test_set_and_get(rust.fn().get_i, rust.fn().set_i, "i", -9)
    test_set_and_get(rust.fn().get_u, rust.fn().set_u, "u", 13)

    rust.fn().display(sa)

def wrapped():
    sa = rust.build_PySync();

    #sa = rust.new_PySync();
    # ^ This fails when using `typedef void* PySync` due to unknown ctype size
    #   and fails when using explicit struct layout in both of the following:
    #       1. ffi.new("PySync") due to
    #           "TypeError: expected a pointer or array ctype, got 'PySync'"
    #       2. ffi.new("PySync *") due to
    #           "TypeError: initializer for ctype 'PySync' must be a list or
    #            tuple or dict or struct-cdata, not cdata 'PySync *'"

    printPy("sa = " + str(sa))
    printPy("sa.ptr = " + str(sa.ptr))

    def test_set_and_get(getter, setter, field, num):
        setter(num)
        x = getter()
        printPy("ptr." + field + " = (" + str(x) + ") <- should be " + str(num))
        assert(x == num)

    test_set_and_get(sa.get_d, sa.set_d, "d", 3.25)
    test_set_and_get(sa.get_f, sa.set_f, "f", 3.25)
    test_set_and_get(sa.get_i, sa.set_i, "i", -9)
    test_set_and_get(sa.get_u, sa.set_u, "u", 13)

    sa.display()

print("\nWRAPPED:")
wrapped()

print("\nUN-WRAPPED:")
unwrapped()
