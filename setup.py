from setuptools import setup

package_name = 'voice_control_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Darshmehar',
    maintainer_email='example@email.com',
    description='Voice Controlled Robot',
    license='MIT',
    entry_points={
        'console_scripts': [
            'voice_node = voice_control_robot.voice_node:main',
            'command_node = voice_control_robot.command_node:main',
        ],
    },
)
