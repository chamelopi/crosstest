#!/usr/bin/env python3

import sys
import os
import subprocess
import shutil

supported_targets = ["linux", "win"]

def print_usage():
    """Print program usage"""
    print("Usage: {} <target_system>".format(sys.argv[0]))
    print(" where <target system> can be one of the following")
    print("  - linux (Linux x86_64")
    print("  - win   (Windows x64 MinGW")
    print("")

def build_target(target):
    """Compile using specific toolchain file"""
    builddir = "build_" + target
    toolchain = "toolchain-{}.cmake".format(target)

    if not os.path.isfile(toolchain):
        print("Error: There is no toolchain for {}!".format(target))
        sys.exit(1)
    # If build directory exists, remove it
    if os.path.isdir(builddir):
        shutil.rmtree(builddir)

    os.makedirs(builddir)
    os.chdir(builddir)
    # If cmake fails, don't make!
    if (subprocess.call(["cmake", "..", "-DCMAKE_TOOLCHAIN_FILE=../" + toolchain ])) == 0:
        subprocess.call(["make"])

    os.chdir("..")


if __name__ == "__main__":
    # Check if called from the root directory,
    # because of relative paths
    if not os.path.dirname(os.path.realpath(__file__)) == os.getcwd():
        print("Expected to be in '{}' but am in '{}'!")
        sys.exit(1)

    if len(sys.argv) != 2:
        print("Error: Expected exactly one argument!")
        print_usage()
        sys.exit(1)

    target = sys.argv[1]
    if not target in supported_targets and not target == "all":
        print("Error: '{}' is not supported as compilation target!".format(target))
        print_usage()
        sys.exit(1)

    if target == "all":
        for t in supported_targets:
            print("    " + "* "*30)
            print("        BUILDING FOR TARGET {}".format(t))
            print("    " + "* "*30)

            build_target(t)
            print()
    else:
        build_target(target)
    sys.exit(0)
