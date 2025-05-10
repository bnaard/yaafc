# YAAFC Yet another absurd file commander - Project Planning

## Project Overview

This project implements a Norton Commande-like file commander in the web using reflex.dev framework. The goal is to provide a user-friendly interface for managing files and directories, similar to the classic Norton Commander.
The project is designed to be modular and extensible, allowing for easy addition of new features and tools.
It is meant as a tool to be installed on a local computer or a server to manage files and directories. of that computer or server.

## Architecture

- **Backend and Frontend Framework**: Managed by reflex.dev
- **Database**: using the built-in database of reflex.dev
- **File Management**: Uses the built-in file management capabilities of python pathlib

## Components

1. **Files View**

   - Implements the main functionality similar to classic Norton Commander
   - Displays files and directories in a view, which shall be fully configurable
   - Allows users to navigate, copy, move, and delete files and directories
   - Provides a command line interface for executing commands
   - Supports drag-and-drop functionality for file operations
   - Allows users to create, rename, and delete files and directories
   - Provides a search functionality to find files and directories
   - Supports file previews for images, text files, and other common formats
   - Allows users to view and edit file properties (size, type, date modified)
   - Provides a customizable toolbar for quick access to common actions
   - Supports keyboard shortcuts for common actions
   - Allows users to customize the appearance and layout of the interface
   - Provides a help section with documentation and tips for using the tool
   - Supports multiple themes for the interface

2. **Layout View**

   - Helps to configure the layout of the files view
   - Allows users to customize the appearance and layout of the interface
   - Provides a drag-and-drop interface for rearranging components
   - Allows users to save and load custom layouts
   - Provides a preview of the layout changes before applying them
   - Supports multiple themes for the interface
   - Customization is based on a 6-by-4 grid system
   - Allows users to add, remove components in the layout
   - Provides the user with a choice of different components to add to the layout
   - Allows users to customize the position of components in the layout
   - Provides a help section with documentation and tips for using the tool
   - Supports keyboard shortcuts for common actions

3. **Profile View**

   - Allows users to manage their profiles
   - Provides a list of profiles that can be selected
   - Allows users to create, edit, and delete profiles

4. **Settings View**
   - Allows users to configure various settings for the tool
   - Provides a list of settings that can be customized
   - Allows users to save and load custom settings
   - Provides a preview of the settings changes before applying them
   - Supports multiple themes for the interface

## File Structure

```text
yaafc/
├── assets/               # Static assets (images, icons, etc.)
├── context/              # Context files for AI assistants with general rules, requirements and tasks
│   ├──PLANNING.md        # Project planning (this file)
│   ├── PRD01_table_polars_dataframe.md # Project requirements document
│   ├── TASKS.md          # Task tracking
├── docs/                 # Documentation files for mkdocs
├── scripts/              # Helper scripts used during development of the project
├── tests/                # Unit tests for the project
├── yaafc/                # Main package
│   ├── config/           # Configuration files
│   ├── models/           # Models for reflex.dev built-in database management
│   ├── pages/            # Pages for reflex.dev
│   ├── states/           # Global states for reflex.dev
│   ├── templates/        # Templates for reflex.dev pages
│   ├── ui/               # UI components for the application based on reflex.dev ui components
│   ├── utilities/        # Utility functions for the application
│   ├── __init__.py       # Package initialization
│   ├── yaafc.py          # Main application file
├── codecov.yml           # Code coverage configuration
├── CONTRIBUTING.md       # Contribution guidelines
├── LICENSE               # Project license
├── mkdocs.yml            # MkDocs configuration
├── pyproject.toml        # Python project configuration including Poe the poet task configuration
├── requirements.txt      # Python dependencies
└── rx.config             # Reflex.dev configuration
```

## 📎 Style & Conventions

- **Use Python** as the primary language.
- Follow PEP8 standards
- Use type hints for all functions, for all function parameters and return values
- Use type hints for all class attributes and variables
- Use f-strings for string formatting
- Use snake_case for variable and function names
- Use CamelCase for class names
- Document functions with Google-style docstrings
- Format code with ruff
- use isort for sorting imports
- use mypy for type checking
- use pre-commit for pre-commit hooks
- use tox-uv for testing
- use deptry for dependency management
- use mkdocs for documentation
- use markdownlint for markdown linting
- use mkdocstrings for generating documentation from docstrings
- use pytest for testing
- use pytest-cov for code coverage
- use pytest-mock for mocking in tests

## Python Package Manager

Use uv for dependency management and poe for task management.

## Dependencies

- reflex
- polars
- pytest
- pytest-cov
- pre-commit
- tox-uv
- deptry
- mypy
- pytest-cov
- ruff
- mkdocs
- mkdocs-material
- mkdocstrings[python]

## AI Assistant Context

### Webpages to fetch

Always fetch and read the following webpages before starting a new task:

- [Reflex Documentation](https://reflex.dev/docs/getting-started/introduction/)
- [Polars Documentation](https://docs.pola.rs/)
- [Radix UI Colors](https://www.radix-ui.com/colors)

## Reflex Guidelines

- Create new reflex-based components for this project always in the `yaafc/ui` directory
- When creating a component, as much as possible use the following blueprint:

```python
class Table(rx.ComponentState):
    @classmethod
    def create(cls, *children, **props) -> rx.Component:
        return rx.component(
            cls,
            *children,
            **props,
        )

table = Table.create
```

- when using a component created in this project, always use the following blueprint:

```python
import yaafc.ui as ui

table = ui.table()
```

- Use Reflex state for all app state.
- Use Chakra UI components for layout and forms.
- Add docstrings to all public functions.
- Only comment on complex business logic.
- Sanitize all user inputs.
- Lazy-load images and large components.
- Never expose stack traces in error messages.

## Markup and Tailwind CSS Guidelines

### Keep Markup Simple

- Aim for a maximum nesting depth of 3-4 levels
- Avoid excessive conditional rendering that creates multiple levels of nesting
- Use sensible defaults for CSS with minimal override complexity

### Tailwind Best Practices

- Use Tailwind's utility classes directly in HTML/JSX for most styling
- Extract reusable patterns to components rather than creating custom classes
- For complex components, consider grouping Tailwind classes with template literals
- Utilize Tailwind's `@apply` directive sparingly and only for highly reused patterns
- Create consistent spacing, color and typography systems through Tailwind configuration

## Code Elegance Guidelines

### Simplicity Principles

- Functions should generally be under 20 lines
- Components should generally be under 150 lines
- Aim for component props to be under 7 items
- Use destructuring for cleaner component interfaces
- Group related state items in meaningful objects
- Follow the principle of least knowledge (components only know what they need)
- Use `isort` to sort imports
- Use `ruff` to format code
- Use `mypy` for type checking
- Always order contents of `__all__` alphabetically

## Implementation Instructions

- **Always read all the following listed project requirements documents** before starting a new task and check the requirements in this file. Implement all requirements in this file in the order of priority. When finished with one requirement, set it's status to "Completed" and add the date of completion. If a requirement is not relevant anymore, set it's status to "Not relevant" and add the date of this decision.
  - [ ] PRD01_table_polars_dataframe.md
