#!/usr/bin/env python3
import argparse, os
from pathlib import Path
import docker


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("imagetag", type=str, help="Docker image tag to build in")

    parser.add_argument("file", type=str, help="Source code file")

    parser.add_argument(
        "-o",
        "--outfile",
        type=str,
        help="Build output file",
        default="",
    )

    parser.add_argument(
        "-p",
        "--packages",
        type=str,
        help="Comma-separated additional packages to install",
        default="gcc",
    )

    parser.add_argument(
        "-dr",
        "--dont-remove",
        action='store_true',
        help="When set, don't remove build container")
    
    parser.add_argument(
        "-c",
        "--command",
        help="Custom build command",
        default=""
    )

    args = parser.parse_args()

    args.packages = args.packages.split(",")
    if '' in args.packages:
        args.packages.remove('')

    if "gcc" not in args.packages:
        args.packages.append(args.packages)



    client = docker.from_env()

    container = client.containers.run(
        args.imagetag,
        '/bin/bash',
        tty=True,
        detach=True,
        volumes=[f"{os.getcwd()}:/root/"]
    )

    container.exec_run("apt update")
    container.exec_run(f"apt install -y {' '.join(args.packages)}")

    output = container.exec_run(args.command if args.command else f"gcc {args.file} -o {args.outfile if args.outfile else Path(args.file[:-2]).stem}", workdir="/root")

    print(output.output.decode())

    if not args.dont_remove:
        container.stop()
        container.remove()
    else:
        print(f"Container ID: {container.id}")

