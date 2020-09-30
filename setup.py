import setuptools

setuptools.setup(
    name                            = "tutorial-additional-metrics",
    description                     = "Additional metrics for models in orquestra.",
    url                             = "https://github.com/zapatacomputing/tutorial-additional-metrics",
    packages                        = setuptools.find_packages()),
    package_dir                     = {"" : "python"},
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires = [
        "sklearn",
        "numpy",
   ],
)