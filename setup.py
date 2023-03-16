from setuptools import setup, find_namespace_packages

setup(name = 'cleaner_project',
      version='1.0.4',
      description='Helps to clean folders',
      long_description='This module helps to sort files to the appropriate folders.Contains folders for images, videos, documents, audios, archives',
      author = 'Anna Pekarska',
      license='MIT license',
      url='https://github.com/Pekarska/homework_6',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['sorting_files = clean_folder.my_project:main_sorting_fnct']}
    )
