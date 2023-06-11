"""
Creates folder and files as defined in the project layout (user input)
"""


import os


def create_layout(base_path: str, project_structure: dict) -> None:
    """
    Creates the needed directories and files as specified in
    the project layout.

    Args:
        base_path: root directory of the project.
        project_structure: project structure in dict format.

    Returns:
        None.

    Raises:
      OSError: If base_path already exists.
    """

    # creating parent dir
    os.mkdir(base_path)

    # creating layout
    def recursion(my_dict, curr_dir):
        for k, v in my_dict.items():
            if isinstance(v, dict):
                # make dirs
                print(f'{k}', ':', os.path.join(curr_dir, k))
                os.makedirs(os.path.join(curr_dir, k), exist_ok=True)
                recursion(v, os.path.join(curr_dir, k))
            else:
                # make files
                print(f'{k}', ':', os.path.join(curr_dir, k))
                open(os.path.join(curr_dir, k), 'w', encoding='utf-8').close()

    recursion(project_structure, base_path)


if __name__ == '__main__':
    # example below - Flask Tutorial Project Layout
    project_layout = {
        'flaskr': {
            '__init__.py': None,
            'db.py': None,
            'schema.sql': None,
            'auth.py': None,
            'blog.py': None,
            'templates': {
                'base.html': None,
                'auth': {
                    'login.html': None,
                    'register.html': None
                },
                'blog': {
                    'create.html': None,
                    'index.html': None,
                    'update.html': None
                }
            },
            'static': {
                'style.css': None
            }
        },
        'tests': {
            'conftest.py': None,
            'data.sql': None,
            'test_factory.py': None,
            'test_db.py': None,
            'test_auth.py': None,
            'test_blog.py': None
        },
        '.venv': {},
        'pyproject.toml': None,
        'MANIFEST.in': None
    }

    create_layout('test', project_layout)
