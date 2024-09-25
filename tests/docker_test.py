import pathlib
import subprocess

from utils import check_root


def test_build():
    """Test to pull a Docker image and convert it into an Apptainer.

    Raises:
        RuntimeError: Display the error message from building an overlay.
    """
    check_root()

    # Create the output directory
    pathlib.Path("save").mkdir(parents=True, exist_ok=True)

    # Run the sbatch script and capture output
    results = subprocess.run(
        ["docker", "build", "-t", "local/ubuntu_22.04:latest", "./tests/docker/"],
        capture_output=True,
        text=True,
        check=False,
    )

    results = subprocess.run(
        [
            "singularity",
            "build",
            "save/ubuntu_22.04.sif",
            "docker-daemon://local/ubuntu_22.04:latest",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    # Check for error when sent to scheduler
    if results.returncode != 0:
        raise RuntimeError(f"Invalid result: { results.returncode }, Error: {results}")
