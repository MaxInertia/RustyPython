#[derive(Debug)]
#[repr(C)]
pub struct PySync {
    d: f64,
    f: f32,
    i: i32,
    u: u32,
}

// TODO: other primitive types
// TODO: nested structures

#[no_mangle]
pub extern "C"
fn new_PySync() -> *mut PySync {
    let r = Box::new(PySync { d: 287.325, f: 287.325, i: -13, u: 42});
    println!("Rust: Allocating {} bytes for PySync instance", std::mem::size_of::<PySync>());
    let raw = Box::into_raw(r);
    raw
}

#[no_mangle]
pub extern "C"
fn free_PySync(ptr: *mut PySync) {
    if ptr.is_null() {
        return;
    }
    unsafe {
        Box::from_raw(ptr);
    }
}

#[no_mangle]
pub extern "C"
fn display(ptr: &PySync) {
    println!("Rust: {:?}", ptr)
}

// Getters and Setters
// Rust type - C type

// f32 - float

#[no_mangle]
pub extern "C"
fn get_f(ptr: &PySync) -> f32 {
    ptr.f
}

#[no_mangle]
pub extern "C"
fn set_f(ptr: &mut PySync, value: f32) {
    ptr.f = value
}

// f64 - double

#[no_mangle]
pub extern "C"
fn get_d(ptr: &PySync) -> f64 {
    ptr.d
}

#[no_mangle]
pub extern "C"
fn set_d(ptr: &mut PySync, value: f64) {
    ptr.d = value
}

// i32 - int

#[no_mangle]
pub extern "C"
fn get_i(ptr: &PySync) -> i32 {
    ptr.i
}

#[no_mangle]
pub extern "C"
fn set_i(ptr: &mut PySync, value: i32) {
    ptr.i = value
}

// u32 - uint32_t

#[no_mangle]
pub extern "C"
fn get_u(ptr: &mut PySync) -> u32 {
    ptr.u
}

#[no_mangle]
pub extern "C"
fn set_u(ptr: &mut PySync, value: u32) {
    ptr.u = value
}
