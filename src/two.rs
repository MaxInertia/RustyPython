#[repr(C)]
pub struct Heapy {
    //arr: [i32; 10]
    width: f64,
    height: f64,
}

//impl PySync for heapy {
#[no_mangle]
pub extern "C" fn new_heapy() -> *mut Heapy {
    let r = Box::new(Heapy { width: 13.5, height: 44.2 }); //arr: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] });
    Box::into_raw(r)
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
        let _b = Box::from_raw(ptr);
    }
}
//}

/*impl heapy {
    #[no_mangle]
    pub extern "C" fn speak(&self) {
        println!("heapy: \"Hello from Rust!\"")
    }
}*/

/*#[no_mangle]
pub extern "C" fn speak(h: &Heapy) {
    println!("Heapy: \"Hello from Rust!\" w: {}, h: {}", h.width, h.height)
}*/

#[no_mangle]
pub extern "C" fn get_width(h: &Heapy) -> f64 {
    h.width
}

#[no_mangle]
pub extern "C" fn get_height(h: &Heapy) -> f64 {
    h.height
}

#[no_mangle]
pub extern "C" fn set_width(h: &mut Heapy, value: f64) {
    h.width = value
}

#[no_mangle]
pub extern "C" fn set_height(h: &mut Heapy, value: f64) {
    h.height = value
}
