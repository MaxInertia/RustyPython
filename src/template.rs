#[repr(C)]
#[derive(Debug)]
pub struct Apple {
    pub f: f32,
    pub i: i32,
    //pub u_num: u32, // Broken?
}

// TODO: To what degree, if any, can Traits be used across the ffi?
// TODO: PySync Trait?

/*#[no_mangle] // returns the size of the struct in bytes
pub extern "C" fn sizeof_apple() -> i32 {
    size_of::<apple>();
}*/

#[no_mangle]
pub extern "C" fn new_apple() -> *mut Apple {
    let r = Box::new(Apple { f: 2.89, i: -13});
    println!("Rust: Allocating {} bytes for apple instance", std::mem::size_of::<Apple>());
    let raw = Box::into_raw(r);
    raw
}

#[no_mangle]
pub extern "C" fn free_apple(ptr: *mut Apple) {
    if ptr.is_null() {
        return;
    }
    unsafe {
        Box::from_raw(ptr);
    }
}

// Getters and Setters

#[no_mangle]
pub extern "C" fn get_f(ptr: &Apple) -> f32 {
    ptr.f
}

#[no_mangle]
pub extern "C" fn set_f(ptr: &mut Apple, value: f32) {
    ptr.f = value
}

#[no_mangle]
pub extern "C" fn get_i(ptr: &Apple) -> i32 {
    ptr.i
}

#[no_mangle]
pub extern "C" fn set_i(ptr: &mut Apple, value: i32) {
    ptr.i = value
}

// Other

#[no_mangle]
pub extern "C" fn display(ptr: &Apple) {
    println!("Rust: {:?}", ptr)
}

// Broken?

/*
#[no_mangle]
pub extern "C" fn get_uint(ptr: &mut Apple) -> u32 {
    ptr.u
}

#[no_mangle]
pub extern "C" fn set_uint(ptr: &mut Apple, value: u32) {
    ptr.u = value
}*/
