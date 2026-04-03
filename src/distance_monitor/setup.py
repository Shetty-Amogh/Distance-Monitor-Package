from setuptools import find_packages, setup

import os
from glob import glob
from setuptools import setup

package_name = 'distance_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*.launch.py'))),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amoghshetty',
    maintainer_email='amoghshetty@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'distance_publisher = distance_monitor.distance_publisher:main',
        'distance_subscriber = distance_monitor.distance_subscriber:main',
        ],
    },
)
