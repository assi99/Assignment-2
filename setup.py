from setuptools import setup, find_packages
setup(name='study_reminders', version='1.0.0', packages=find_packages(), install_requires=['schedule>=1.2.0'], entry_points={'console_scripts':['study-reminders=study_reminders.main:main']})
