from setuptools import setup


def readme():
    with open("README.rst") as f:
        return f.read()


setup(name="pycloudstream",
      version="0.1",
      description="Send messages to spring cloud stream",
      long_description=readme(),
      url="https://github.com/michal-kk/pycloudstream",
      author="Michal Kopec",
      author_email="lekkoscbytu@gmail.com",
      license="MIT",
      packages=["pycloudstream"],
      install_requires=["pika"],
      zip_safe=True,
      entry_points={
          "console_scripts": [
              "pycloudstream-send=pycloudstream.command_line:main",
              ],
      })
