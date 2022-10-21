#!/usr/bin/env python3
#
# Copyright (c) 2022 Cisco and/or its affiliates.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Build the Virtual Environment

import argparse
import glob
import logging
import os
import argparse
from pathlib import Path
import signal
from subprocess import Popen, PIPE, STDOUT, call
import sys
import time
import venv
import datetime

# Pip version pinning
pip_version = "22.3"
pip_tools_version = "6.9.0"
setuptools_version = "65.5.0"
script_dir = os.path.dirname(os.path.realpath(__file__))
requirements_file = os.path.join(script_dir, "requirements.txt")
pip_compiled_requirements_file = os.path.join(script_dir, "requirements-3.txt")


def show_progress(stream):
    """
    Read lines from a subprocess stdout/stderr streams and write
    to sys.stdout & the logfile
    """
    while True:
        s = stream.readline()
        if not s:
            break
        data = s.decode("utf-8")
        # Filter the annoying SIGTERM signal from the output when VPP is
        # terminated after a test run
        if "SIGTERM" not in data:
            sys.stdout.write(data)
            logging.debug(data)
        sys.stdout.flush()
    stream.close()


class ExtendedEnvBuilder(venv.EnvBuilder):
    """
    1. Builds a Virtual Environment for running VPP unit tests
    2. Installs all necessary scripts, pkgs & patches into the vEnv
         - python3, pip, pip-tools, papi, scapy patches &
           test-requirement pkgs
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post_setup(self, context):
        """
        Setup all packages that need to be pre-installed into the venv
        :param context: The context of the virtual environment creation
                        request being processed.
        """
        # Set the venv python executable & binary install path
        env_exe = context.env_exe
        bin_path = context.bin_path
        # Packages/requirements to be installed in the venv
        # [python-module, cmdline-args, package-name_or_requirements-file-name]
        test_req = [
            ["pip", "install", f"pip==={pip_version}"],
            ["pip", "install", f"pip-tools==={pip_tools_version}"],
            ["pip", "install", f"setuptools==={setuptools_version}"],
        ]
        if config.compile_reqs is True:
            test_req.append(
                [
                    "piptools",
                    "compile",
                    "-q",
                    "--generate-hashes",
                    requirements_file,
                    "--output-file",
                    pip_compiled_requirements_file,
                ]
            )
        test_req.append(["piptools", "sync", pip_compiled_requirements_file])
        for req in test_req:
            args = [env_exe, "-m"]
            args.extend(req)
            print(args)
            p = Popen(args, stdout=PIPE, stderr=STDOUT, cwd=bin_path)
            show_progress(p.stdout)


def build_venv():
    # Builds a virtual env containing all the required packages and patches
    # for running VPP unit tests
    if not os.path.exists(venv_install_done):
        env_builder = ExtendedEnvBuilder(clear=True, with_pip=True)
        print(f"Creating a Virtual Env in {config.venv_dir}")
        env_builder.create(config.venv_dir)
        # Write state to the venv run dir
        Path(venv_run_dir).mkdir(exist_ok=True)
        Path(venv_install_done).touch()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Virtual Env Builder Tool")
    parser.add_argument("--compile-reqs", required=False, action="store_true")
    parser.add_argument("venv_dir", type=Path)
    config = parser.parse_args()

    # Required Std. Path Variables
    venv_bin_dir = os.path.join(config.venv_dir, "bin")
    venv_lib_dir = os.path.join(config.venv_dir, "lib")
    venv_run_dir = os.path.join(config.venv_dir, "run")
    venv_install_done = os.path.join(venv_run_dir, "venv_install.done")
    if os.path.exists(os.path.dirname(config.venv_dir)):
        build_venv()
        print(
            f"Source following file to active the virtual environment:\n{venv_bin_dir}/activate"
        )
    else:
        sys.exit(f"ERROR: venv parent directory does not exist: '{config.venv_dir}")
