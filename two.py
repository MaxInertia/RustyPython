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
        typedef struct {
            float width;
            float height;
        } heapy;

        heapy new_heapy();

        void free_heapy(heapy);

        float get_width(heapy);
        float get_height(heapy);

        void set_width(heapy, float);
        void set_height(heapy, float);

        void display(heapy);
    """)

# Alternatively could use an opaque pointer to the struct 'heapy'
# typedef void* heapy;

def display(h):
    print("Python: " + str(h))

h = rust.fn().new_heapy()
#rust_struct_ref.speak()
#ffi.speak(heapy)

print("\nPre-set")
rust.fn().display(h)
display(h)

print("\nPost-set")
rust.fn().set_width(h, 3.0)
rust.fn().set_height(h, 4.0)
rust.fn().display(h)
display(h)

# This hangs and crashes
#print("\nPython.set")
#h.width = 124.0;
#h.height = 42.7;
#print("width: " + str(rust.fn().get_width(h)))
#print("height: " + str(rust.fn().get_height(h)))
rust.fn().free_heapy(h)

print("\nPost-free")
rust.fn().display(h)
display(h)

print("\nAttemping Post-free set")
rust.fn().set_width(h, 13.0)
rust.fn().set_height(h, 7.0)
rust.fn().display(h)
display(h)
