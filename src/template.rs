#[repr(C)]
#[derive(Debug)]
pub struct Apple {
    pub f_num: f32,
    pub i_num: i32,
    //pub u_num: u32,
}

// TODO: To what degree, if any, can Traits be used across the ffi?
// TODO: PySync Trait?

#[no_mangle]
pub extern "C" fn new_apple() -> *mut Apple {
    let r = Box::new(Apple { f_num: 2.89, i_num: -13});
    println!("Rust: Allocating {} bytes for Apple instance", std::mem::size_of::<Apple>());
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

/*fn fix_ptr<'a>(ptr: *const Apple) -> &'a Apple {
    unsafe {
        assert!(!ptr.is_null());
        &*ptr
    }
}*/

#[no_mangle]
pub extern "C" fn get_f(ptr: &Apple) -> f32 {
    //println!("Rust::get_float::<Apple> = {:?}", ptr);
    //println!("Rust::get_float() = {}", ptr.f_num);
    ptr.f_num
}

/*#[no_mangle]
pub extern "C" fn get_int(ptr: &mut Apple) -> i32 {
    ptr.i
}

#[no_mangle]
pub extern "C" fn get_uint(ptr: &mut Apple) -> u32 {
    ptr.u
}*/

#[no_mangle]
pub extern "C" fn set_f(ptr: &mut Apple, value: f32) {
    ptr.f_num = value
}

//println!("POST: Rust::get_float::<Apple> = {:?}", ptr);
//println!("PRE: Rust::get_float::<Apple> = {:?}", ptr);

/*#[no_mangle]
pub extern "C" fn set_int(ptr: &mut Apple, value: i32) {
    ptr.i = value
}

#[no_mangle]
pub extern "C" fn set_uint(ptr: &mut Apple, value: u32) {
    ptr.u = value
}*/

// Other

/*
#[no_mangle]
pub extern "C" fn display(ptr: *const Apple) {
    let v = unsafe {
        assert!(!ptr.is_null());
        &*ptr
    };
    println!("Rust: {:?}", v)
}
*/
