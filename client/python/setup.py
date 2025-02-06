from distutils.core import setup

setup(
    name = 'UnrealCV',
    packages = ['unrealcv'],
    version = '1.1.3',
    python_requires='>=3.7',
    description = 'UnrealCV client for python. see http://unrealcv.github.io for more detail.',
    author = 'Weichao Qiu, Fangwei Zhong, Hai Ci, Kui Wu',
    author_email = 'qiuwch@gmail.com',
    url = 'http://unrealcv.github.io',
    download_url = 'http://unrealcv.github.io',
    install_requires=['docker', 'opencv-python', 'pillow'],
    keywords = ['computer vision', 'unreal engine', 'ue4', 'synthetic', 'simulator', 'robotics'],
    classifiers = [],
)
