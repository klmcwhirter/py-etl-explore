import setuptools

setuptools.setup(
    name="py-etl-explore",
    description="exploration project of ETL with Python",
    version="0.1",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'}
)
