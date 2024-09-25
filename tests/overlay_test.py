import pathlib
import subprocess

from utils import check_root


def test_build():
    """Test to create an overlay on an Apptainer container.  This will add persistent storage for a container so that it can write to its internal folders.

    Raises:
        RuntimeError: Display the error message from building an overlay.
    """
    check_root()

    # Create the output directory
    pathlib.Path("save").mkdir(parents=True, exist_ok=True)

    # Run the sbatch script and capture output
    results = subprocess.run(
        ["singularity", "overlay", "create", "--size", "128", "save/base.sif"],
        capture_output=True,
        text=True,
        check=False,
    )

    # Check for error when sent to scheduler
    if results.returncode != 0:
        raise RuntimeError(f"Invalid result: { results.returncode }, Error: {results}")
