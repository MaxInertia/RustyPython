#[repr(C)]
#[derive(Debug)]
pub struct PySync {
    d: f64,
    f: f32,
    i: i32,
    u: u32,
}

/*
It appears that the only combinations of primitive struct fields that work
are those whose sum are 8 bytes.

- f64
- i32 and i32 || i32 and f32 || f32 and f32

This is solved by changing the python header definition of PySync from

    typedef struct {
        float f;
        float f2;
    } PySync;

to

    typedef void* PySync;

which seemingly allows arbitrary fields in the struct
*/

// TODO: To what degree, if any, can Traits be used across the ffi?
// TODO: PySync Trait?

#[no_mangle] pub extern "C"
fn new_PySync() -> *mut PySync {
    let r = Box::new(PySync { d: 287.325, f: 287.325, i: -13, u: 42});
    println!("Rust: Allocating {} bytes for PySync instance", std::mem::size_of::<PySync>());
    let raw = Box::into_raw(r);
    raw
}

#[no_mangle] pub extern "C"
fn free_PySync(ptr: *mut PySync) {
    if ptr.is_null() {
        return;
    }
    unsafe {
        Box::from_raw(ptr);
    }
}

#[no_mangle] pub unsafe extern "C"
fn display(ptr: &PySync) {
    println!("Rust: {:?}", ptr)
}

// Getters and Setters
// Rust type - C type

// f32 - float

#[no_mangle] pub unsafe extern "C"
fn get_f(ptr: &PySync) -> f32 {
    ptr.f
}

#[no_mangle] pub unsafe extern "C"
fn set_f(ptr: &mut PySync, value: f32) {
    /*let v = unsafe {
        assert!(!ptr.is_null());
        &mut *ptr
    };*/
    /*unsafe {
        assert!(!ptr.is_null());
        (*ptr).f = value
    }*/
    ptr.f = value
}

// f64 - double

#[no_mangle] pub unsafe extern "C"
fn get_d(ptr: &PySync) -> f64 {
    ptr.d
}

#[no_mangle] pub unsafe extern "C"
fn set_d(ptr: &mut PySync, value: f64) {
    ptr.d = value
}

// i32 - int

#[no_mangle] pub unsafe extern "C"
fn get_i(ptr: &PySync) -> i32 {
    ptr.i
}

#[no_mangle] pub unsafe extern "C"
fn set_i(ptr: &mut PySync, value: i32) {
    ptr.i = value
}

// u32 - uint32_t

#[no_mangle] pub unsafe extern "C"
fn get_u(ptr: &mut PySync) -> u32 {
    ptr.u
}

#[no_mangle] pub unsafe extern "C"
fn set_u(ptr: &mut PySync, value: u32) {
    ptr.u = value
}
