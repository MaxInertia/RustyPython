A small experiment in using Rust Structs and calling Rust Functions from Python... By telling Rust to expose stuff to C and telling Python to call C!

Purpose: To assist in learning Rust and Python at the same time.

Primary resource is/was https://bheisler.github.io/post/calling-rust-in-python/
If you are interested I highly recommend checking it out.

CFFI docs: https://cffi.readthedocs.io/en/latest/index.html

### Setup
- Install Rust and Python
- run `pip install cffi`

### Testing
- Compile rust with `cargo build`
- Run python with `python test.py`

### Tested with the following dependency versions
- rustc 1.31.1 (b6c32da9b 2018-12-18)
- cargo 1.31.0 (339d9f9c8 2018-11-16)
- python 2.7.15
- cffi 1.11.5
