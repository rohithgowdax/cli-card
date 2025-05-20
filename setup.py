from setuptools import setup, find_packages

setup(
    name="rohith",                     # Replace with your package name
    version="0.1.3",                   # Replace with your package version
    packages=find_packages(),          # Automatically find packages in the current directory
    include_package_data=True,
    install_requires=[                  # These will be automatically installed when someone installs your package using pip
        "questionary",
        "rich",
        "requests"
    ],
    entry_points={ 
        "console_scripts": [
            "rohith=rohith.cli:main"  # This points to the main() function inside the cli.py file within the rohith/ package.
        ]
    },
    author="Rohith Gowda R",        # Replace with your name
    description="A terminal-based CLI card to showcase Rohith Gowda's profile and quick contact tools.",       # Replace with a short description of your package
    # Make sure to have a README.md file in the same directory as this setup.py
    long_description=open("README.md").read(),  # This will read the content of your README file and use it as the long description
    long_description_content_type="text/markdown",  # Specify the format of the long description
    url="https://github.com/rohithgowdax/cli-card",  # The URL of your package's repository
    classifiers=[
        "Programming Language :: Python :: 3",      # Specify the Python versions you support
        "License :: OSI Approved :: MIT License"    # Replace with the license you are using
    ],
)
