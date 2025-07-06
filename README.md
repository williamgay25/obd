# OBD-II Python Scripts

This project contains example scripts for connecting to a vehicle's OBD-II port and reading diagnostic information using the [`python-OBD`](https://github.com/brendan-w/python-OBD) library.

## Installation

1. **Clone this repository** (if you haven't already):

    ```sh
    git clone git@github.com:williamgay25/obd.git
    cd obd
    ```

2. **Create a virtual environment (optional but recommended):**

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install the required package:**

    ```sh
    pip install obd
    ```

## Usage

Make sure your OBD-II adapter is plugged in and note the serial port (e.g., `/dev/cu.usbserial-210`). You can list available serial devices with:

```sh
ls /dev/cu.*