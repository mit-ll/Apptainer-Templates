import pathlib
import subprocess

from utils import check_root


def build_container(build_args):
    """Build an Apptainer with the passed build arguments.

    Raises:
        Exception: Throws an error if any of the builds fail.
    """

    check_root()

    # Create the output directory
    pathlib.Path("save").mkdir(parents=True, exist_ok=True)

    # Run the sbatch script and capture output
    result = subprocess.run(
        build_args,
        capture_output=True,
        text=True,
        check=False,
    )

    # Check for error when sent to scheduler
    if result.returncode != 0:
        raise RuntimeError(f"Invalid result: { result.returncode }, Error: {result}")


def test_build_core():
    build_args = [
        "singularity",
        "build",
        "--force",
        "save/core.sif",
        "templates/core.def",
    ]

    build_container(build_args)


def test_build_miniconda():
    build_args = [
        "singularity",
        "build",
        "--force",
        "save/miniconda.sif",
        "templates/miniconda.def",
    ]

    build_container(build_args)


def test_build_base():
    build_args = [
        "singularity",
        "build",
        "--force",
        "save/base.sif",
        "templates/base.def",
    ]

    build_container(build_args)
