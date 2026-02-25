from setuptools import setup, find_packages

setup(
    name='road_surface_recognition',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python',
        'PyYAML',
        'scikit-learn',
        'torch',
        'torchvision',
        'matplotlib',
    ],
) 
