from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    # name="logger",
    # version="0.1.0",
    # license="BSD",

    # description="パッケージの説明",
    # author="作成者",
    # url="GitHubなどURL",
    # packages=find_packages("src"),
    # package_dir={"": "src"},
    # zip_safe=False,
    # py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    # include_package_data=True,


    # install_requires=_requires_from_file('requirements.txt'),
    # setup_requires=["pytest-runner"],
    # tests_require=["pytest", "pytest-cov"]
)
