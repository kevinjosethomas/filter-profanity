import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="filter-profanity",
    version="1.0.9",
    author="TrustedMercury",
    author_email="trustedmercury@gmail.com",
    description="The fastest python module to filter and censor obscene language from strings!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TrustedMercury/filter-profanity",
    keywords="profanity, filter, censor",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
