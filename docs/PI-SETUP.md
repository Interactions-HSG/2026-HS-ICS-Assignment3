# Setting up the Pi, and the commands for every task

Come back here whenever the sheet says "see `docs/PI-SETUP.md`".

*(New here? Read the [README](../README.md) first — it covers getting your copy of the
repository.)*

In this guide, `$USER` stands for the username you choose for your Pi and `$IP` for the Pi's IP
address. Replace both with your own values whenever you type a command.

---

## Task 1 · Install Raspberry Pi OS and reach the Pi

### 1. Write the OS image to the SD card with Raspberry Pi Imager

Download and install [Raspberry Pi Imager](https://rptl.io/imager) on your computer, insert the
SD card into your laptop, and run the Imager.

> This erases the SD card, including the files from Assignments 1 and 2. That is fine — you
> do not need them any more.

In the Imager, select:

| Setting | What to choose |
| --- | --- |
| Device / model | **Raspberry Pi 400** |
| Operating system | **Raspberry Pi OS (32-bit)** — the one *with* the Raspberry Pi Desktop, since the Raspberry Pi 400 requires the video driver |
| Storage | your SD card |

Take the **32-bit** version, not the 64-bit one the Imager may suggest first: the memory
addresses on the assignment sheet are 32-bit addresses, and yours will only look like them on
the 32-bit OS. (The description names the Debian release the OS is based on; whichever release
the Imager currently offers is fine.)

The Imager then lets you **customise** the OS before writing it. Depending on its version this
is an **Edit settings** button after pressing **Next**, or a series of steps it walks you
through. Either way, set:

- **Username and password:** a username for your Pi (e.g., `ics`) and a password (e.g.,
  `mypassword`).
- **Wireless LAN:** your SSID (e.g., `labnet`) and its password (e.g., `inthrustwetrust`).

  We recommend you use your phone as a hotspot and connect your Pi to it. Find out how to share
  the network connection on your phone and set up your own hotspot, and take note of the SSID
  and the password you configured:

  - Android: <https://support.google.com/android/answer/9059108?hl=en>
  - iPhone: <https://support.apple.com/en-us/HT204023>

  For the Pi to connect to your phone's network, use your phone's SSID (in place of `labnet`)
  and its password (in place of `inthrustwetrust`).
- **Wireless LAN country:** `CH`
- **SSH** (under *Services* or *Remote access*): enable it, with **password authentication**.

Save the settings, confirm that you want to apply them, and let the Imager write the card.

### 2. Find your Pi in the Wi-Fi network

Insert the SD card into the Pi and power it on. It should connect to the configured Wi-Fi
network by itself (this can take a few minutes on the first boot). If it does not, connect the
Pi to a monitor with the HDMI cable from the box and join the Wi-Fi by hand: click the Wi-Fi
icon in the top right corner of the desktop.

To connect to the Pi over the network, you first have to find its IP address.

If the Pi is connected to your phone's hotspot, your phone may list the connected devices with
their IP addresses — then you can go straight to step 3. Otherwise:

Connect your computer to the same Wi-Fi as the Pi. The MAC addresses of the devices on a network
can be obtained with the
[Address Resolution Protocol (ARP)](https://en.wikipedia.org/wiki/Address_Resolution_Protocol).
Run this in the Terminal on macOS/Linux or in PowerShell on Windows:

```sh
arp -a
```

The Wi-Fi network interface of a Raspberry Pi 400 has a
[MAC address](https://en.wikipedia.org/wiki/MAC_address) with a specific prefix like
`E4:5F:01:xx:xx:xx` — it shows that the device is from the
[Raspberry Pi Foundation](https://udger.com/resources/mac-address-vendor-detail?name=raspberry_pi_foundation).
So in the `arp` output, look for the IP address next to a MAC address that starts with
`E4:5F:01`.

If you cannot find it this way, you can connect the Pi to your computer with an Ethernet cable
instead (see this [tutorial](https://gist.github.com/chengguizi/590a4621135da3ff720158f5e9b0b0d5)),
or scan your network with [Nmap](https://www.redhat.com/sysadmin/quick-nmap-inventory) on Linux
or [LanScan](https://www.iwaxx.com/lanscan/) on macOS/Windows.

### 3. Log in to the Pi with SSH

Open a terminal on your computer and type (with your own values for `$IP` and `$USER`):

```sh
ssh $IP -l $USER
```

When you see a message like this one, you are logged in to the Pi:

```console
Linux raspberrypi 6.6.51+rpt-rpi-v8 #1 SMP PREEMPT Debian 1:6.6.51-1+rpt3 (2024-10-08) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Nov 21 13:08:09 2024 from $IP
$USER@raspberrypi:~ $
```

From now on, there are **two** terminals in your life: one on your computer, and one that is
logged in to the Pi. The prompt (`…@raspberrypi`) tells you which one you are typing into.

### 4. Copy files between your computer and the Pi

The convenient way to do this is the secure-copy tool
[SCP](https://www.ssh.com/academy/ssh/scp). Run these commands **on your computer**, from the
main folder of your repository.

Copy the code folders and the `Makefile` to a folder `a3` in your home directory on the Pi:

```sh
ssh $USER@$IP "mkdir -p a3"
scp -r Task3 Task4 Task5 Makefile $USER@$IP:a3/
```

Copy a single file back from the Pi after you changed it there:

```sh
scp $USER@$IP:a3/Task3/stack_and_heap.c Task3/stack_and_heap.c
```

(Put a path in quotation marks if it contains spaces or special characters.)

> **Your repository is the hand-in, not the Pi.** Whatever you edit on the Pi has to come back
> to your computer and be committed and pushed. The safest habit: edit on your computer, copy
> to the Pi, run there.

You can also set up **public key authentication**, so you do not have to type the password
every time. Knowing how to set up key-based authentication is a valuable skill that you will
need many times in the years to come — hence, go for this! Follow this guide:
<https://www.ssh.com/academy/ssh/authorized-keys-openssh>

### 5. Check the gcc version

On the Pi:

```sh
gcc --version
```

Take a screenshot of the terminal showing the output and save it in your repository as
**`screenshots/t1.png`**. Copy the first line of the output into section 1.1 of `REPORT.md`.

---

## Task 3

All commands in this part are typed **on the Pi**, in the folder with the code:

```sh
cd ~/a3/Task3
```

### 3.2 b) Run the code using gcc

Compile the code:

```sh
gcc stack_and_heap.c -o stack_and_heap
```

If the memory error is not already shown, profile the code with Valgrind. Install it (once):

```sh
sudo apt install valgrind
```

Compile with debug information, so that Valgrind can tell you line numbers:

```sh
gcc -g -Og stack_and_heap.c -o stack_and_heap
```

Profile and run the code:

```sh
valgrind ./stack_and_heap
```

### 3.2 c) Debug the code

The following is an example string to cause the buffer overflow. Any string longer than 30
characters should show a visible effect on the stack bytes.

```
anexercisetoexplaintheheapandstackmemoryallocationanddeaclloactioninc
```

Compile the code without optimisation:

```sh
gcc -g -O0 stack_and_heap.c -o stack_and_heap
```

Run the code:

```sh
./stack_and_heap
```

Debug the code:

```sh
gdb ./stack_and_heap
```

Inside gdb, set a breakpoint (pick a line *after* the one that reads your input):

```
b stack_and_heap.c:line_number
```

start the program:

```
run
```

and, once it stops at the breakpoint, show the stack bytes:

```
x/40x $sp
```

Take the screenshot of these stack bytes and save it as **`screenshots/t3_2c.png`**. Leave gdb
with `quit`.

### 3.3 Memory traces

```sh
gcc -finstrument-functions foo.c -o foo
```

```sh
./foo
```

Take a screenshot of the output and save it as **`screenshots/t3_3.png`**.

---

## Task 4

```sh
cd ~/a3/Task4
gcc matrix_multiplication.c -o matrix_multiplication
./matrix_multiplication
```

If your program takes arguments (the matrix sizes, for example), describe how to call it in the
comment at the top of `matrix_multiplication.c`.

---

## Task 5

Compile and link to the math library:

```sh
cd ~/a3/Task5
gcc calculate_gflops.c -o calculate_gflops -lm
```

```sh
./calculate_gflops
```

Do this **twice**: once on the Pi and once on your own machine.

- **It takes a while.** The program multiplies matrices of every size from 1 to 999, and the
  big ones are slow — on the Pi the whole run can take an hour or more. Keep the Pi powered and
  the SSH session open.
- **Keep the numbers.** Save the output to a file while still seeing it on the screen:

  ```sh
  ./calculate_gflops | tee results_rpi.tsv
  ```

  Copy that file back to your computer with `scp` (see step 4 above). The columns are separated
  by tabs, so a spreadsheet program opens it directly.
- **Plot** the GFLOPS (third column) against the matrix size (first column), one plot per
  device, with whatever tool you like — a spreadsheet, Python, gnuplot. Save the plots as
  **`screenshots/t5_rpi.png`** and **`screenshots/t5_local.png`**.

**No gcc on your own machine?**

- **macOS:** run `xcode-select --install` in the Terminal; after that the `gcc` command works.
- **Linux:** `sudo apt install gcc` (or your distribution's equivalent).
- **Windows:** follow <https://phoenixnap.com/kb/install-gcc-windows>, or use WSL if you have
  it.

---

## The short way: `make`

The repository has a `Makefile` that wraps the commands above. It works on the Pi (you copied
it there in step 4), on macOS and on Linux. Run it from the folder that contains the
`Makefile` — on the Pi that is `~/a3`.

```console
make all               # compile everything into build/ -- a quick "does it all compile?"
make valgrind          # Task 3.2 b) -- compile stack_and_heap.c and run it under Valgrind
make gdb               # Task 3.2 c) -- compile stack_and_heap.c for debugging and open gdb
make foo               # Task 3.3    -- compile foo.c with -finstrument-functions and run it
make matrix            # Task 4      -- compile matrix_multiplication.c
make gflops            # Task 5      -- compile calculate_gflops.c
make clean             # remove build/
```

The compiled programs land in `build/`, e.g. `./build/calculate_gflops`.

---

## When something does not work

| Problem | What to try |
| --- | --- |
| The Pi never shows up in the network | Check SSID and password for typos (they are case-sensitive). A phone hotspot must be switched on and **visible** *before* the Pi boots; on an iPhone, keep the hotspot settings screen open and turn on *Maximise Compatibility*. If all else fails, connect a monitor and join the Wi-Fi by hand. |
| `ssh: connect to host … port 22: Connection refused` | SSH was not enabled in the Imager settings. Write the card again, or connect a monitor and enable SSH under *Preferences → Raspberry Pi Configuration → Interfaces*. |
| `Permission denied` when logging in | Wrong username or password — they are the ones you set in the Imager, not your laptop's. |
| `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!` | You re-imaged the Pi, so it has a new identity. Run `ssh-keygen -R $IP` on your computer and connect again. |
| `gcc: command not found` on the Pi | You probably installed the *Lite* OS. Run `sudo apt update && sudo apt install build-essential gdb`. |
| `sudo apt install valgrind` cannot find the package | Run `sudo apt update` first. The Pi needs internet access for this. |
| The addresses in your gdb output start with `0x7ff…` instead of `0xbe…`/`0xff…` | You are on a 64-bit OS, or not on the Pi at all. Check with `getconf LONG_BIT` — it must print `32`. |
| The Pi's IP address changed | Hotspots hand out new addresses now and then. Repeat step 2. |
