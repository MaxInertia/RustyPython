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
        typedef void* heapy;

        heapy new_heapy();

        void free_heapy(heapy);

        float get_width(heapy);
        float get_height(heapy);

        void set_width(heapy, float);
        void set_height(heapy, float);
    """)

#  typedef struct {
#      float width;
#      float height;
#  } heapy_t;


print("ffi: " + str(rust.ffi))

h = rust.fn().new_heapy()
#rust_struct_ref.speak()
#ffi.speak(heapy)

print("\nPre-Set")
print("heapy: " + str(h))
print("width: " + str(rust.fn().get_width(h)))
print("height: " + str(rust.fn().get_height(h)))

print("\nPost-Set")
rust.fn().set_width(h, 3.0)
rust.fn().set_height(h, 4.0)
print("heapy: " + str(h))
print("width: " + str(rust.fn().get_width(h)))
print("height: " + str(rust.fn().get_height(h)))

rust.fn().free_heapy(h)

print("\nPost-Free")
print("heapy: " + str(h))
print("width: " + str(rust.fn().get_width(h)))
print("height: " + str(rust.fn().get_height(h)))

print("\nAttemping Set")
rust.fn().set_width(h, 13.0)
rust.fn().set_height(h, 7.0)
print("heapy: " + str(h))
print("width: " + str(rust.fn().get_width(h)))
print("height: " + str(rust.fn().get_height(h)))
