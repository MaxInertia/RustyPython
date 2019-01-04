from cffi import FFI

class RustLib():
    def __init__(self, lib_dll, headers):
        self.ffi = FFI()
        self.lib = self.ffi.dlopen(lib_dll)
        self.ffi.cdef(headers)
    def fn(self):
        return self.lib

# Rust Library
rust = RustLib(
    "target/debug/rusty_python.dll",
    """
        int doubled(int);

        typedef struct {
            double x, y, z;
        } vector_t;

        double length(const vector_t *vec);
    """)

# Testing `double length(const vector_t *vec)`
vector = rust.ffi.new("vector_t *")
vector.x = 3.0
vector.y = 4.0
vector.z = 0
print("Vector length = " + str(rust.fn().length(vector)))

# Testing `int doubled(int)`
# Input to our function
input = 9
# Call rust function
#print("rust.fn().doubled(" + str(input) + ") = " + str(rust.fn().doubled(input)))
# Assign rust function to more convenient name (aliasing)
double = rust.fn().doubled
# Call function via alias
#print("double(" + str(input) + ") = " + str(double(input)))
