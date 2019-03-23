from setuptools import setup

setup(
        name="pythonwp",
        packages=["pythonwp"],
        include_package_data=True,
        install_requires=[
            "flask",
            "flask-sqlalchemy",
            "flask-migrate",
            "mysql-python",
        ]
)
