# YAAFC: Yet Another Absurd File Commander

## Features

- Norton Commander-like file management interface
- User-friendly web-based UI built with reflex.dev
- Modular and extensible architecture
- File operations: navigate, copy, move, delete, rename
- Drag-and-drop functionality for file operations
- Search functionality for files and directories
- File previews for images, text files, and other formats
- Customizable toolbar and keyboard shortcuts
- Multiple themes and layout customization
- Profile and settings management

## Prerequisites

- Python 3.12 or higher
- Docker (optional for containerized setup)
- Node.js (for frontend development, if needed)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Docker Setup

1. Build the Docker image:

   ```bash
   docker build -t yaafc .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8000:8000 yaafc
   ```

## Usage

1. Start the application:

   ```bash
   python yaafc/yaafc.py
   ```

2. Access the web interface at `http://localhost:8000`.

## Development

### Project Structure

- `yaafc/`: Main application package
  - `components/`: UI components
  - `config/`: Configuration files
  - `models/`: Database models
  - `pages/`: Application pages
  - `states/`: Global application states
  - `templates/`: Page templates
  - `ui/`: UI utilities and widgets
  - `utilities/`: Helper functions
- `tests/`: Unit tests
- `assets/`: Static assets (images, icons, etc.)
- `docs/`: Documentation files
- `scripts/`: Development helper scripts

### Running Tests

1. Install test dependencies:

   ```bash
   pip install pytest pytest-cov
   ```

2. Run tests:

   ```bash
   pytest --cov=yaafc tests/
   ```

### Using uv Package Manager

The `uv` package manager is used for dependency management and task execution in this project. To get started:

1. Install `uv`:

   ```bash
   pip install uv
   ```

2. Sync dependencies:

   ```bash
   uv sync
   ```

3. Run tasks using `uv` commands. For example:

   ```bash
   uv run reflex run
   ```

### Using Poe the Poet

`Poe the Poet` is a task runner integrated into this project. It simplifies running common tasks. The available tasks are defined in the `pyproject.toml` file under `[tool.poe.tasks]`.

#### Available Commands

- **Run the application**:

  ```bash
  poe run
  ```

- **Install dependencies and pre-commit hooks**:

  ```bash
  poe install
  ```

- **Check code quality**:

  ```bash
  poe check
  ```

- **Run tests with coverage**:

  ```bash
  poe test
  ```

- **Build the project**:

  ```bash
  poe build
  ```

- **Clean build artifacts**:

  ```bash
  poe clean-build
  ```

- **Test documentation build**:

  ```bash
  poe docs-test
  ```

- **Serve documentation locally**:

  ```bash
  poe docs
  ```

- **Deploy documentation to GitHub Pages**:

  ```bash
  poe docs-deploy
  ```

- **Upgrade dependencies**:

  ```bash
  poe bump
  ```

### How It Works

YAAFC is a web-based file commander inspired by Norton Commander. It uses the reflex.dev framework for both backend and frontend, providing a seamless and interactive user experience. The application is designed to be modular, allowing for easy addition of new features and tools.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
