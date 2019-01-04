#[no_mangle]
pub extern "C" fn doubled(x: i32) -> i32 {
    x * 2
}

#[repr(C)]
pub struct Vector3 {
    pub x: f64,
    pub y: f64,
    pub z: f64,
}

impl Vector3 {
    fn length(&self) -> f64 {
        (self.x.powi(2) + self.y.powi(2) + self.z.powi(2)).sqrt()
    }
}

#[no_mangle]
pub extern "C" fn length(ptr: *const Vector3) -> f64 {
    let vector = unsafe {
        assert!(!ptr.is_null());
        &*ptr
    };
    vector.length()
}
