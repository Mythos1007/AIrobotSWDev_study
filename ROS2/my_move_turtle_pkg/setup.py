from setuptools import find_packages, setup

package_name = 'my_move_turtle_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mythos',
    maintainer_email='mythos@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
          'move_turtle_pub = my_move_turtle_pkg.move_turtle_pub:main',
          'move_turtle_sub = my_move_turtle_pkg.move_turtle_sub:main',
        ],
    },
)
