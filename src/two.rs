#[repr(C)]
#[derive(Debug)]
pub struct Heapy {
    //arr: [i32; 10]
    pub width: f32,
    pub height: f32,
}

//impl PySync for heapy {
#[no_mangle]
pub extern "C" fn new_heapy() -> *mut Heapy {
    let r = Box::new(Heapy { width: 13.5, height: 44.2 }); //arr: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] });
    let raw = Box::into_raw(r);
    println!("\nRust: size_of<Heapy> = {} bytes", std::mem::size_of::<Heapy>());
    println!("Rust: size_of_val(return) = {} bytes", std::mem::size_of_val(&raw));
    raw
}
//}

//trait PySync {
//#[no_mangle]
//extern "C" fn make() -> Self;

#[no_mangle]
pub extern "C" fn free_heapy(ptr: *mut Heapy) {
    if ptr.is_null() {
        return;
    }
    unsafe {
        Box::from_raw(ptr);
    }
}

#[no_mangle]
pub extern "C" fn display(ptr: &Heapy) {
    println!("Rust: {:?}", ptr)
}

#[no_mangle]
pub extern "C" fn get_width(h: &Heapy) -> f32 {
    h.width
}

#[no_mangle]
pub extern "C" fn get_height(h: &Heapy) -> f32 {
    h.height
}

#[no_mangle]
pub extern "C" fn set_width(h: &mut Heapy, value: f32) {
    h.width = value
}

#[no_mangle]
pub extern "C" fn set_height(h: &mut Heapy, value: f32) {
    h.height = value
}
