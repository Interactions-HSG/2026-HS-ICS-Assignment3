#!/usr/bin/env bash
# Installs the C compiler, gdb and Valgrind into the Codespace.
#
# NOTE: this is here so you can write your report and check that your code compiles in
# the browser. A Codespace is a 64-bit Intel/AMD machine in a data centre -- it is not
# your Raspberry Pi and cannot reach it. Everything you hand in as a result (screenshots,
# addresses, measurements) has to come from the Pi.
set -euo pipefail

echo "Installing gcc, gdb, valgrind and make..."
sudo apt-get update -qq
sudo apt-get install -y -qq --no-install-recommends gcc libc6-dev gdb valgrind make python3

echo
gcc --version | head -1
echo "Tools ready. Try: make all"
