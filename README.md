#  vscode-devcontainer-aws-sam-local

Develop and debug AWS SAM functions locally from VS Code Dev Containers

![Debug Tab UI in VS Code](assets/screenshot.png)

## Prerequisites

- Docker (tested on macOS and Linux)
- VS Code with *Remote - Containers* extension installed

## Usage

1. Clone the repository
    ```sh
    git clone https://github.com/ilyasotkov/aws-sam-local-python-devcontainer.git
    ```
2. (Only needed on Linux): Modify [.devcontainer/devcontainer.json](https://github.com/ilyasotkov/aws-sam-local-python-devcontainer/blob/main/.devcontainer/devcontainer.json) by uncommenting one of the lines in `runArgs` property depending on your Docker version.

3. Open the cloned folder in VS Code. You'll be prompted to reopen in container, agree by pressing "Reopen in container".
3. Wait for container image to build and container to launch and VS Code extensions to download.
4. Go to [`./src/main.py`](https://github.com/ilyasotkov/aws-sam-local-python-devcontainer/blob/main/src/main.py). Uncomment all commented out lines so that the Lambda function will wait for VS Code debugger to attach. Set a breakpoint in the `lambda_handler` function.
5. Go to the debug tab in VS Code, and press on "Start Debugging". Debugger should automatically attach and hit the breakpoint that you've set.
